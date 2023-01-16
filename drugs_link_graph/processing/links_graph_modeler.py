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
                     "drug_name": drug_name_value,
                     "links":{
                                 "clinical_trials" : [(journal_name_1, date_mention_1),  ....],
                                "pubmed" : [(journal_name_1, date_mention_1),  ....]
                    }}]
        """
    links_list = []
    for ind in drugs.index :
        links_dico = {}
        drug_id = drugs['atccode'][ind]
        drug_name = drugs['drug'][ind].lower()
        links_dico.update({"drug_id": drug_id,
                         "links": [] })
        for i, row in datalinks.iterrows():
            if (drug_name in row['title']) : 
                value_to_append = {"link_type": row['type'], "journal_name": row["journal"], "date_mention":row["date"]}
                links_dico["links"].append(value_to_append)
        links_list.append(links_dico)               
    return links_list         

            
