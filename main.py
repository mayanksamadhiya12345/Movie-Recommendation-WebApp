# importing the libraries 
import email
from enum import unique
from operator import index
from io import BytesIO

from pickle import dump
from flask import Flask, Request,render_template,request,redirect,flash,send_file
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint, Table, select, true
from flask_login import UserMixin
from flask_login import login_required,logout_user,login_user,login_manager,LoginManager,current_user
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import requests

import re
import numpy as np
import contractions


# make suring the databse connection
local_server = True
app = Flask(__name__)
app.secret_key = "mayank_engage_2022"


# unique user access
# login_manager = LoginManager(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view="login"


# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql:///username:password@localhost/databasename"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@127.0.0.2:3307/medserv"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@127.0.0.2:3307/moviedata"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 


# make suring the current user login
@login_manager.user_loader
def load_user(user_id):
    return Movieuserdata.query.get(int(user_id))


# making a class for storing user login/sign up data in Movieuserdata table
class Movieuserdata(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    useremail = db.Column(db.String(100))
    
    userpassword =  db.Column(db.String(100))
    
# making a class for storing user liked movies data in likemovie table
class likemovie(db.Model,UserMixin):
    sn = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.Integer)
    movieid = db.Column(db.Integer)											




# using NLP
import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
import pandas as pd
df = pd.read_csv('popular_movies.csv')
df = df[['movie_title']]
df["movie_title"] = df["movie_title"].str.lower()
# df.tagline.fillna('', inplace=True)
# df['description'] = df['tagline'].map(str) + ' ' + df['overview']
df.dropna(inplace=True)
df = df.sort_values(by=['movie_title'], ascending=True)


# fetching movie related details using TMDB API Key
def movie_detail(moviel):
    doc = []
    for m in moviel:
        l = []
        movie_id = get_movie_id(m)

        #fetch title
        l.append(m.title()) 

        #fetch data
        url = "https://api.themoviedb.org/3/movie/{}?api_key=cd109cb98c90d3020a252e6f524b8d63&language=en-US".format(movie_id)
        data = requests.get(url) 
        data = data.json()

        #fetch poster
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + str(poster_path)
        l.append(full_path) 

        #fetch rating
        rating = data['vote_average']
        l.append(rating) 

        #fetch runtime
        runtime = data['runtime']
        l.append(runtime)

        #fetch genre
        genres_path = data['genres']
        genrelist = []
        for i in range(len(genres_path)):
            genrelist.append(genres_path[i]['name'])
        l.append(genrelist)

        #fetch overview
        overview = data['overview']
        l.append(overview)

        #release date
        release_date = data['release_date']
        l.append(release_date)

        #vote count
        l.append(data['vote_count'])

        #tagline
        l.append(data['tagline'])

        #top-5 cast
        cast_url = "https://api.themoviedb.org/3/movie/{}/credits?api_key=cd109cb98c90d3020a252e6f524b8d63&language=en-US".format(movie_id)
        cast_data = requests.get(cast_url)
        cast_data = cast_data.json()
        cast_data
        ci = []
        for i in range(len(cast_data['cast'])):
            c = []
            c.append(cast_data['cast'][i]["name"])
            c.append(cast_data['cast'][i]["character"])
            c.append("https://image.tmdb.org/t/p/w500"+ str(cast_data['cast'][i]["profile_path"]))
            ci.append(c)
        
        l.append(ci[:5])

        #fetch review
        r_url = "https://api.themoviedb.org/3/movie/{}/reviews?api_key=cd109cb98c90d3020a252e6f524b8d63&language=en-US".format(movie_id)
        r_data = requests.get(r_url)
        r_data = r_data.json()
        r_data
        li = []
        for i in range(len(r_data['results'])):
            r = []
            r.append(r_data['results'][i]["author"])
            r.append("https://image.tmdb.org/t/p/w500"+ str(r_data['results'][i]["author_details"]["avatar_path"]))
            r.append(r_data['results'][i]["content"])
            li.append(r)
        l.append(li)


        doc.append(l)
    return doc


def movie_detail_by_id(moviel):
    doc = []
    for m in moviel:
        l = []
        movie_id = m

        #fetch title
        

        #fetch data
        url = "https://api.themoviedb.org/3/movie/{}?api_key=cd109cb98c90d3020a252e6f524b8d63&language=en-US".format(movie_id)
        data = requests.get(url) 
        data = data.json()

        #fetch poster
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + str(poster_path)
        movie = data['original_title']

        l.append(movie.title()) 

        l.append(full_path) 

        #fetch rating
        rating = data['vote_average']
        l.append(rating) 

        #fetch runtime
        runtime = data['runtime']
        l.append(runtime)

        #fetch genre
        genres_path = data['genres']
        genrelist = []
        for i in range(len(genres_path)):
            genrelist.append(genres_path[i]['name'])
        l.append(genrelist)

        #fetch overview
        overview = data['overview']
        l.append(overview)

        #release date
        release_date = data['release_date']
        l.append(release_date)

        #vote count
        l.append(data['vote_count'])

        #tagline
        l.append(data['tagline'])

        #top-5 cast
        cast_url = "https://api.themoviedb.org/3/movie/{}/credits?api_key=cd109cb98c90d3020a252e6f524b8d63&language=en-US".format(movie_id)
        cast_data = requests.get(cast_url)
        cast_data = cast_data.json()
        cast_data
        ci = []
        for i in range(len(cast_data['cast'])):
            c = []
            c.append(cast_data['cast'][i]["name"])
            c.append(cast_data['cast'][i]["character"])
            c.append("https://image.tmdb.org/t/p/w500"+ str(cast_data['cast'][i]["profile_path"]))
            ci.append(c)
        
        l.append(ci[:5])

        #fetch review
        r_url = "https://api.themoviedb.org/3/movie/{}/reviews?api_key=cd109cb98c90d3020a252e6f524b8d63&language=en-US".format(movie_id)
        r_data = requests.get(r_url)
        r_data = r_data.json()
        r_data
        li = []
        for i in range(len(r_data['results'])):
            r = []
            r.append(r_data['results'][i]["author"])
            r.append("https://image.tmdb.org/t/p/w500"+ str(r_data['results'][i]["author_details"]["avatar_path"]))
            r.append(r_data['results'][i]["content"])
            li.append(r)
        l.append(li)


        doc.append(l)
    return doc




import pandas as pd
df = pd.read_csv('main.csv')
stop_words = nltk.corpus.stopwords.words('english')
def normalize_document(doc):
    doc = re.sub(r'[^a-zA-Z0-9\s]', '', doc, re.I|re.A)
    doc = doc.lower()
    doc = doc.strip()
    doc = contractions.fix(doc)
    tokens = nltk.word_tokenize(doc)
    filtered_tokens = [token for token in tokens if token not in stop_words]
    doc = ' '.join(filtered_tokens)
    return doc


normalize_corpus = np.vectorize(normalize_document)
norm_corpus = normalize_corpus(list(df['comb']))
from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer(ngram_range=(1, 2), min_df=2)
tfidf_matrix = tf.fit_transform(norm_corpus)
tfidf_matrix.shape


# MODEL CREATION
# By using cosine_similarity
from sklearn.metrics.pairwise import cosine_similarity
def create_similarity():
    data = pd.read_csv('main.csv')
    # creating a count matrix
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['comb'])
    # creating a similarity score matrix
    similarity = cosine_similarity(count_matrix)
    return data,similarity

# Movies Recommendar function
def rcmd(m):
    m = m.lower()
    try:
        data.head()
        similarity.shape
    except:
        data, similarity = create_similarity()
    if m not in data['movie_title'].unique():
        return('Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies')
    else:
        i = data.loc[data['movie_title']==m].index[0]
        lst = list(enumerate(similarity[i]))
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
        lst = lst[1:9] # excluding first item since it is the requested movie itself
        l = []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['movie_title'][a])
        return l


#Normal Predictor MODEL 
import pandas as pd 
import ast
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
from surprise import Reader, Dataset, NormalPredictor
from surprise.model_selection import cross_validate
from sklearn.metrics.pairwise import cosine_similarity



dt = pd.read_csv("main.csv")

titles = dt['movie_title']
indices = pd.Series(dt.index, index=dt['movie_title'])
reader = Reader()
ratings = pd.read_csv('ratings_small.csv')
ratings.head()
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
nor = NormalPredictor()
trainset = data.build_full_trainset()
nor.fit(trainset)

import numpy as np
def convert_int(x):
    try:
        return int(x)
    except:
        return np.nan
    
id_map = pd.read_csv('links_small.csv')[['movieId', 'tmdbId']]
id_map['tmdbId'] = id_map['tmdbId'].apply(convert_int)
id_map.columns = ['movieId', 'id']
id_map = id_map.merge(dt[['movie_title', 'id']], on='id').set_index('movie_title')
indices_map = id_map.set_index('id')


# movie recommender function
def hybrid(userId, title):
    idx = indices[title]
    tmdbId = id_map.loc[title]['id']
    movie_id = id_map.loc[title]['movieId']
    data, similarity = create_similarity()
    sim_scores = list(enumerate(similarity[int(idx)]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:9]
    movie_indices = [i[0] for i in sim_scores]
    movies = dt.iloc[movie_indices][['movie_title', 'vote_count', 'vote_average', 'id','comb']]
    # est = []
    # for x in range(len(sim_scores)):
    #     a = sim_scores[x][0]
    #     est.append(data['movie_title'][a])
    # return est
    est = []
    for x in list(movies['id']):
        try:

            est.append(nor.predict(userId, indices_map.loc[x]['movieId']).est)
        except:
            est.append(0)
    movies['est'] = est
    movies = movies.sort_values('est', ascending=False)
    return list(movies['movie_title'].head(8))


# home page
@app.route("/", methods=['POST','GET'])
def home():
    new_data = pd.read_csv('popular_movies.csv')
    new_data['movie_title'] = new_data['movie_title'].str.lower()


    a_pop = new_data.sort_values(by=['movie_title'],ascending=True)
    b_pop = a_pop.iloc[:8,:]
    b_pop = b_pop['movie_title'].to_list()
    postsdata = movie_detail(b_pop)

    return render_template("home.html", postsdata=postsdata)


# home page after login
@app.route("/loghome", methods=['POST','GET'])
@login_required
def loghome():
    new_data = pd.read_csv('popular_movies.csv')
    new_data['movie_title'] = new_data['movie_title'].str.lower()


    a_pop = new_data.sort_values(by=['movie_title'],ascending=False)
    b_pop = a_pop.iloc[:8,:]
    b_pop = b_pop['movie_title'].to_list()
    postsdata = movie_detail(b_pop)

    return render_template("profile_home.html", postsdata=postsdata)




# getting movie ID
my_api_key = 'cd109cb98c90d3020a252e6f524b8d63'
def get_movie_id(movie):
    url='https://api.themoviedb.org/3/search/movie?api_key='+my_api_key+'&query='+ movie
    df = requests.get(url)
    df = df.json()
    movie_id = df['results'][0]['id']
    return movie_id


# search page 
@app.route("/search", methods=['POST','GET'])
def search():
    if request.method=="POST":
        try:
            movie = request.form.get("movie")
            movie_list = rcmd(movie)
            
            movie_list = np.insert (movie_list,0,movie)
            postsdata = movie_detail(movie_list)
            return render_template("index.html", postsdata = postsdata)
        except:
            return render_template("404.html")

    return render_template("index.html")


# search page after login
@app.route("/searchdash", methods=['POST','GET'])
@login_required
def searchdash():
    if request.method=="POST":
        try:
            userid = current_user.id
            movie = request.form.get("movie")
            movie = movie.lower()
            movie_list = hybrid(userid, movie)
            movie_list = np.insert (movie_list,0,movie)
            movie_list = [x.lower() for x in movie_list]
            
            postsdata = movie_detail(movie_list)
            return render_template("profile.html", postsdata = postsdata)

        except:
            return render_template("profile_404.html")

    return render_template("profile.html")




# after signup
@app.route("/signup", methods=['POST','GET'])
def signup():
    if request.method == "POST":
        funame = request.form.get('username') 
        fumail = request.form.get('email')
        
        fupass = request.form.get('password')
        fcupass = request.form.get('cpassword')

        new_data = pd.read_csv('popular_movies.csv')
        new_data['movie_title'] = new_data['movie_title'].str.lower()


        a_pop = new_data.sort_values(by=['movie_title'],ascending=False)
        b_pop = a_pop.iloc[:8,:]
        b_pop = b_pop['movie_title'].to_list()
        postsdata = movie_detail(b_pop)

        user = Movieuserdata.query.filter_by(useremail = fumail).first()
        if user :
            flash("E-mail that you have entered Already Exist")
            return render_template("home.html", postsdata = postsdata)

        new_user = db.engine.execute(f"INSERT INTO `movieuserdata` (`id`, `username`, `useremail`, `userpassword`)  VALUES (NULL, '{funame}','{fumail}','{fupass}')")


        flash("Registered Successfully !!!!")    
        return render_template("home.html", postsdata=postsdata)
    else:
        render_template(url_for('signup'))



# after login
@app.route("/login", methods=['POST','GET'])
def login():
    if request.method == "POST":
        
        umail = request.form.get('useremail') 
        upass = request.form.get('password')
        
        user = Movieuserdata.query.filter_by(useremail = umail).first()

        if user and user.userpassword == upass:
            login_user(user)
            new_data = pd.read_csv('popular_movies.csv')
            new_data['movie_title'] = new_data['movie_title'].str.lower()


            a_pop = new_data.sort_values(by=['movie_title'],ascending=False)
            b_pop = a_pop.iloc[:8,:]
            b_pop = b_pop['movie_title'].to_list()
            postsdata = movie_detail(b_pop)
            flash("You have Successfuly logged in !!!!") 

            return render_template('profile_home.html', postsdata=postsdata)

        else:
            flash("invalid credentials")
            return redirect(url_for('home'))
            


# movie information page
@app.route('/information',  methods=['POST','GET'])
def information():
    if request.method == "POST":
        try:
            movie = request.form.get("movie").lower()
            movie_list = rcmd(movie)
            movie_list = np.insert (movie_list,0,movie)
            postsdata = movie_detail(movie_list)

            return render_template('moviesingle.html', postsdata = postsdata)
        except:
            return render_template("404.html")



# movie information page after login
@app.route('/information2',  methods=['POST','GET'])
@login_required
def information2():
    if request.method == "POST":
        try:
            userid = current_user.id
            movie = request.form.get("movie")
            movie = movie.lower()
            movie_list = hybrid(userid, movie)
            movie_list = np.insert (movie_list,0,movie)
            movie_list = [x.lower() for x in movie_list]
                    
            postsdata = movie_detail(movie_list)

            return render_template('moviesingle2.html', postsdata = postsdata)
        except:
            return render_template("profile_404.html")


# page after liking the movie
@app.route('/like',  methods=['POST','GET'])
@login_required
def like():
    if request.method == "POST":
        movie = request.form.get("movie").lower()
        movie_id = get_movie_id(movie)

        new_entry = db.engine.execute(f"INSERT INTO `likemovie` (`userid`, `movieid`, `sn`)  VALUES ('{current_user.id}','{movie_id}', NULL)")
        userid = current_user.id
        movie = request.form.get("movie")
        movie = movie.lower()
        movie_list = hybrid(userid, movie)
        movie_list = np.insert (movie_list,0,movie)
        movie_list = [x.lower() for x in movie_list]
                
        postsdata = movie_detail(movie_list)
        flash("Added to Favourite List !!") 

        return render_template('moviesingle2.html', postsdata = postsdata)

    return redirect(url_for('loghome'))


# user profile page
@app.route('/like_detail',  methods=['POST','GET'])
@login_required
def like_detail():

    user_id = current_user.id

    data = likemovie.query.filter_by(userid = user_id).all()

    movie_id = []
    for i in data:
        movie_id.append(i.movieid)
    
    movie_id = list(set( movie_id))

    postsdata = movie_detail_by_id(movie_id)
    print(postsdata)
    # return "favojfg"
    return render_template('userfavoritegrid.html', postsdata = postsdata)

    
# after logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have successfully logged out")
    return redirect(url_for('home'))

# start 
app.run(debug = True)