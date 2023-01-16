# coding: utf-8
"""

Usage:
======
    python LinksGraph.py 
    
"""

__authors__ = ("Abla")
__contact__ = ("abla.takkag10@gmail.com")
__copyright__ = "MIT"
__date__ = "2022-12-05"
__version__= "1.0.0"

import os
import pandas as pd
import json
import numpy as np
import logging, warnings
R = os.path.abspath('../..')
if R not in os.sys.path:
    S = os.sys.path.insert(0,R)
    

from drugs_link_graph.connectors.connector_local import ConnectorLocal
from drugs_link_graph.loaders.loader_local import LoaderLocal
from drugs_link_graph.data_cleaning.cleaner import Cleaner
from drugs_link_graph.tools.utils import reader, concat_data
from drugs_link_graph.data_modeling.links_graph_modeler import compute_drug_links
from drugs_link_graph.config.config import load_conf_file, configure_logging
import drugs_link_graph.tools.constants as cst

warnings.filterwarnings("ignore")
logger = logging.getLogger(__name__)

    
class LinksGraphPipeline():
    """cette classe permet de construire le pipeline pour calculer les liens entre les drugs d'un côté et leurs 
      mentions dans les PubMed, les journaux et clinical_trials
      
       Parameters
       ----------
        conf_path: str
                   chemin d'accès vers le fichier de config.
        conf_name: str
                   nom de fichier de config.
       
    """
    
    def __init__(self, conf_path, conf_name):
        self.conf_path = conf_path
        self.conf_name = conf_name 
        return
        


    def compute(self, ) : 
        
        logger.info("=========> Getting input data...")
        
        #Lire la config
        conf = load_conf_file(self.conf_path, self.conf_name)
        
        # Lire le dataframe des drugs
        connector = ConnectorLocal(conf['input_path'])
        drugs_input_name = conf['drugs']
        drugs = reader(drugs_input_name["file_name"], drugs_input_name["format"], drugs_input_name["delimiteur"], connector)   
        
        # Lire et concatener les donnees de liens (pubmed & clinicals trials)
        datalinks = concat_data(conf, connector) 
        
        logger.info("=========> preprocessing & cleaning data...")
        # Nettoyer les données de liens
        clean = Cleaner(datalinks)
        # Nettoyer et uniformiser la colonne date 
        cleaned_date = clean.clean_date_column('date')
        # Nettoyer la colonne title
        cleaned_title = clean.clean_words_column('title')
        # Nettoyer la colonne journal 
        cleaned_journal = clean.clean_words_column('journal')
        # Supprimer les nulls
        cleaned_datalinks = clean.deal_with_nan()
        
        logger.info("=========> links graph modeler...")
        # Calculer les liens entre les drugs et les donnees
        links = compute_drug_links(drugs, cleaned_datalinks)
        
        logger.info("=========> save result ...")
        # Enregitrer les resultats 
        loader = LoaderLocal(conf['links_path'])
        loader.write_json_file(links, conf['links_name'])
        
        return True
