# nous allons demander à un utilisateurs de saisir 3 notes
#comment on calcule la moyenne de ces trois notes
from linecache import clearcache

grade1 = input("Enter first grade: ")
grade2 = input("Enter second grade: ")
grade3 = input("Enter third grade: ")

# calcule la somme
gradet = float(grade1) + float(grade2) + float(grade3)
print(gradet)
# claculer la moyenne
moyenne = gradet/3
print(moyenne)
print(f"la somme est : {gradet:.2f}")
# mettre les commentaires en fonction de la moyenne
print(f"la moyenne est : {moyenne:.2f}")


# si la moyenne obtenue est supérieure ou egale à 16 imprime, very good
if moyenne>=16:
     print(" very good")
# si la moyenne est supérieure ou égale, à 14 imprime good
elif moyenne>=14:
    print("good")
# dans la mesure ou la moyenne est supérieure ou égle à 12 imprime fairly good
elif moyenne>=12:
    print("fairly good")
# dans le cas ou la moyenne est égale à 10 imprime passable
elif moyenne>=10:
    print("passable")
# si aucune des conditions précédentes n'est valable, imprime failed
else:
    print("failed")










