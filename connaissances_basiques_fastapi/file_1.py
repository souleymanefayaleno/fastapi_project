print("---------------------Q0------------------------")

print("Création de la liste de 5 animaux")

animals_list = ["rabbit", "cat", "dog", "mouse", "horse"]

print("---------------------Q1------------------------")

print("Suppression de l'animal d'index 3 de la liste")

animals_list.pop(3)

print(animals_list)

print("---------------------Q2------------------------")

print("Ajout d'un animal à la fin de la liste")

animals_list.append("dog")

print(animals_list)

print("---------------------Q3------------------------")

print("Suppression du prémier animal de la liste")

animals_list.pop(0)

print(animals_list)

print("---------------------Q4------------------------")

print("Affichage de tous les animaux de la liste")

for animal in animals_list:
    print(animal)

print("---------------------Q5------------------------")

print("Affichage des 3 premiers animaux de la liste")

for animal in animals_list[0:3]:
    print(animal)

print("---------------------Q6------------------------")

print("Affichage des 2 derniers animaux de la liste")

for animal in animals_list[2:]:
    print(animal)
