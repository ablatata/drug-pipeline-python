# coding: utf-8
import os

R = os.path.abspath('../..')
if R not in os.sys.path:
    S = os.sys.path.insert(0,R)
    
from drugs_link_graph.connectors.connector_local import ConnectorLocal
import drugs_link_graph.tools.constants as cst
import pandas as pd
import json
import logging.config

logger = logging.getLogger()

def load_conf_file(conf_path, conf_name):
    """
    Cette fonction permet de charger le fichier de configuration json
     
        Parameters
        ----------
        
        conf_path: str
                   chemin d'accès au fichier de configuration.
        log_conf_name: str
                       nom de fichier de configuration.
                       
    """
    
    file_path = os.path.join(conf_path, conf_name)
    if os.path.exists(file_path):
        reader = ConnectorLocal(conf_path)
        file_content = reader.read_json_file(conf_name)
        logger.info(
            "configuration file ('{}') successfully loaded".format(file_path))
    else:
        raise Exception("Could not load the configuration file '{}'".format(file_path))
    return file_content


def configure_logging(conf_path, log_conf_name):
    """
    Cette fonction permet de Configurer les logs (si le fichier ne peut pas être chargé ou lu,
     une configuration de base sera utilisée à la place)
     
        
        Parameters
        ----------
        
        conf_path: str
                   chemin d'accès au fichier de configuration des logs.
        log_conf_name: str
                       nom de fichier de configuration des logs.
               
    
    """
    log_config_file = os.path.join(conf_path, log_conf_name)
    
    if os.path.exists(log_config_file):
        reader = ConnectorLocal(conf_path)
        config = reader.read_json_file(log_conf_name)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)


        
        
    
    
