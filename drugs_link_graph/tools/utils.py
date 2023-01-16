# coding: utf-8
"""

Usage:
======
    python utils.py 
    
"""

__authors__ = ("Abla")
__contact__ = ("abla.takkag10@gmail.com")
__copyright__ = "MIT"
__date__ = "2022-12-05"
__version__= "1.0.0"



import pandas as pd
import json
import logging


logger = logging.getLogger(__name__)

def reader(file_name, format_name, delimiteur, connector):  
    
    """Cette fonction permet de lire un les données sous deux formats csv ou json
        
    Parameters
    ----------

    file_name: str
               nom du fichier.
    format_name: str
                 nom de format csv ou json
    delimiteur: str
         séparateur des colonnes.
    connector: Object
               connector pour lire les donnees
    Returns
    -------  
    data : pandas.DataFrame
             dataframe contenant les données récupérées du fichier csv ou json

    """

    # Si l'input est un fichier csv
    if (format_name == "csv"):
        data_csv = connector.read_csv_file(file_name, delimiteur)
        return  data_csv
    if format_name == "json":
        data_json = pd.DataFrame(connector.read_json_file(file_name))
        return data_json 
    else : 
        print("format not found: %s" % str(format_name))
        return 
               

def concat_data(dico_links_conf, connector): 
    
    """Cette fonction permet de lire un les données sous deux formats csv ou json
        
    Parameters
    ----------

    dico_links_conf: str
                     dictionnaire contenant la conf des donnees links.

    connector: Object
               connector pour lire les donnees
    Returns
    -------  
    data_links: pandas.DataFrame
                dataframe contenant les données de liens

    """
    # Definir un dataframe vide
    datalinks= pd.DataFrame()
    # Recuprer la conf de des donnees de liens
    data_mention = dico_links_conf['data_mention'] 
    # Boucler sur les noms des inputs 
    for input_name in data_mention : 
        # Boucler sur la conf de l'input
        for data in data_mention[input_name]: 
            # lire l'input de liens
            df = reader(data["file_name"], data["format"], data["delimiteur"], connector)   
            # Renomer le nom de la colonne scientific_title a title dans le dataframe de clinicals trials
            if input_name == "clinical_trials" : 
                df.columns = df.columns.str.replace('scientific_', '')
            # Ajouter un colonne qui prend le nom de la donnee (scientific_trials, pubmed)    
            df['type'] = input_name  
            # Concat les donnees de liens avec le dataframe
            datalinks= pd.concat([df, datalinks] , ignore_index=True)

    return datalinks      
