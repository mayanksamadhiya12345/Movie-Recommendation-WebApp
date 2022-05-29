# Movie_Recommender

![Python](https://img.shields.io/badge/Python-3.8-blueviolet)
![Framework](https://img.shields.io/badge/Framework-Flask-red)
![Frontend](https://img.shields.io/badge/Frontend-HTML/CSS/JS-green)
![API](https://img.shields.io/badge/API-TMDB-fcba03)

Built this project for Microsoft Engage 2022 mentorship program

[live project link](https://www.google.com)
# Project-working video link
[documentation link](https://docs.google.com/document/d/1lUxrAwOHD4NpXEiNzpjfIm82YD7fBnIbhQVDbYPGP0o/edit?usp=sharing)


# Overview
A Movie Recommendation web app which lets users register and search for a movie and gives the movie as a result and other recommended movies as well. It helps users to add movies in the favourite list and based on the favourite list, our recommendation engine will suggest some movies in the recommendation letter. We have taken data till 2017 so it will give results according to that.


# Tech Stack
<strong>Frontrnd</strong> : HTML, CSS, JavaScript <br />
<strong>Backend</strong> : Flask, python <br />
<strong>Database</strong> : MySQL <br />
<strong>Important Packages Used</strong> : numpy, pandas, scikit-learn, seaborn, email, requests, re, contractions, nltk, ast, unique, index, BytesIO, dump, Flask, SQLAlchemy, CountVectorizer, TfidfVectorizer, cosine_similarity, NormalPredictor, surprise <br />
<strong>API Used</strong> : TMDB API <br />
<strong>Deployed on</strong> : 



# Features
A user can use our webapp with sign-in and without registering on the website. User can also register(sign-up) on the webapp for personalized recommendations.

1. <strong>Without registration (Cosine Similarity Model): </strong><br />
User can search for a movie and this webapp will give that movie as an output with their respective recommendations using Cosine Similarity Model and if user wants to see more information about the movie then he or she can get more information about that movie by clicking on that movie, information like : tagline, cast, reviews, related movies, IMDB rating, runtime, release date will be shown to the user.

2. <strong>With registration (Hybrid Model): </strong><br />
For registered users, I provided some more features for their recommendations. After signing in, user can add the movies in his/her favorite list and he or she can see their favorite movies in the list later and based on their favorite movies list our model (HYBRID USING Normal Predictor) will give recommendations. And if user wants to logout then he or she can logout.


# local setup
pip install -r requirements.txt (to install all the dependencies) <br />
Start your server <br />
python main.py (to start the server)


Note : Due To Large Data I am Unable to Upload credits.csv file so you can access it by here <br />
[credits.csv](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=credits.csv)
