import pandas as pd
from pytest import raises

df = pd.read_csv('Alhuraibi_Alamoudi_Ahmed_Spotify_Playlist_Dataset.csv')

def test_compute_analysis():
    from compute_analysis import compute_analysis
    result = compute_analysis(df)
    assert (result['Tracks Count'] >= 0).all()
    assert (result['Song Count'] >= 0).all()
    assert (result['Duration (Hrs)'] >= 0).all()
    assert (result['Duration (Min)'] >= 0).all()
    assert (result['Artists Count'] >= 0).all()

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a DataFrame")