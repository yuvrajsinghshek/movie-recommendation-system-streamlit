# Movie Recommendation System

A personalized movie recommendation web-app built using Streamlit, Pandas, and a trained ML model.
Users can filter movies by genre, language, year, cast, and rating preference, and instantly get a curated list of movie suggestions.

## Features

Select single genre

Choose preferred language

Filter movies by minimum release year

Option to show Top Rated movies only

Search movies by cast name

### Displays:

🎞 Title

⭐ Rating

📅 Release Year

⏱ Runtime

🎭 Cast

🎬 Director

🏁 Status

## Project Structure
movie_recommendation_app/
│── app.py
│── movies.ipynb
│── reco_df.csv
│── requirement.txt
│── revenue_model.zip   ← compressed ML model file
│── README.md

## Installation
### Clone the repository
git clone https://github.com/yuvrajsinghshek/movie_recommendation_app.git
cd movie_recommendation_app

### Install dependencies
pip install -r requirement.txt

## Important — Model File Note

GitHub does NOT allow large .pkl files, so this project includes:

### revenue_model.zip

Inside it there is your trained ML model:

revenue_model.pkl

## How to Use:

Download revenue_model.zip from the repository

Extract it

Place revenue_model.pkl in the same folder where app.py is located

Your folder should look like:

app.py
revenue_model.pkl
reco_df.csv


app.py will automatically load the model from this file.

## Run the Streamlit App
streamlit run app.py


App will open in the browser automatically.

## Model Description

A regression model trained to analyze & utilize movie metadata

Uses cleaned and feature-engineered dataset

Helps refine movie recommendations alongside filters

## Author

Yuvraj Singh Shekhawat
Aspiring Data Scientist | Python & SQL | ML & Data Analytics
🔗 GitHub: https://github.com/yuvrajsinghshek

🔗 LinkedIn: https://www.linkedin.com/in/yuvraj-singh-shekhawat-155719316

## Support

If you like this project, don’t forget to star the repo!
