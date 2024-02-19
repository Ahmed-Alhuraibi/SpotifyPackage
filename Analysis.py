from SpotifyPackage import load_data
from SpotifyPackage import compute_analysis

# from . import load_data
# from . import compute_analysis
from typing import Optional
import matplotlib.pyplot as plt
import yaml
import requests
import pandas as pd
import logging
import matplotlib.pyplot as plt
import sys
import os

# sys.path.append(r'C:\Users\a.alhuraibi\Documents\Huraibi\ds\UofT-DSI\Week#5\Assignments\Homeworks')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
               
logging.basicConfig(
    handlers=(logging.StreamHandler(), logging.FileHandler('logs.log')),
    level=logging.INFO,
)


class Analysis:
    def __init__(self, analysis_config: str) -> None:

        CONFIG_PATHS = ['system_config.yml', 'user_config.yml']

        # add the analysis config to the list of paths to load
        paths = CONFIG_PATHS + [analysis_config]

        # initialize empty dictionary to hold the configuration
        config = {}

        # load each config file and update the config dictionary
        for path in paths:
            with open(path, 'r') as f:
                this_config = yaml.safe_load(f)
            config.update(this_config)
        self.config = config

    def load_data(self) -> pd.DataFrame:
        self.data = load_data.load_data(self.config)
        return self.data
        

    def compute_analysis(self) -> pd.DataFrame:
        output = compute_analysis.compute_analysis(self.data)
        return output


    def notify_done(self, body='Analysis done for my Spotify Playlist') -> None:
        ''' Message the user about the analysis status

        This message will be sent through ntfy.sh API.

 
        Parameters
        ----------
        message : str
            The message body and topic

        Returns
        -------
        None

        '''
        
        requests.post(f"https://ntfy.sh/{self.config['msg_topic']}", 
            data=body.encode(encoding='utf-8'))
        



