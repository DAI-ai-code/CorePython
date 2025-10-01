import pandas as pd
import json
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)      # Show all rows
pd.set_option('display.max_columns', None)   # Show all columns
pd.set_option('display.width', None)         # No line wrapping
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('./data/tmdb_5000_movies.csv')

def major_genre(i):
    if len(json.loads(i)) != 0:
        return json.loads(i)[0]['name']

df['major_genre'] =  df['genres'].apply(lambda x : major_genre(x))

grouped_by_major_genre = df.groupby('major_genre')

# top movies of each genre
vote_avg = grouped_by_major_genre['vote_average'].nlargest(5)
grp_avg = vote_avg.groupby('major_genre').mean().nlargest(5)

# plt.subplot(1,2,1)
# plt.figure(figsize=(16, 22))
plt.bar(grouped_by_major_genre.groups.keys(), grouped_by_major_genre.count()['genres'])
plt.title('Distribution of movies genre wise in this dataset')
plt.xlabel('Genre')
plt.ylabel('Counts')
plt.show()



# plt.subplot(2,2,2)
plt.plot(grp_avg.index, grp_avg.values)
plt.title('Average rating of top 5 movies for each genre')
plt.xlabel('Genre')
plt.ylabel('Rating')

plt.show()






