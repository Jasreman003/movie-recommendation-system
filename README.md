# 🎬 Movie Recommendation System

## 📌 Project Overview
This project is a Movie Recommendation System built using the MovieLens dataset.  
It recommends movies similar to a given movie based on user ratings using collaborative filtering.

---

## 🎯 Objective
To build a system that suggests relevant movies to users by analyzing rating patterns and similarities between movies.

---

## 📂 Project Structure
```
movie-recommendation-system/
│
├── data/
│   ├── Movie_Id_Titles
│   └── u.data
│
├── images/
│   ├── correlation_heatmap.png
│   ├── rating_distribution.png
│   ├── ratings_count_distribution.png
│   ├── most_rated_movies.png
│   └── top_rated_movies.png
│
├── notebooks/
│   └── movie-recommendation.ipynb
│
├── requirements.txt
└── README.md
```

---

## 📊 Dataset
- MovieLens Dataset  
- Contains:
  - User IDs
  - Movie IDs
  - Ratings
  - Movie Titles  

---

## ⚙️ Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  

---

## 🧠 Methodology

### 1. Data Preprocessing
- Loaded ratings and movies datasets  
- Merged datasets using `item_id`  

### 2. Exploratory Data Analysis (EDA)
- Analyzed:
  - Most rated movies  
  - Highest rated movies  
- Created visualizations:
  - Rating distribution  
  - Number of ratings distribution  
  - Top movies bar charts  
  - Correlation heatmap  

### 3. Feature Engineering
- Created a **user-movie matrix** using pivot table  

### 4. Recommendation System
- Used **Collaborative Filtering**  
- Applied **Pearson Correlation** to find similar movies  

```python
movie_matrix.corrwith()
```

---

## 📈 Visualizations

### 🔹 Top Rated Movies
![Top Rated Movies](images/top_rated_movies.png)

### 🔹 Most Rated Movies
![Most Rated Movies](images/most_rated_movies.png)

### 🔹 Rating Distribution
![Rating Distribution](images/ratings_distribution.png)

### 🔹 Ratings Count Distribution
![Ratings Count Distribution](images/ratings_count_distribution.png)

### 🔹 Correlation Heatmap
![Correlation Heatmap](images/correlation_heatmap.png)

---

## 🔍 How It Works

1. User selects a movie  
2. System finds similarity with other movies using correlation  
3. Filters movies with sufficient number of ratings  
4. Recommends top similar movies  

---

## 📈 Key Insights

- Popular movies tend to have more stable ratings  
- Movies with very few ratings can have misleading high averages  
- Correlation works better when filtering movies with sufficient ratings  
- User behavior patterns help in identifying similar movies  

---

## 🙌 Author

**Jasreman Kaur**  
Aspiring Data Analyst  

## 📬 Contact

If you have any questions or would like to connect, feel free to reach out:

- 💼 LinkedIn: https://www.linkedin.com/in/jasreman-kaur-818568298