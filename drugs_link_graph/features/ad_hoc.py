# coding: utf-8
"""

Usage:
======
    python count_max_journal  
    
"""

__authors__ = ("Abla")
__contact__ = ("abla.takkag10@gmail.com")
__copyright__ = "MIT"
__date__ = "2022-12-05"
__version__= "1.0.0"

import os
R = os.path.abspath('../..')
if R not in os.sys.path:
    S = os.sys.path.insert(0,R)
    
import logging, warnings    
import pandas as pd
import numpy as np
from datetime import datetime
from drugs_link_graph.config.config import load_conf_file, configure_logging
from drugs_link_graph.connectors.connector_local import ConnectorLocal
from drugs_link_graph.loaders.loader_local import LoaderLocal
import drugs_link_graph.tools.constants as cst

warnings.filterwarnings("ignore")
logger = logging.getLogger(__name__)

def journal_max_links(conf_path, conf_name): 
    """Cette fonction permet de calculer le nom du journal (ou les noms des journaux) 
    qui mentionne le plus de medicaments différents.
        
        Parameters
        ----------
        
        conf_path : str
                    chemin d'accès vers le fichier de configuration
               
        Returns
        --------
        dico_max_count : dict
                         dictionnaire avec nom du journal qui mentionne le plus de medicaments différents 
                    
        """

    conf = load_conf_file(conf_path, conf_name)
    connector = ConnectorLocal(conf['links_path'])
    
    logger.info("=========> Getting links data...")
    links = connector.read_json_file(conf["links_name"])
    df=pd.DataFrame(links)
    
    logger.info("=========> Count max Drugs in journal...")
    # Definir la colonne drug_id comme index, exploser la colonne links en plusieurs lignes
    # Puis réinitialisez l'index après.
    data_exploded_rows = df.set_index('drug_id').apply(lambda x: x.apply(pd.Series).stack()).reset_index().drop('level_1', 1)
    
    # Exploser la colonne links en 3 colonnes : link_type, journal_name & date_mention
    data_exploded_col = data_exploded_rows.join(pd.json_normalize(data_exploded_rows.pop("links")))
    
    # Calculer le nombre de medicaments differents mentionnes dans chaque article
    df_drugs_count= data_exploded_col.groupby("journal_name", as_index=False) ['drug_id'].nunique()
    
    # Calculer l'article ou les articles qui ont le plus de médicaments différents 
    result_max_count= df_drugs_count[df_drugs_count['drug_id'] == df_drugs_count['drug_id'].max()]
    
    # Ajouter la date de jour de count et convertir le resultat en dictionnaire
    current_date_count = datetime.now().strftime('%Y-%m-%d')
    result_max_count["date_of_count"]= current_date_count
    dico_max_count= result_max_count.to_dict('records')
    
    logger.info("=========> save result ...")
    # Enregitrer les résultat
    loader = LoaderLocal(conf['features_path'])
    loader.write_json_file(dico_max_count, conf['features_name'])

    return dico_max_count        
