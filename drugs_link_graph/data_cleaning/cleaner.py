# coding: utf-8
"""

Usage:
======
    python cleaner.py 
    
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
import numpy as np 

logger = logging.getLogger(__name__)


class Cleaner():
    
    """cette classe permet de lire ou écrire un fichier csv ou json en local
    """

    def __init__(self, df):
        self.df = df
        return
    
    def clean_date_column(self, column_name):
        
        """Cette fonction permet d'uniformiser le format de la colonne date pour avoir un seul format '%d-%m-%Y'.
        
        Parameters
        ----------
        
        df:   pandas.DataFrame
              DataFrame.
        column_name: str
                     nom de la colonne date.
        Returns
        --------
        df: pandas.DataFrame
            dataframe avec la colonne date
        """
        df = self.df
        # Convertir la colonne en datetime
        df[column_name]=pd.to_datetime(df[column_name])
        # Uniformiser le format des dates DD-MM-YYYY
        df[column_name] = df[column_name].apply(lambda x: x.strftime('%d-%m-%Y'))
        
        return df
    
    def clean_words_column(self, column_name):
        
        """Cette fonction permet d'enlever des espaces et des caractères de la colonne text.
        
        Parameters
        ----------
        df:   pandas.DataFrame
              DataFrame.
        column_name: str
                     nom de la colonne date.
                     
        Returns
        --------
        df: pandas.DataFrame
            dataframe 
        
        """
        df = self.df
        # Remplacer des cacactères non ascii 
        df[column_name]= df[column_name].str.replace(r'\\x[0-9A-Fa-f]{2}','', regex=True).values
        # Enlever les espaces et les vides 
        df[column_name] = df[column_name].str.replace('  ',' ', ).values
        # Rendre miniscule les strings
        df[column_name] = df[column_name].str.lower()
        return df
    
    
    def deal_with_nan(self, ) : 
                
        """Cette fonction permet d'enlever des espaces et des caractères de dataframe.
        
        Parameters
        ----------
        df:   pandas.DataFrame
              DataFrame.
                     
        Returns
        --------
        df: pandas.DataFrame
            dataframe 
        
        """
        df = self.df
        df = df.replace(r'^\s*$', np.nan, regex=True)
        df = df.dropna()
        return df
