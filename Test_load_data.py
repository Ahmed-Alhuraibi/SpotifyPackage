'''Testing load_data_fn file'''

from pytest import raises

def test_preprocess_data_fn():
    from load_data import preprocess_data_fn

    with raises(TypeError):
        preprocess_data_fn('must be dataframe')
       

def test_playlist_URI_fn():
    from load_data import playlist_URI_fn

    input_strings = ['https://open.spotify.com/playlist/5zFVXcNZrCZsRmgtxJfVN9']
    output_strings = ['5zFVXcNZrCZsRmgtxJfVN9']

    result_strings = [playlist_URI_fn(url) for url in input_strings]

    assert result_strings == output_strings


