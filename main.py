# coding: utf-8
import warnings
import logging
from drugs_link_graph.data_pipeline.links_graph_pipeline import LinksGraphPipeline
from drugs_link_graph.config.config import configure_logging
import drugs_link_graph.tools.constants as cst
import time

warnings.filterwarnings("ignore")
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    program_starting_time = time.time()
    logger = logging.getLogger()
    configure_logging(cst.CONF_PATH, cst.LOGGING_CONF_FILE)
    logger.info("The process starts at {}".format(time.strftime(" %Hh%Mmin, %d-%m-%Y", time.gmtime())))
    starting_time = time.time()
    LinksGraphPipeline(cst.CONF_PATH, cst.CONF_NAME).compute()
    logger.info("The process ends at {} \n".format(time.strftime(" %Hh%Mmin, %d-%m-%Y", time.gmtime())))
