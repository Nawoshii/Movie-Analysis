import requests
import pandas as pd

# Replace with your TMDb API Key
api_key = "54ed4a45904939ecafec3b864e9a3525"

# Define the TMDb API URL for popular movies
url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1"

# Fetch data from API
response = requests.get(url)
data = response.json()

# Extract relevant details
movies = []
for movie in data["results"]:
    movies.append({
        "title": movie["title"],
        "release_date": movie["release_date"],
        "vote_average": movie["vote_average"],
        "popularity": movie["popularity"]
    })

# Convert to DataFrame
df_movies = pd.DataFrame(movies)

# Display top movies
print(df_movies.head())

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,5))
sns.histplot(df_movies["vote_average"], bins=10, kde=True)
plt.title("Distribution of Movie Ratings")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(data=df_movies, x="vote_average", y="popularity", hue="release_date", palette="coolwarm")
plt.title("Popularity vs Ratings of Movies")
plt.xlabel("Ratings")
plt.ylabel("Popularity")
plt.show()

df_movies.to_csv("popular_movies.csv", index=False)

