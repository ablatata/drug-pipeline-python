# coding: utf-8
"""

Usage:
======
    python compute_drug_links drugs alldatalinks 
    
"""

__authors__ = ("Abla")
__contact__ = ("abla.takkag10@gmail.com")
__copyright__ = "MIT"
__date__ = "2022-12-05"
__version__= "1.0.0"

import os
import pandas as pd
import numpy as np


def compute_drug_links(drugs, datalinks): 
    """Cette fonction permet de calculer les liens entre les differents medicaments et leurs mentions dans les PubMed, 
    les publications scientifiques et les journaux'.
        
        Parameters
        ----------
        
        drugs: pandas.DataFrame
               DataFrame contenant les medicaments avec leurs ids.
        alldatalinks: pandas.DataFrame
                      DataFrame contenant les toutes les donnees des pubmed, publications et journaux.
        Returns
        --------
        links_list : list de dico
                     liste of dictionnaires contenant les drugs et leurs liens comme le schéma suivant :
                    [{"drug_id": drug_id_value, 
                     "links":[{
                                 "link_type": link_type_1, "journal_name" : journal_name_1, 
                                 "date_mention": date_mention_1},  ....],
                                
                    }]
        """
    # Definir une liste vide
    links_list = []
    # Boucler sur index de dataframe drugs
    for ind in drugs.index :
        # Definir un dico links vide 
        links_dico = {}
        # Recuperer l'id et le nom de drug a chaque boucle
        drug_id = drugs['atccode'][ind]
        drug_name = drugs['drug'][ind].lower()
        # Mettre a jour le dico des links avec l'id de drug et les links (vide)
        links_dico.update({"drug_id": drug_id,
                         "links": [] })
        # Boucler sur l'index et la ligne de dataframe des liens
        for i, row in datalinks.iterrows():
            # Si la colonne titre contien le nom de drug 
            if (drug_name in row['title']) : 
                # On append la cle de dictionnaire links 
                value_to_append = {"link_type": row['type'], "journal_name": row["journal"], 
                                   "date_mention":row["date"]}
                links_dico["links"].append(value_to_append)
        links_list.append(links_dico)               
    return links_list         

            
