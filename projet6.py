import numpy as np

num_students = int(input("Entrez le nombre d'élèves : "))
num_subjects = int(input("Entrez le nombre de matières : "))

note = np.ones((num_students , num_subjects))

for i in range(num_students):
    print(f"\n Entrer les notes pour l'eleve {i + 1}:")
    for j in range(num_subjects):
       note[i,j]= float(input(f"Matiere {i + 1}:"))

total = np.sum(note, axis=1)

porcentage = (total/ (num_subjects * 100)) * 100

def calculate(porcentage):
    if porcentage >= 90:
        return 'A+'
    elif porcentage >= 80:
        return 'A'
    elif porcentage >= 70:
        return 'B+'
    elif porcentage >= 60:
        return 'B'
    elif porcentage >= 50:
        return 'C'
    else:
        return 'F' 
