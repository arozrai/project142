import pandas as pd
import numpy as np

df = pd.read_csv('final.csv')

C = df['total_events_mean'].mean()
m = df['total_events'].quantile(0.9)
q_movies = df.copy().loc[df['total_events'] >= m]

def weighted_rating(x, m=m, C=C):
    v = x['total_events']
    R = x['total_events_average']
    return (v/(v+m) * R) + (m/(m+v) * C)

q_movies['score'] = q_article.apply(weighted_rating, axis=1)

q_movies = q_movies.sort_values('score', ascending=False)

output = q_movies[['title', 'image_link', 'release_date', 'total_events', 'overview']].head(20).values.tolist()

