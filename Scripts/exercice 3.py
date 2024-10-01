# nous avons une liste

# j'affiche le contenu de ma liste avec la fonction while
animal_list = ['cow', 'mouse', 'yeast', 'bacteria']
# la condition d'arrêt de notre liste
nombre_elements = len(animal_list)
print(nombre_elements)
i = 0
while i < nombre_elements:
    print(i, animal_list[i])
    i = i + 1
# j'affecte la liste des éléments à la variable animal
# utilisation de la boucle for
for animal in animal_list:
    print(animal)
    print(f"la liste des animaux est :{animal}")



