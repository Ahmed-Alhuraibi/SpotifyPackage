import pandas as pd 
import logging

def compute_analysis(df):
    '''
    This function created to analyze my spotify playlist dataset fetshed using API

    Parameters
    ----------
    df : loaded data frame


    Returns:
    --------
    print the followings:
        1- Artists Count
        2- Song Count
        3- Tracks Count
        4- Duration (Min)
        5- Duration (Hrs)
 
    
    '''

    try :
        num_tracks = df.shape[0]
        print(num_tracks)
        artist_count = len(df['artists'].unique())
        song_count = len(df['name'].unique())
        duration_in_Hr = round(df['duration_ms_x'].sum()/3600000)
        duration_in_Mi = round(df['duration_ms_x'].sum()/60000)
        analysis_dictionary = {'Artists Count':artist_count,'Song Count':song_count,'Tracks Count': num_tracks, 'Duration (Hrs)': duration_in_Hr,'Duration (Min)': duration_in_Mi}
        df_analysis = pd.DataFrame(analysis_dictionary, index=[''])
        return df_analysis

    except  Exception as x:
        x.add_note('No data Frame found')
        logging.error('data loading error')
