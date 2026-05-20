import pandas as pd


df = pd.read_csv("data/anime_dataset.csv")
print(f"Original dataset shape: {df.shape}")

# drop rows where critical score data is missing
df_clean = df.dropna(subset=["score"]).copy()

# fill in missing metadata with some string placeholders 
df_clean["genres"] = df_clean["genres"].fillna("Unknown")
df_clean["themes"] = df_clean["themes"].fillna("Unknown")
df_clean["studios"] = df_clean["studios"].fillna("Unknown")

# pass pipe separated string cateogires into their clean lists 
df_clean["genres_list"] = df_clean["genres"].str.split("|")
df_clean["themes_list"] = df_clean["themes"].str.split("|")
df_clean["studios_list"] = df_clean["studios"].str.split("|")

# create a lowercase title column for easier searching 
df_clean["title_lowercase"] = df_clean["title"].str.lower()

# save processed data to a separate working file
df_clean.to_csv("data/anime_dataset_cleaned.csv", index=False)
print("data cleaning complete. cleaned dataset saved to 'data/anime_dataset_cleaned.csv'.")