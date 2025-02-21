#!/usr/bin/env python
# coding: utf-8


from comu import *



amis = {
    "Alice" : ["Bob", "Dan"],
    "Bob" : ["Alice", "Carl", "Dan"],
    "Carl" : ["Bob"],
    "Dan" : ["Alice", "Bob"]
}



def test_cree_reseau():
    '''
    fonction qui vérifie le fonctionnement de la fonction cree_reseau
    
    renvoie soit une erreur, soit une chaîne de caractère 'Tout vas bien !' en fonction du résultat du test
    '''
    reseau = ["Alice", "Bob", "Alice", "Dan", "Bob", "Carl", "Bob", "Dan"]
    assert cree_reseau(reseau) == {"Alice" : ["Bob", "Dan"], "Bob" : ["Alice", "Carl", "Dan"], "Carl" : ["Bob"], "Dan" : ["Alice", "Bob"]}
    reseau2 = []
    assert cree_reseau(reseau2) == {}
    print("Tout vas bien !")
test_cree_reseau()



def test_liste_personnes():
    '''
    fonction qui vérifie le fonctionnement de la fonction liste_personnes
    
    renvoie soit une erreur, soit une chaîne de caractère 'Tout vas bien !' en fonction du résultat du test
    '''
    assert liste_personnes(amis) == ["Alice", "Bob", "Carl", "Dan"]
    assert liste_personnes([]) == []
    print("Tout vas bien !")
    
test_liste_personnes()



def test_sont_amis():
    '''
    fonction qui vérifie le fonctionnement de la fonction sont_amis
    
    renvoie soit une erreur, soit une chaîne de caractère 'Tout vas bien !' en fonction du résultat du test
    '''
    assert sont_amis(amis, "Alice", "Bob") == True
    assert sont_amis(amis, "Alice", "Carl") == False
    print("Tout vas bien !")

test_sont_amis()



def test_sont_amis_de():
    '''
    fonction qui vérifie le fonctionnement de la fonction sont_amis_de
    
    renvoie soit une erreur, soit une chaîne de caractère 'Tout vas bien !' en fonction du résultat du test
    '''
    assert sont_amis_de(amis, "Alice", ["Bob", "Dan"]) == True
    assert sont_amis_de(amis, "Alice", ["Carl", "Dan", "Bob"]) == False
    print("Tout vas bien !")
    
test_sont_amis_de()



def test_est_comu():
    '''
    fonction qui vérifie le fonctionnement de la fonction est_comu
    
    renvoie soit une erreur, soit une chaîne de caractère 'Tout vas bien !' en fonction du résultat du test
    '''
    grp1 = ["Alice", "Bob", "Dan"]
    grp2 = ["Alice", "Bob", "Carl"]
    
    assert est_comu(amis, grp1) == True
    assert est_comu(amis, grp2) == False
    print("Tout vas bien !")
    
test_est_comu()



def test_comu():
    '''
    fonction qui vérifie le fonctionnement de la fonction comu
    
    renvoie soit une erreur, soit une chaîne de caractère 'Tout vas bien !' en fonction du résultat du test
    '''
    grp1 = ["Alice", "Bob", "Dan"]
    grp2 = ["Carl", "Alice", "Bob", "Dan"]
    grp3 = ["Carl", "Alice", "Dan"]
    
    assert comu(amis, grp1) == ["Alice", "Bob", "Dan"]
    assert comu(amis, grp2) == ["Carl", "Bob"]
    assert comu(amis, grp3) == ["Carl"]
    print("Tout vas bien !")
    
test_comu()



def test_tri_popu():
    '''
    fonction qui vérifie le fonctionnement de la fonction tri_popu
    
    renvoie soit une erreur, soit une chaîne de caractère 'Tout vas bien !' en fonction du résultat du test
    '''
    grp = ["Alice", "Bob", "Carl"]
    tri_popu(amis, grp)
    
    assert  grp == ["Bob", "Alice", "Carl"]
    print("Tout vas bien !")
    
test_tri_popu()



def test_comu_dans_reseau():
    '''
    fonction qui vérifie le fonctionnement de la fonction comu_dans_reseau
    
    renvoie soit une erreur, soit une chaîne de caractère 'Tout vas bien !' en fonction du résultat du test
    '''
    assert comu_dans_reseau(amis) == ["Bob", "Alice", "Dan"]  #L'ordre n'a pas d'importance
    print("Tout vas bien !")
    
test_comu_dans_reseau()



def test_comu_dans_amis():
    '''
    fonction qui vérifie le fonctionnement de la fonction comu_dans_amis
    
    renvoie soit une erreur, soit une chaîne de caractère 'Tout vas bien !' en fonction du résultat du test
    '''
    assert comu_dans_amis(amis,"Alice") == ["Alice", "Bob", "Dan"]
    assert comu_dans_amis(amis,"Carl") == ["Carl", "Bob"]
    print("Tout vas bien !")
    
test_comu_dans_amis()



def test_comu_max():
    '''
    fonction qui vérifie le fonctionnement de la fonction comu_max
    
    renvoie soit une erreur, soit une chaîne de caractère 'Tout vas bien !' en fonction du résultat du test
    '''
    assert comu_max(amis) == ["Alice", "Bob", "Dan"]
    print("Tout vas bien !")
    
test_comu_max()

