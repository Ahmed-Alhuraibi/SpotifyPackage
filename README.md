# SpotifyPackage
This package utilizes the Spotify API to perform various tasks such as searching for tracks, albums, artists, creating playlists, and more. It's a Python application that allows users to interact with Spotify's vast music database programmatically.

## Prerequisties
* Python 3.x
* Spotify Developer Account (for obtaining API credentials)
* Requests library (install via pip install requests)

## Getting Started
* Obtain your Spotify API credentials by creating a Spotify Developer Account and registering your application.
* Copy your Client ID and Client Secret obtained from the Spotify Developer Dashboard.

## Installation
* Use the following python lines to execute this package from COLAB
``` python
!pip install git+https://github.com/user/yourteamrepo
from yourteamrepo import Analysis

analysis_obj = Analysis('config.yml')
analysis_obj.load_data()

analysis_output = analysis_obj.compute_analysis()
print(analysis_output)

analysis_figure = analysis_obj.plot_data()
``` 
