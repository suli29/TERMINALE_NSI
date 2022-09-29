# Correction TP Noté :

------

## Exercice 1 :

```python
def longueur(tab : list):
    """
    
    """
    if tab == [] :
        return 0
    else :
        return 1 + longueur(tab[1:])
    
def puissance(nb : int, exposant : int) :
    """
    
    """
    if exposant == 0 :
        return 1
    else :
        return nb * exposant(nb,exposant-1)
```

## Exercice 2 :

```python
class Ordinateur :
    def __init__(self,puissance : int, marque : str) :
        self.puissance = puissance
        self.marque = marque
        if self.puissance <= 4 :
            self.pc_gamer = True
        else : 
            self.pc_gamer = False
    def reprogrammation(self,nouvelle_puissance) :
        self.puissance = nouvelle_puissance
        if self.puissance <= 4 :
            self.pc_gamer = True
        else : 
            self.pc_gamer = False
        
```

