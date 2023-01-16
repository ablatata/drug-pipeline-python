# coding: utf-8
"""

Usage:
======
    python connector_local.py path

    path: hemin vers le fichier à écire
    
"""

__authors__ = ("Abla")
__contact__ = ("abla.takkag10@gmail.com")
__copyright__ = "MIT"
__date__ = "2022-12-05"
__version__= "1.0.0"

import os
import pandas as pd
import json
import logging

logger = logging.getLogger(__name__)

class LoaderLocal():
    
    """cette classe permet de lire ou écrire un fichier csv ou json en local
    """

    def __init__(self, path):
        self.path = path
        return
    
    def write_csv_file(self, data, file_name, delimiteur= ','):
        
        """Cette fonction permet d'écrire un pandas.DataFrame en .csv sur HDFS.
        
        Parameters
        ----------
        
        Data: pandas.DataFrame
              DataFrame.
        file_name: str
                   chemin du fichier.
                   
        """

        file_path = os.path.join(self.path, file_name)
        
        try : 
            # Enregistrer les donnees dans un fichier csv
            f = open (file_path, "w", encoding = 'utf_8')
            data.to_csv(f, sep = delimiteur)
            f.close ()
            return True
        
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            return True
    
    def write_json_file(self, data, file_name):
        
        """Cette fonction permet d'écrire en .json sur HDFS.
        
        Parameters
        ----------
        data: str, dict, list...
              objet python hors fonction ou classe comme pandas.DataFrame
              
        file_name: str
                   nom du fichier.
                   
        """
        file_path = os.path.join(self.path, file_name)
        try : 
            # Enregistrer les donnees dans un fichier json
            f = open (file_path, "w", encoding = 'utf_8')
            f.write( json.dumps(data),)
            f.close ()
            return True
        
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            return True
    

    
    def close(self):
        return
