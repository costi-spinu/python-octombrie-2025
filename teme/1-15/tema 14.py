# Task
# Two lists of integers are filled with random numbers. Do the following:
# •	Create the third list containing elements of both lists;
# •	Create the third list containing elements of both lists without repetitions;
# •	Create the third list containing elements common to both lists;
# •	Create the third list containing elements that are unique to each list;
# •	Create the third list containing only the smallest and the largest values of each list.
################################################################################################################################

print("Task 1")
# Two lists of integers are filled with random numbers. Do the following:
import random

lun_lista1 = random.randint(2, 10)
lun_lista2 = random.randint(2, 10)
lista1 = [random.randint(-100, 100) for c in range(lun_lista1)]
lista2 = [random.randint(-100, 100) for c in range(lun_lista2)]
print("Lista 1:", lista1)
print("Lista 2:", lista2)
# •	Create the third list containing elements of both lists;
lista3 = lista1 + lista2
print("Lista 3 cu elementele din ambele liste:\n\t", lista3)
# •	Create the third list containing elements of both lists without repetitions;
# ####### varianta 1
# lista4 = list(
#     set(lista3)
# )  ##comanda set elimina elemente repetitive si aranjeaza aleatorii valorile din lista ,neaparat si comanda list
# print("Lista 4 fara elemente repetitive:\n\t", lista4)
####### varianta 2
lista4_1 = []
for elem_com in lista3:
    if elem_com not in lista4_1:
        lista4_1.append(elem_com)
print("Lista 4.1 fara elemente repetitive cu ordinea numerelor pastrata:\n\t", lista4_1)
# •	Create the third list containing elements common to both lists;
lista5 = []
for x in lista1:
    if x in lista2 and x not in lista5:
        lista5.append(x)
print("Lista 5 elemente comune din ambele liste:\n\t", lista5)
# •	Create the third list containing elements that are unique to each list;
lista6 = []
for elem in lista1:
    if elem not in lista2 and elem not in lista6:
        lista6.append(elem)
for elem in lista2:
    if elem not in lista1 and elem not in lista6:
        lista6.append(elem)
print("Lista 6 cu elemente unice din ambele liste:\n\t", lista6)
# •	Create the third list containing only the smallest and the largest values of each list.
lista7 = [min(lista1), max(lista1), min(lista2), max(lista2)]
nr_max_lst1, nr_min_lst1, nr_max_lst2, nr_min_lst2 = lista7
print("Lista 7 doar cu elementele minime si maxime din cele doua liste:\n\t", lista7)
print("numar maxim lista 1 =", nr_max_lst1)
print("numar minim lista 1 =", nr_min_lst1)
print("numar maxim lista 2 =", nr_max_lst2)
print("numar minim lista 2 =", nr_min_lst2)
