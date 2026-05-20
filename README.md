# data science project

## assignment overview
the goal of this project was to apply data science principles to a real world dataset. using a comprehensive anime dataset, the objective was to programmatically clean the raw data, perform structured data analysis to uncover trends, and generate a clear visualization representing the insights.

---

## dataset & methodology

### 1. data cleaning (`clean_data.py`)
the raw dataset contains extensive information on thousands of anime entries, including genres, user scores, and popularity metrics. the cleaning script prepares this data for mathematical processing by:
* handling missing values and dropping incomplete data entries.
* filtering out unrated items to ensure analytical accuracy.
* outputting a refined target dataset for the analysis script.

### 2. data analysis (`analysis.py`)
the analysis script processes the cleaned dataset to identify how different anime genres perform relative to one another. because entries often contain multiple genres combined together, the script:
* isolates individual genres to evaluate them fairly.
* computes statistical metrics, including the mean scores for each genre.
* calculates correlation coefficients to evaluate the mathematical relationship between popularity metrics and final user ratings.

### 3. visualization
the project concludes by utilizing data visualization libraries to map out the statistical results. the script automatically exports a structured distribution graph saved as `genre_rating_analysis.png` to visually highlight the trends found during analysis.

---

## project structure
* **`data/`**: directory containing the source dataset which includes the original 'anime_dataset.csv' file and the cleaned 'anime_dataset_cleaned.csv' file.
* **`clean_data.py`**: filters and structures the raw data.
* **`analysis.py`**: runs statistical computations and generates the plot.
* **`genre_rating_analysis.png`**: the final generated analytical chart.
* **`README.md`**: project overview and summary.

