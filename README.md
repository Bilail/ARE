# ARE Road project
echo "# ARE" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/Noblessse/ARE.git
git push -u origin master
hello


Aujourd'hui nous sommes constamment ammené à nous déplacer que ce soit en voiture, en transport en commun, ... et les accidents, les vicitmes de la route, les morts, les bouchons sont omniprésent et aucun pays n'y est épargné nous sommes tous touché. Néanmoins les gouvernements ont tenté de modifier des paramètres afin de limité ces accidents nous allons donc essayer de jouer sur ces paramètres pour voir les conséquence, si l'on diminue la vitesse limite, augmente les distances de sécurités, ...

Le but de notre projet est de simuler une portion de route et d'observer son évolution en jouant avec des paramètres.

Exemple de paramètres: 
- Vitesse limite
- Distance de sécurité
- Temps de réaction
- ...

# La fonction tour de piste 
Nous avons décidé de simuler notre route par une droite infini, en effet dès que le véhicule arrive au bout il revient au début et ainsi de suite créant ainsi une boucle infini. Nous localisons donc la voiture en 2 dimensions une X qui nous donne l'anvancé sur une voie et une Y qui nous indique sur quel voie il se trouve
![image](https://drive.google.com/uc?export=view&id=1ht9zwcbYT6JQ1700k_WHLjzA6Jvxz2H4)

# La fonction distance de sécurité 
Pour éviter toutes accidents et danger il est prévu dans le code de la route de respecter des distances de sécurité en prenant en compte le temps de réaction et la distance d'arrêt. 
Afin d'éviter une collision le véhicule va voir sa vitesse majoré par le véhicule de devant et devra ajuster son allure à celui-ci
![image](https://drive.google.com/uc?export=view&id=1ybzE5rZ_ue81dWm4ckhr7aPGmnzAqiK9)
![image](https://drive.google.com/uc?export=view&id=1OTUMUeRH2gG5xhWjOSpJdhsSnhdtQSmQ)

# La fonction accident 
Dans la vrai vie, un accident se produit lorsqu'il y a collision entre deux véhicules, nous avons donc programmé dans la même optique. 
C'est à dire nous avons codé de sorte que dès qu'il y ait contact entre deux véhicules alors nous avons accident.
Contact == Accident 
![image](https://drive.google.com/uc?export=view&id=1Wi-YDbQIGEAdaa1Xn9pBWd0XRrOHtKNv)

[![Vidéo simulation](https://img.youtube.com/vi/VID/0.jpg)](https://www.youtube.com/watch?v=gzuSBJBJtjs&feature=youtu.be)

# La fonction dépassement 
On parle de dépassement lorsque deux véhicules, qui circulent dans le même sens de circulation, se dépassent sur la voie publique.
En France, le code de la route indique que les dépassements s’effectuent généralement par la gauche. Il n’est possible de dépasser par la droite que lorsqu’un usager souhaite doubler un véhicule tournant à gauche.
![image](https://drive.google.com/uc?export=view&id=1PGjsLqsPi82X2FsVznO8ViQuQ_ujeFN_)


