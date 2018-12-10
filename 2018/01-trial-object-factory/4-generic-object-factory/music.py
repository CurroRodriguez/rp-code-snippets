import object_factory

class SpotifyService:

    def __init__(self, access_code):
        self._access_code = access_code

    def test_connection(self):
        print('Accessing Spotify with {ac}'.format(ac=self._access_code))

class SpotifyServiceBuilder:
    
    def __init__(self):
        self._instance = None

    def __call__(self, **kwargs):
        if not self._instance:
            client_key = kwargs.get('SPOTIFY_CLIENT_KEY')
            client_secret = kwargs.get('SPOTIFY_CLIENT_SECRET')
            access_code = self.authorize(client_key, client_secret)
            self._instance = SpotifyService(access_code)
        return self._instance

    def authorize(self, key, secret):
        return 'SPOTIFY_ACCESS_CODE'


class PandoraService:

    def __init__(self, consumer_key, consumer_secret):
        self._key = consumer_key
        self._secret = consumer_secret


    def test_connection(self):
        print('Accessing Pandora with key {k} and secret {s}'.format(k=self._key, s=self._secret))


class PandoraServiceBuilder:

    def __init__(self):
        self._instance = None

    def __call__(self, **kwargs):
        if not self._instance:
            client_key = kwargs.get('PANDORA_CLIENT_KEY')
            client_secret = kwargs.get('PANDORA_CLIENT_SECRET')
            consumer_key, consumer_secret = self.authorize(client_key, client_secret)
            self._instance = PandoraService(consumer_key, consumer_secret)
        return self._instance

    def authorize(self, key, secret):
        return 'PANDORA_CONSUMER_KEY', 'PANDORA_CONSUMER_SECRET'

class LocalService:

    def __init__(self, location):
        self._location = location

    def test_connection(self):
        print('Accessing Local music at {l}'.format(l=self._location))


def create_local_music_service(**kwargs):
    location = kwargs.get('LOCAL_MUSIC_LOCATION')
    return LocalService(location)


class MusicServiceProvider(object_factory.ObjectFactory):

    def get(self, service_id, **kwargs):
        return self.create(service_id, **kwargs)

services = MusicServiceProvider()
services.register_builder('SPOTIFY', SpotifyServiceBuilder())
services.register_builder('PANDORA', PandoraServiceBuilder())
services.register_builder('LOCAL', create_local_music_service)
