# coding: utf-8
"""

Usage:
======
    python loader_local.py path

    path: chemin vers le fichier à lire
    
"""

__authors__ = ("Abla TAKKA")
__contact__ = ("abla.takkag10@gmail.com")
__copyright__ = "MIT"
__date__ = "2022-12-05"
__version__= "1.0.0"

import os
import pandas as pd
import json

R = os.path.abspath('../..')
if R not in os.sys.path:
    S = os.sys.path.insert(0,R)



class ConnectorLocal():
    """cette classe permet de lire ou écrire un fichier csv ou json en local
    """

    def __init__(self, path):
        self.path = path
        return
    
    def read_csv_file(self, file_name, sep = '|'):
        """Cette fonction permet de lire un pandas.DataFrame.
        
        Parameters
        ----------
        
        file_name: str
                   nom du fichier.
        sep: str
             séparateur des colonnes (par défaut = '|').
        Returns
        -------  
        df_open: pandas.DataFrame
                 dataframe contenant les données récupérées du fichier csv
        
        """
        # Path de fichier = path + nom de fichier
        file_path = os.path.join(self.path, file_name)
        # Lire un fichier csv
        try:
            with open(file_path, "rb") as reader:
                df_open = pd.read_csv(reader, sep = sep)
                return df_open
        except BaseException as e:
            print("Error on_file %s: %s" % (str(file_path), str(e)))
            
            
        
    
    def read_json_file(self, file_name):
        """Cette fonction permet de lire un fichier .json en local.
        
        Parameters
        ----------
        
        file_name: str
                   chemin du fichier.
        df_open: pandas.DataFrame
                 dataframe contenant les données récupérées du fichier csv. 
        Returns
        -------  
        df_open: dict
                 dictionnaire contenant les données récupérées du fichier csv                 

        """
        # Path de fichier = path + nom de fichier
        file_path = os.path.join(self.path, file_name)
        
        # Lire un fichier json
        try:
            with open(file_path, encoding='utf-8', errors='ignore') as reader:
                json_output = json.load(reader, strict=False)
                return json_output
        except BaseException as e:
            print("Error on_file %s: %s" % (str(file_path), str(e)))
        
            
        
    
    def close(self):
        return
