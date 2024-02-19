import pandas as pd
import requests

def token_fn(client_id:str, client_secret:str) -> dict:
    ''' Provide access token to capture data via API

    Parameters
    ----------
    client_id : str
        spotify account id

    client_secret : str
        spotify secret key

    Returns
    -------
    Status : int
        Status of the request
    
    headers : dict
        access token that expires frequently and needs to be updated
    '''

    url = 'https://accounts.spotify.com/api/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    try:
        auth_req = requests.post(url, headers=headers, data=data)
        auth_req.raise_for_status()  # Raise an HTTPError for bad status codes
        print("Status Code", auth_req.status_code)
        print("JSON Response ", auth_req.json())
        
        access_token = auth_req.json().get('access_token')
        if access_token:
            headers = {'Authorization': f'Bearer {access_token}'}
        else:
            print("Access token not found in response.")
    except requests.exceptions.RequestException as e:
        print("Error:", e)



def json_to_df_fn( playlist_lists:list) -> pd.DataFrame:
    ''' This function converts json list to data frame. 

    Parameters
    ----------
    playlist_lists : list of API response

    Returns
    -------
    df : keys converted to columns of data frame
    '''
 
    df = pd.DataFrame()
    page_index = 0

    while page_index < len(playlist_lists):
        page = playlist_lists[page_index]
        df = pd.concat([df, pd.json_normalize(page, sep='_')])
        page_index += 1



def playlist_URI_fn(playlist_url: str) -> str:
    ''' This function passes the URL of spotify playlist to parse the playlist URI 
    
    Parameters
    ----------
    playlist_url : my spotify url, 
    sample url : 'https://open.spotify.com/playlist/5zFVXcNZrCZsRmgtxJfVN9'

    Returns
    -------
    playlist_uri : my playlist URI
    Sample URI: 5zFVXcNZrCZsRmgtxJfVN9
    '''
    playlist_URI = playlist_url.split('/')[-1]
    return playlist_URI



def track_ids_list_fn(playlist_URI : str, headers : dict) -> list:
    ''' Provides track ids from the playlist

    This function lists track ids from my spotify playlist 
   

    Parameters
    ----------
    playlist_URI : URI of playlist
    headers : access token

    Returns
    -------
    track_ids : a list of all my playlist track ids
    '''
    playlist_endpoint = f'https://api.spotify.com/v1/playlists/{playlist_URI}/tracks'
    offset = 0
    playlist_lists = []

    while True:
        api_response = requests.get(playlist_endpoint + f'?offset={offset}', headers=headers)
        
        playlist_total = api_response.json()['total']
        
        playlist_lists.append(api_response.json()['items'])

        offset += 100
        
        if offset > playlist_total:
            break

    # track no.1 
    print(playlist_lists[0][0])



def track_data_list_fn(track_ids:list, headers:dict) -> pd.DataFrame:
    '''
    This function iterats over a list of track ids and fetsh not more than 50 records each time till
    meet the total number of data frame records

    Parameters
    ----------
    track_ids : one track id retrived from the list 
    headers : access token

    Returns
    -------
    track_ids : playlist track ids separated by comma
    sample output: 3OohydwTMW65eZKOrX5MPY,2rn3iavjpkKfwxSeL7PwJC,..
    '''
        
    start = 0
    end = len(track_ids)
    step = 50  

    api_track_info = []
    api_track_feature_info = []

    i = start
    while i < end:
        x = i
        id_var = ','.join(track_ids[x:x + step])

        api_track_endpoint = f'https://api.spotify.com/v1/tracks?ids={id_var}'
        api_response_track = requests.get(api_track_endpoint, headers=headers)
        api_track_info.append(api_response_track.json())

        api_track_features_endpoint = f'https://api.spotify.com/v1/audio-features?ids={id_var}'
        api_response_feature = requests.get(api_track_features_endpoint, headers=headers)
        api_track_feature_info.append(api_response_feature.json())

        # assert isinstance(df, pd.DataFrame)
        print(id_var)
        
        i += step


def preprocess_data_fn(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function preprocesses dataframe obtained from an API, extracting the artist name 
    and performing key mapping. 

    Parameters
    ----------
    df : pd.DataFrame
        

    Returns
    ----------
    pd.DataFrame
        Processed df
    '''

    # Fixing the artist column
    df['artists'] = df['artists'].str.extract(r"name':'([^']+)", expand=False)

    # Mapping keys column to actual keys
    music_dict = {0: 'C', 1: 'C', 2: 'D', 3: 'D#', 4: 'E', 5: 'F', 6: 'F#', 7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'}
    df['key'] = df['key'].map(music_dict)

    return df



def data_load_fn(config:dict):
    ''' Get dataset from spotify API

    This function takes the neccessory input and return the selected data frame

    Parameters
    ----------
    config : keys added in the config file


    Returns
    -------
    The processed data frame

    '''

    client_id = config['client_id']
    client_secret = config['client_secret']
    playlist_url = config ['playlist_url']
    headers = token_fn(client_id, client_secret)
    playlist_uri = playlist_URI_fn(playlist_url)
    track_ids = track_ids_list_fn(playlist_uri, headers)
    df_raw = track_data_list_fn(track_ids,headers)
    df = preprocess_data_fn(df_raw)
    
    return df