
# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path

#     return full_path

# def fetch_genre(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['genres']
#     genrelist = []
#     for i in range(len(poster_path)):
#         genrelist.append(poster_path[i]['name'])
#     return genrelist

# def fetch_rating(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     rating = data['vote_average']
    
#     return rating

# def fetch_runtime(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     run = data['runtime']
    
#     return run

# def fetch_overview(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     run = data['overview']
    
#     return run




# import nltk
# # nltk.download('stopwords')
# # nltk.download('punkt')
# import pandas as pd
# df = pd.read_csv('Medilab/backend/tmdb_5000_movies.csv')
# df = df[['title', 'tagline', 'overview', 'popularity']]
# df["title"] = df["title"].str.lower()
# df.tagline.fillna('', inplace=True)
# df['description'] = df['tagline'].map(str) + ' ' + df['overview']
# df.dropna(inplace=True)
# df = df.sort_values(by=['popularity'], ascending=False)


# data = pd.read_csv("Medilab/backend/tmdb_5000_movies.csv")
# def get_movie_id(movie):
    
#     data['title'] = data['title'].str.lower()
#     first = data[["id","title"]]
#     second = first[data['title']== movie]
#     rt = list(second['id'])
   
#     return rt[0]

# def posters(movies):
#     poster_list = []

#     for i in movies:
#         poster_list.append(fetch_poster(get_movie_id(i)))
#     return poster_list


# def movie_detail(moviel):

#     doc = []

#     for m in moviel:
#         l = []
#         id = get_movie_id(m)
#         l.append(m.title())
#         l.append(fetch_poster(id))
#         l.append(fetch_rating(id))
#         l.append(fetch_runtime(id))
#         l.append(fetch_genre(id))
#         l.append(fetch_overview(id))
#         doc.append(l)
#     return doc


# import re
# import numpy as np
# import contractions


# stop_words = nltk.corpus.stopwords.words('english')
# def normalize_document(doc):
#     doc = re.sub(r'[^a-zA-Z0-9\s]', '', doc, re.I|re.A)
#     doc = doc.lower()
#     doc = doc.strip()
#     doc = contractions.fix(doc)
#     tokens = nltk.word_tokenize(doc)
#     filtered_tokens = [token for token in tokens if token not in stop_words]
#     doc = ' '.join(filtered_tokens)
#     return doc
# normalize_corpus = np.vectorize(normalize_document)
# norm_corpus = normalize_corpus(list(df['description']))
# from sklearn.feature_extraction.text import TfidfVectorizer
# tf = TfidfVectorizer(ngram_range=(1, 2), min_df=2)
# tfidf_matrix = tf.fit_transform(norm_corpus)
# tfidf_matrix.shape
# from sklearn.metrics.pairwise import cosine_similarity
# doc_sim = cosine_similarity(tfidf_matrix)
# doc_sim_df = pd.DataFrame(doc_sim)
# movies_list = df['title'].values
# def movie_recommender(movie_title, movies=movies_list, doc_sims=doc_sim_df):
#     movie_idx = np.where(movies == movie_title)[0][0]
#     movie_similarities = doc_sims.iloc[movie_idx].values
#     similar_movie_idxs = np.argsort(-movie_similarities)[1:6]
#     similar_movies = movies[similar_movie_idxs]
#     return similar_movies