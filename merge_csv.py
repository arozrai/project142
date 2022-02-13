import csv

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]

headers.append("poster_link")

with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)

with open("articles_links.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles_links = data[1:]

for articles_item in all_articles:
    poster_found = any(articles_item[8] in articles_link_items for articles_link_items in all_articles_links)
    if poster_found:
        for articles_link_item in all_articles_links:
            if articles_item[8] == articles_link_item[0]:
                articles_item.append(articles_link_item[1])
                if len(articles_item) == 28:
                    with open("final.csv", "a+") as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(articles_item)