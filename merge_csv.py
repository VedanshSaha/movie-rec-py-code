import csv

with open("movies.csv",encoding='utf8') as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)
    all_movies = data[1:]
    headers = data[0]

headers.append("poster_link")

with open('final.csv','a+',encoding='utf8') as f:
    csv_write = csv.writer(f)
    csv_write.writerow(headers)


with open("movie_links.csv",encoding='utf8') as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)
    all_movie_links = data[1:]

for i in all_movies:
  poster_found = any(i[8] in movie_link_items for movie_link_items in all_movie_links)
  if poster_found :
    for movie_link_items in all_movie_links:
      if i[8] == movie_link_items[0]:
        i.append(movie_link_items[1])
        if len(i)== 28:
          with open('final.csv','a+',encoding='utf8') as f:
            csv_write = csv.writer(f)
            csv_write.writerow(i)
