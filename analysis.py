import matplotlib
matplotlib.use('Agg') # Tells python to save files quietly without a popup window

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load the cleaned dataset
df = pd.read_csv("data/anime_dataset_cleaned.csv")
print(f"loaded {len(df)} rated entries for analysis.")

# split genres string and explode to group individual genres fairly
df["genres_list"] = df["genres"].str.split("|")
df_exploded = df.explode("genres_list")

# aggregate stats per individual genre
genre_stats = (
    df_exploded.groupby("genres_list")
    .agg(
        average_score=("score", "mean"),
        total_members=("members", "sum"),
        anime_count=("title", "count"),
    )
    .reset_index()   
)

# filter out the extreme outliers (requires at least 100 to show)
genre_stats = genre_stats[genre_stats["anime_count"] >= 100]

# sort genres by highest average rating
genre_stats_sorted = genre_stats.sort_values(
    by="average_score", ascending=False
)

print("\nTop 5 Highest Rated Genres on Average:")
print(genre_stats_sorted[["genres_list", "average_score"]].head())

# set up the visualization style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10,6))

# create a horizontal bar chart of the top 15 genres
top_15_genres = genre_stats_sorted.head(15)
sns.barplot(
    x="average_score", y="genres_list", data=top_15_genres, palette="viridis" 
)

# apply formatting to meet rubric requirements
plt.title(
    "Average User Score by Anime Genre (Top 15)",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Average Score (1-10 scale)", fontsize=12)
plt.ylabel("Genre", fontsize=12)
plt.xlim(5.5, 7.5) # focus on the range where most genres fall

# save the visualization directly to the repository 
plt.tight_layout()
plt.savefig("genre_rating_analysis.png", dpi=300)
print("\nanalysis complete. visualization saved to 'genre_rating_analysis.png'.")

# calculate overall correlation to complete the analysis 
correlation = df["members"].corr(df['score'])
print(f"\npopularity-to-score correlation coefficient: {correlation:.2f}")
