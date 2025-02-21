#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def nb_amis(amis, prenom):
    nb=0
    i=0
    while i<len(amis)/2:
        if amis[2*i]== prenom or amis[2*i+1]==prenom: 
            nb+=1
        i+=1
    return nb

def taille_reseau(amis):
    personnes=[]
    i=0
    while i<len(amis):
        if amis[i] not in personnes:
            personnes.append(amis[i])
        i+=1
    return len(personnes)

def lecture_reseau(path):
    f_in=open(path,encoding='utf-8', mode ='r')
    
    amis=[]
    li=f_in.readline()
    li=li.strip()
    while li!='':
        tab_li=li.split(';')
        amis.append(tab_li[0])
        amis.append(tab_li[1])
        li=f_in.readline()
        li=li.strip()
    f_in.close()
    return amis

def lecture_reseau_bis(path):
    f_in=open(path,encoding='utf-8', mode ='r')
    
    lus=[]
    amis=[]
    li=f_in.readline()
    li=li.strip()
    while li!='':
        tab_li=li.split(';')
        if li not in lus :
            # on ajoute la nouvelle paire d'amis
            amis.append(tab_li[0])
            amis.append(tab_li[1])
            # on tient compte de la symetrie de la relation 
            lus.append(li)
            lus.append(tab_li[1]+';'+tab_li[0])
        li=f_in.readline()
        li=li.strip()
    f_in.close()
    return amis

def personnes(amis):
    """
    retourne le tableau des différentes personnes du tableau amis
    """
    personnes=[]
    i=0
    while i<len(amis):
        if amis[i] not in personnes:
            personnes.append(amis[i])
        i+=1
    return personnes

def ses_amis(amis, prenom):
    """
    Retourne le tableau des amis de prenom
    """
    ses_amis=[]
    i=0
    while i<len(amis)/2:
        if amis[2*i]== prenom :
            ses_amis.append(amis[2*i+1])
        elif amis[2*i+1]==prenom :
            ses_amis.append(amis[2*i])
        i+=1
    return ses_amis

#version non optimisée 
def dico_reseau(amis):
    reseau={}
    # membres du réseau 
    pers=personnes(amis)
    # construction du dictionnaire
    i=0
    while i<len(pers):
        reseau[pers[i]]=ses_amis(amis,pers[i])
        i+=1
    return reseau

def nb_amis_plus_pop(dico_reseau):
    if dico_reseau=={}:
        return 0
    
    personnes = list(dico_reseau)
    maxi=len(dico_reseau[personnes[0]])
    i=1
    while i < len(personnes):
        if len(dico_reseau[personnes[i]]) > maxi :
            maxi = len(dico_reseau[personnes[i]])
        i+=1
    return maxi

def les_plus_pop(dico_reseau):
    plus_pop=[]
    personnes = list(dico_reseau)
    maxi=nb_amis_plus_pop(dico_reseau)
    i=1
    while i < len(personnes):
        if len(dico_reseau[personnes[i]]) == maxi :
            plus_pop.append(personnes[i]) 
        i+=1
    plus_pop.sort()
    return  plus_pop


# 
