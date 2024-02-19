# myspotify Package
This package utilizes the Spotify API to perform various tasks such as searching for tracks, albums, artists, creating playlists, and more. It's a Python application that allows users to interact with Spotify's vast music database programmatically.

##Prerequisties
Python 3.x
Spotify Developer Account (for obtaining API credentials)
Requests library (install via pip install requests)

##Installation
!pip install git+https://github.com/user/yourteamrepo
from yourteamrepo import Analysis

analysis_obj = Analysis('config.yml')
analysis_obj.load_data()

analysis_output = analysis_obj.compute_analysis()
print(analysis_output)

analysis_figure = analysis_obj.plot_data()
