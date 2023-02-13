def avg_imdb_score(movies): 
      avg_score=0
      tot_movies=len(movies)
      for i in movies:
           avg_score=avg_score+i['imdb']
           avg_score=avg_score/tot_movies
           return avg_score
print('Average IMDB score of all the movies is: ')
s1=avg_imdb_score()
print(s1)