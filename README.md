# Tetris

## !!!!!

En gros, j'ai fait:

- un Block est composé de plusieurs Box ET d'une Shape definissant la disposition de ces Box. On le construit en donnant la Shape + l'emplacement du carré en haut a gauche. Il stocke la liste de ces carrés, pour les afficher on itere dedans on affiche tout

- une Box est un carré (5x5 par defaut), definit par 4 point: topLeft, botLeft, etc. On le construit en donnant le Point en haut a gauche et la taille

- un Point = int x, int y

- Shapes = enumeration des differents blocks (inversions comprises)
