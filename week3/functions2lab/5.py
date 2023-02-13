def return_movie_category(movies,cat_name): 
        out_list=[]
        for i in movies:
           curr_cat=i['category']
           if cat_name.lower()==curr_cat.lower():
                out_list.append(i)
        return out_list
        
def avg_imdb_score(movies): 
      avg_score=0
      tot_movies=len(movies)
      for i in movies:
           avg_score=avg_score+i['imdb']
           avg_score=avg_score/tot_movies
           return avg_score

def avg_imdb_acc_to_cat(movies,cat_name):
       cat_movies= return_movie_category(movies, cat_name)
       avg_score= avg_imdb_score(cat_movies)
       return avg_score
print('Average IMDB of movies in this category is: ')
s2=avg_imdb_acc_to_cat()
print(s2)