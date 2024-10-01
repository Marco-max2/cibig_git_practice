#afficher un message donc on utilise la fonction print
from linecache import clearcache

print("seq_gen")
#ecrire une variable
var_str = "variable chaine de caractere"
print(var_str)
var_num = 6
print(var_num)
var_bool = False
print(var_bool)
var_str_2 = "6"
print(var_str_2)
conv_var_bool_to_int= int(var_bool)
print(conv_var_bool_to_int)
conv_var_num_to_bool= bool(var_num)
print(conv_var_num_to_bool)
message="variable numerique:"
print(message,var_num)
message= "variable booleenne"
print(message,var_bool)
print("message:",var_str)
# apprendre à faire les opérations
# les operations d'addition
# je definis deux variables a et b
a= 7
b= 13
c=a+b
print("c=",c)
a=a+b
print("a=a+b :",a)
a +=b
print("a += b :",a)
# additionner deux variables de differentes natures (str et numerique)
f= str(var_num)+var_str_2
print(f)
f= var_num + float(var_str_2)
print(f)
print("additionner deux variables de differentes natures : "+str(a+b))
print(f"additionner deux variables de differentes natures : {a+b} ")C
clearcache()

