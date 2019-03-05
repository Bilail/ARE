#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Comportement:
    
    def init(self, a_max, a_min, temps_reaction, longueur):
        self.a_max = a_max
        self.a_min = a_min
        self.temps_reaction = temps_reaction
        self.longueur = longueur
        
    def calcul_acceleration(self, v_j, v_i, distance, vitesse_limite):
        
        Tau = vitesse_limite / self.a_max

        temps_securite = self.temps_reaction

        distance_securite = temps_securite * v_i + self.longueur
        delta_x = distance_securite - distance
        
        if delta_x < 0:
            vitesse_vehicule = vitesse_limite
        else:  
            vitesse_vehicule = v_j * (1 - delta_x / distance_securite)
            
        if vitesse_vehicule > vitesse_limite: 
            vitesse_vehicule = vitesse_limite
            
        if vitesse_vehicule < 0:
            vitesse_vehicule = 0

        return (vitesse_vehicule - v_i) / Tau
    


# In[ ]:


from Comportement import Comportement

class Voiture(object):
    
    def __init__(self, position, vitesse, delta, temps_total, indice, numero_section):

