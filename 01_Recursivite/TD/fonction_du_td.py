def fct_recursive() :
    print("Je suis un appel de la fonction")
    fct_recursive()

def somme(n) :
    if n == 0 :
        return 0
    else :
        return n + somme(n-1)
    
def factorielle(n) :
	if n == 0 :
		return 1
	else :
		return n * factorielle(n-1)
	
def mystere(i,k):
    if i<=k :
    	print(i)
        boucle(i+1,k)

def maximum(t):
    if len(t) == 0:
        return -1
    elif len(t) == 1 :
        return t[0]
    else :
        return max(t[0], maximum(t[1:]))

def syracuse(u):
    print(u)
    if u > 1 :
        if u%2 == 0 :
            return syracuse(u//2)
        else :
            return syracuse(u*3 + 1)