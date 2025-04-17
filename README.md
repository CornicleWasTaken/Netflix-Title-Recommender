Netflix Movie Recommender System

This project is a simple content-based movie recommender system built with Python. It uses the Netflix dataset to suggest similar movies based on title, cast, genre, director, and description. You can run it in the terminal or as a web app using Streamlit.

📁 Project Structure

netflix-recommender/
│
├── netflix_titles.csv          # Netflix dataset from Kaggle
├── netflix_recommender.py      # Command-line version
├── streamlit_app.py            # Streamlit web app version
└── README.txt                  # Project guide (you're reading it!)

📦 Requirements

Install the required libraries using pip:

```pip install pandas scikit-learn streamlit```

📥 Dataset

Download the dataset from Kaggle:  
📎 Netflix Movies and TV Shows Dataset: https://www.kaggle.com/datasets/shivamb/netflix-shows

- Save the file as netflix_titles.csv in the project directory.

🧪 How to Use

📍 Option 1: Command Line Version

Run the terminal app:

```python netflix_recommender.py```

Then enter a Netflix movie title when prompted, for example:

Enter a Netflix movie title: The Matrix

Top 5 recommendations:
- The Signal
- Spectral
- ARQ
- The Cloverfield Paradox
- IO

🌐 Option 2: Web App Version (Streamlit)

To run the web-based version:

```streamlit run streamlit_app.py```

This will open a browser window with a clean interface where you can enter a movie name and view recommended titles instantly.

🔍 How It Works

- Combines key movie metadata (cast, director, genre, description).
- Converts text data into vectors using TF-IDF.
- Calculates similarity using cosine similarity.
- Returns the top 5 most similar movies to the one you entered.

🚧 Limitations

- Only works for titles present in the dataset.
- Doesn't consider user ratings or viewing history.
- Recommendation quality depends on available metadata.

✅ To-Do Ideas

- Add fuzzy matching for movie titles.
- Implement collaborative filtering.
- Deploy to Streamlit Cloud for public access.




Dataset © Netflix via Kaggle (https://www.kaggle.com/datasets/shivamb/netflix-shows).
