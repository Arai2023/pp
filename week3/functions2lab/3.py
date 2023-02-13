def return_movie_category(movies,cat_name): 
        out_list=[]
        for i in movies:
           curr_cat=i['category']
           if cat_name.lower()==curr_cat.lower():
                out_list.append(i)
        return out_list
out_list=return_movie_category()
print(out_list)