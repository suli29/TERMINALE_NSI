# **Les listes chainées**

------

Le but de ce TP est de pouvoir définir la classe des maillons afin de définir la classe des listes chainées qui seront non cyclique et simplement chainée.

## 1. La classe Maillon

Pour rappel, un maillon(ou liste) est constitué de 2 attributs :

- Le contenu
- Le pointeur vers le suivant

S'ajoute à cela la méthode permettant d'ajouter un maillon.

La queue d'une liste chainée utilisant cette classe pointera vers un objet ```None```

Exemple d'utilisation de la classe Maillon pour faire une liste ```[1, 2, 3]```

```python
>>> m3 = Liste(3)
>>> m2 = Liste(2, m3)
>>> m1 = Liste(1, m1)
```

## 2. Première approche

0. Créer un module ```Liste.py```.

1. Définir la classe Liste avec sa documentation.

2. Utiliser la classe Liste pour créer une liste chainée de tous les nombres pair compris entre 0 et 6 inclus.

3. Quels sont les inconvénients de cette méthode pour un utilisateur lambda ?

4. Que faudrait-il faire pour faciliter l’utilisation des listes chaînées pour l’utilisateur. Dans ce cas que devra uniquement connaître l’utilisateur ?

## 3. Une meilleur approche

Il y a plusieurs approches pour structurer une liste chaînée. Elles sont plus ou moins efficaces, plus ou moins bien pensées, selon les points de vues.

Une méthode très utilisée est d’encapsuler la liste chaînée dans un objet. L’utilisateur n’a alors aucune connaissance de la structure, notamment il ne sait même pas ce qu’est un maillon. Il ne fait qu’utiliser l’interface de la liste chaînée.

5. Construire une méthode **est_vide** qui retourne True si la liste est vide, False sinon.

```python
def est_vide(self):
    """
    Renvoie Vrai si la liste est vide.

    :return: (bool) Vrai si la liste est vide, Faux sinon.
    :CU: aucune

    Exemple:
    >>> l1 = Liste()
    >>> l1.est_vide()
    True
    >>> l2 = Liste([1,2,3])
    >>> l2.est_vide()
    False
    """
```

7. Construire une méthode **ajouter_element_queue** qui ajoute un maillon à la liste chaînée. Son paramètre valeur contiendra la valeur du maillon à ajouter. On distinguera les cas où la liste est vide ou non.

```python
>>> l = Liste()
>>> l.ajoute_element_queue(1)
```

8. Surcharger la méthode **__len__** qui permet de calculer la taille de la liste avec l'utilisation de la fonction *len* de python. (De manière récursive)

9. Construire la méthode **extrait_element** qui retourne le maillon de position d’indice *i* spécifié par l’utilisateur. Le programme doit s’arrêter en fournissant un message à l’utilisateur s’il spécifie un indice non valable (préconditions, mot clé *assert* en Python).

10. Construire les méthodes usuelles sur les listes chaînées suivantes :

- ```ajouter_element_tete(self, val)``` : ajoute un maillon de valeur *val* à la tête de la liste ;
- ```supprimer_element_queue(self)``` : supprime le dernier maillon ;
- ```supprimer_element_tete(self)``` : supprime le premier maillon ;
- ```inserer_element(self, val, i)``` : insère un maillon de valeur *val* à la position d’indice *i* ;
- ```supprimer_element(self, i)``` : supprime le maillon de position d’indice *i* ;
- ```chercher_element(self, val)``` : retourne l’indice *i* du maillon recherché de valeur *val* ;
- ```renverser(self)``` : renverse la liste ;
- ```permuter_elements(self, i, j)``` : permute deux maillons de la liste d’indices *i* et *j* ;
- ```__add__(self, other)``` : retourne une nouvelle liste, concaténation de la liste avec la liste *other*.

11. Ajouter la méthode **tuple** permettant d’obtenir un tuple donnant les valeurs contenues dans la liste chaînée.

```python
>>> l = Liste([1, 2, 3])
>>> l.tuple()
(1, 2, 3)
```