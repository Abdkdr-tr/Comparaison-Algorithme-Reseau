#!/usr/bin/env python
# coding: utf-8


amis = {
    "Alice" : ["Bob", "Dan"],
    "Bob" : ["Alice", "Carl", "Dan"],
    "Carl" : ["Bob"],
    "Dan" : ["Alice", "Bob"]
}



'''Question 1'''
def cree_reseau(tab_amis):
    """
    Retourne un dictionnaire dont les clés sont les prénoms des membres du réseau et les valeurs, le tableau de leurs amis
    
    Paramètre :
        -tab_amis(list) : tableau de chaîne de caractère qui modélise les interactions entre les personnes d'un réseau
        
    la fonction retourne un dictionnaire qui résume les interactions de chaques personnes dans le réseau défini
    """
    
    dico_amis = {}
    
    n = len(tab_amis)
    i = 0
    while i < n:                               #on parcourt le tableau d'amis
        if i%2==0:                             #dans l'intéraction (le couple) on regarde le premier prénom
            if not tab_amis[i] in dico_amis:   #si le prénom n'est pas dans le dico, on l'ajoute comme clé avec son ami en valeur 
                dico_amis[tab_amis[i]] = [tab_amis[i+1]] 
            else:                              #si il y est mais que son ami ne l'est pas, on ajoute son ami en valeur
                if not tab_amis[i+1] in dico_amis[tab_amis[i]]:
                    dico_amis[tab_amis[i]].append(tab_amis[i+1])
        else:                                  #on regarde alors le 2e prénom du couple
            if not tab_amis[i] in dico_amis:   #on fait la même chose qu'avant mais dans l'autre sens 
                dico_amis[tab_amis[i]] = [tab_amis[i-1]]
            else:
                if not tab_amis[i-1] in dico_amis[tab_amis[i]]:
                    dico_amis[tab_amis[i]].append(tab_amis[i-1])
        i += 1
    return dico_amis



'''Question 2'''
# Voir dans compare_comu.ipynb



'''Question 3'''
def liste_personnes(reseau):
    '''
    fonction qui va créer un tableau qui contient la liste de tous les membres du réseau passé en paramètre
    
    Paramètre :
        -réseau(dict) : dictionnaire où chaque clé est une personne et dont chaque valeur est le tableau des amis de celui-ci
    '''
    liste_membres = []
    for personne in reseau:    #on parcourt le dico afin d'ajouter chaque clé comme nouvelle valeur dans le tableau créée
        liste_membres.append(personne)
    return liste_membres



'''Question 4'''
def sont_amis(reseau, a, b):
    '''
    fonction qui va vérifier l'amitié entre 2 personnes
    
    Paramètres :
        -reseau(dict) : dictionnaire où chaque clé est une personne et dont chaque valeur est le tableau des amis de celui-ci
        -a(str) : personne a
        -b(str) : personne b
    
    renvoie un booléen en fonction de si 'a' et 'b' sont réciproquement amis
    '''
    return a in reseau[b] and b in reseau[a]      #on vérifie que a et b sont réciproquement amis



'''Question 5'''
def sont_amis_de(reseau, personne, groupe):
    '''
    fonction qui vérifie si la personne mis en paramètre est amie avec tous les membres du groupe passé en paramètre
    
    Paramètres :
        -reseau(dict) : dictionnaire où chaque clé est une personne et dont chaque valeur est le tableau des amis de celui-ci
        -personne(str) : chaîne de caractère qui représente le prénom d'une personne présente dans le réseau
        -groupe(list) : tableau de chaîne de caractère qui représentent des prénoms de personnes présentes dans le réseau
    
    renvoie un booléen en fonction de la présence de tous les membres du groupe dans le réseau d'ami de la personne en paramètre
    '''
    for membre in groupe:                     #on parcourt le tableau contenant les prénoms du groupe
        if not membre in reseau[personne]:    #s'il n'est pas ami avec la personne passée en paramètre la fonction retourne faux
            return False                      #sinon elle retourne vraie
    return True


'''Question 6'''
def est_comu(reseau, groupe): 
    '''
    fonction qui vérifie si toutes les personnes du groupes sont amies entre elles
    
    Paramètres :
        -reseau(dict) : dictionnaire où chaque clé est une personne et dont chaque valeur est le tableau des amis de celui-ci
        -groupe(list) : tableau de chaîne de caractère qui représentent des prénoms de personnes présentes dans le réseau
    
    renvoie un booléen en fonction de l'amitié réciproque entre toutes les personnes du groupe en se basant sur le reseau défini
    '''
    for i, personne1 in enumerate(groupe):   #on parcourt le groupe de personnes 
        for j, personne2 in enumerate(groupe):   #on boucle de nouveau sur le groupe
            if j > i and not sont_amis(reseau, personne1, personne2):  #on vérifie que chaque personne du groupe est ami avec 
                return False                                           #toutes les autres du groupe tout en évitant de vérifier
    return True                                                        #à nouveau les personnes qui ont déja passé le test



'''Question 7'''
def comu(reseau, groupe):
    '''
    fonction qui va créer un tableau qui contient le prénom de toutes les personnes amies de tous ceux ajoutés progressivement
    au tableau
    
    Paramètre :
        -réseau(dict) : dictionnaire où chaque clé est une personne et dont chaque valeur est le tableau des amis de celui-ci
        -groupe(list) : tableau de chaîne de caractère qui représentent des prénoms de personnes présentes dans le réseau
        
    renvoie un tableau de communauté créé à partir du groupe et où chaque membre est ami avec toutes les personnes de la 
    communauté
    '''
    comu = []
    for personne in groupe:   #on parcourt le groupe de personnes
        if sont_amis_de(reseau, personne, comu):   #on ajoute la personne qui est amie avec tous les membres de la communaute qui
            comu.append(personne)                  #est créée progressivement
    return comu



# In[9]:

'''Question 8'''
def swap_tab(tab,i,j):
    '''
    fonction qui échange la place de 2 valeurs au sein du même tableau
    
    Paramètres :
        -tab(list) : tableau dans lequel les éléments doivent être échangés
        -i(int) : indice du premier élément à échanger
        -j(int) : indice du second élément à échanger
        
    la fonction modifie directement le tableau "tab"
    ''' 
    stock = tab[i]
    tab[i] = tab[j]
    tab[j] = stock

def tri_popu(reseau, groupe):
    '''
    fonction de tri par insertion qui trie les membres du groupe de la personne ayant le plus d'amis à celui qui en a le moins
   
    Paramètres :
        -reseau(dict) : dictionnaire où chaque clé est une personne et dont chaque valeur est le tableau des amis de celui-ci
        -groupe(list) : tableau des personne à trier en fonction du reseau d'amis de chacun
        
    la fonction modifie directement la table "groupe"
    '''
    n = len(groupe)
    for i, val in enumerate(groupe):    #on parcourt le groupe de personnes
        j = i+1
        while j < n:   #on compare les personnes du groupe qui sont supposées être moins populaire que le premier membre
            if len(reseau[groupe[j]]) > len(reseau[val]):   #echange la place du premier membre par le membre qui est plus 
                swap_tab(groupe, i, j)                      #populaire que lui parmis ceux qui sont à sa droite
            j += 1
        i += 1

        

# In[10]:

'''Question 9'''
def comu_dans_reseau(reseau):
    '''
    fonction qui trouve la plus grande communaute du reseau en la triant afin de faciliter la recherche
    
    Paramètre :
        -reseau(dict) : dictionnaire où chaque clé est une personne et dont chaque valeur est le tableau des amis de celui-ci
        
    renvoie le tableau des membres de la plus grande communauté trouvée
    '''
    tab_personne = liste_personnes(reseau)
    tri_popu(reseau, tab_personne)           #maximise nos probabilités de construire la plus grande des communautés du réseau
    
    communaute = comu(reseau, tab_personne)
    return communaute



# In[11]:

'''Question 10'''
def comu_dans_amis(reseau,personne):
    '''
    fonction qui trouve la plus grande des communautes possible de la personne passée en paramètre
    
    La fonction recherche les amis de la personne passée en paramètre qui sont amis avec toute la communauté qui est créée 
    progressivement

    Paramètres :
        - reseau(dict) : dictionnaire où chaque clé est une personne et dont chaque valeur est le tableau des amis de celui-ci
        - personne(str) : prénom de la personne à partir de laquelle la plus grande communauté sera trouvée
    
    renvoie le tableau des membres de la plus grande communauté de la personne trouvée
    '''
    comu = [personne]
    tri_popu(reseau, reseau[personne])   #maximise nos probabilités de construire la plus grande des communautés du réseau
    ami_tri = reseau[personne]
    
    for ami in ami_tri:   #rassemble dans le tableau comu le plus de membres que possible qui sont réciproquement amis
        if sont_amis_de(reseau, ami, comu):
            comu.append(ami)
    return comu



# In[12]:

'''Question 11'''
# Voir dans compare_comu.ipynb



# In[13]:

'''Question 12'''
def comu_max(reseau):
    '''
    fonction qui trouve la plus grande communaute existante dans le reseau défini
    
    La fonction parcourt chaque membre du réseau, trouve la communauté la plus grande qu'il peut former avec ses amis et renvoie 
    la communauté ayant le plus de membres.
    
    Paramètre :
        -reseau(dict) : dictionnaire où chaque clé est une personne et dont chaque valeur est la table des amis de celui-ci
        
    renvoie le tableau des membres de la plus grande communauté existante dans le réseau trouvée
'''
    tab_liste_comu = liste_personnes(reseau)
    
    max_comu = []
    for membre in tab_liste_comu:   #création de toutes les communautés possibles afin de trouver la plus grande d'entre elles
        communaute = comu_dans_amis(reseau, membre)
        if len(communaute) > len(max_comu):   #comparaison de la nouvelle communaute créée avec la plus grande en titre et
            max_comu = communaute             #garde la plus grande des 2
    return max_comu

