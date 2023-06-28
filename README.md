# 👾 Git invader 👾
Git invader est un petit projet qui permet de créer un easter egg dans le dashboard de github.  
Le dashboard de github est une data visualisation des commits réalisée sur l'année.  

![dashboard github](https://github.com/nynif/git_invader/blob/main/img/dashboard.jpg?raw=true) 
  
En changeant la date des commits on peut "hacker" ce dashboard.
En ligne de commande voici la fonction pour changer la date d'un commit 

```bash
GIT_COMMITTER_DATE="Mon 27 Mar 2023 21:19:19 BST" git commit --amend --no-edit --date "Mon 27 Mar 2023 21:19:19 BST"
```

Le script python `script.py` permet de dessiner des formes prédéfinis.  
INVADER  
![dashboard github](https://github.com/nynif/git_invader/blob/main/img/invader.jpg?raw=true) 

POKEY  
![dashboard github](https://github.com/nynif/git_invader/blob/main/img/pokey.jpg?raw=true) 

# Fonctionnement 
1. Récuperer le fichier `script.py`
2. Remplir **start_date** en fonction de la date souhaité pour le début du dessin. 
3. Decomenter les lignes **`start_date`** **`level_1`** **`level_2`** **`level_3`** **`level_4`**

- **`level_1`** correspond au case que l'on souhaitera avoir en vert leger (1 commit)
- **`level_2`** correspond au case que l'on souhaitera avoir en vert moyen - (2 commits)
- **`level_3`** correspond au case que l'on souhaitera avoir en vert moyen + (3 commits)
- **`level_4`** correspond au case que l'on souhaitera avoir en vert important (4 commits)

# Commande pour faire tourner le projet

```bash
git init 
python script.py
git remote
git push 
```