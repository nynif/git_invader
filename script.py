import os
import subprocess
from datetime import datetime, timedelta
import random

# Remplir start_date et decommenter pour dessiner INVADER
# La date init doit être un vendredi
start_date = datetime.strptime("2022-11-04", "%Y-%m-%d")
level_1 = [19, 33]
level_2 = []
level_3 = []
level_4 = [0, 6, 7, 11, 12, 13, 17, 18, 20, 21, 25, 26, 27, 31, 32, 34, 35, 39, 40, 41, 48, 49, 56]

# Remplir start_date et decommenter pour dessiner POKEY
# La date init doit être un mardi
# start_date = datetime.strptime("2023-01-10", "%Y-%m-%d")
# level_1 = [0, 1, 2, 3, 4, 6, 9, 10, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 30, 31, 32, 34, 37, 38, 42, 43, 44, 45, 46]
# level_2 = []
# level_3 = []
# level_4 = [7, 14, 15, 28, 35, 36]


# Créer un fichier avec un contenu initial
filename = "file.txt"
with open(filename, "w") as f:
    f.write("Contenu initial\n")

# Ajouter le fichier à l'index Git et faire le premier commit
subprocess.run(["git", "add", filename])
subprocess.run(["git", "commit", "-m", "Commit initial"])

# Fonction pour faire un commit à la date start_date + i days
def add_commit_to_date(i):
    commit_date = start_date + timedelta(days=i, hours=random.randint(1, 10))
    commit_date_str = commit_date.strftime("%a %b %d %H:%M:%S %Y %z")

    # Modifier le fichier
    with open(filename, "a") as f:
        f.write(f"Modification pour le commit {i}\n")

    # Ajouter le fichier modifié à l'index Git
    subprocess.run(["git", "add", filename])

    # Faire le commit avec la date spécifiée
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = commit_date_str
    env["GIT_COMMITTER_DATE"] = commit_date_str
    subprocess.run(["git", "commit", "-m", f"Commit {i}"], env=env)

for i in level_1:
    add_commit_to_date(i)

for i in level_2:
    add_commit_to_date(i)
    add_commit_to_date(i)

for i in level_3:
    add_commit_to_date(i)
    add_commit_to_date(i)
    add_commit_to_date(i)

for i in level_4:
    add_commit_to_date(i)
    add_commit_to_date(i)
    add_commit_to_date(i)
    add_commit_to_date(i)