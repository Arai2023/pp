def sublist_movies_high_score(movies): 
    out_list=[]
    for i in range(0,len(movies)):
           curr_movie=movies[i]
    if curr_movie['imdb']>5.5:
            out_list.append(curr_movie)
            return out_list
    
print ('List of movies with an IMDB score > 5.5')
out_list=sublist_movies_high_score()
print(out_list)