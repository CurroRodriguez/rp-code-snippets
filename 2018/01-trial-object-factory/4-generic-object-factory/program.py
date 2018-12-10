import music

config = {
    'SPOTIFY_CLIENT_KEY': 'THE_SPOTIFY_CLIENT_KEY',
    'SPOTIFY_CLIENT_SECRET': 'THE_SPOTIFY_CLIENT_SECRET',
    'PANDORA_CLIENT_KEY': 'THE_PANDORA_CLIENT_KEY',
    'PANDORA_CLIENT_SECRET': 'THE_PANDORA_CLIENT_SECRET',
    'LOCAL_MUSIC_LOCATION': '/usr/data/music'
}

pandora = music.services.get('PANDORA', **config)
pandora.test_connection()
spotify = music.services.get('SPOTIFY', **config)
spotify.test_connection()
local = music.services.get('LOCAL', **config)
local.test_connection()

pandora2 = music.services.get('PANDORA', **config)
spotify2 = music.services.get('SPOTIFY', **config)

print(id(pandora) == id(pandora2))
print(id(spotify) == id(spotify2))
