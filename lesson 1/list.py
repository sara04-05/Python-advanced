from pygame.display import set_gamma

fav_authors_list = ["kafka" , "dostoevsky" , "tolstoy" , "camus"]
author1= fav_authors_list[0]
author2= fav_authors_list[1]
author3= fav_authors_list[2]
author4= fav_authors_list[3]

print(author1)
print(author2)
print(author3)
print(author4)

shopping_list = ["clothes" , "food" , "supplies"]

shopping_list.append("shoes")
print(shopping_list)

shopping_list.insert(2 , "gloves")
print(shopping_list)

shopping_list.remove("supplies")
print(shopping_list)

del shopping_list[2]
print(shopping_list)

shopping_list[0] = "cereal"
print(shopping_list)

favorite_colors = ['green' , 'yellow' , 'brown' , 'black' , 'pink']

fourth_color = favorite_colors[3]
print(fourth_color)