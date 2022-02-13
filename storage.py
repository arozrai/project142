import csv

all_article = []

with open('final.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_article = data[1:]

liked_article = []
not_liked_article = []
did_not_watch = []