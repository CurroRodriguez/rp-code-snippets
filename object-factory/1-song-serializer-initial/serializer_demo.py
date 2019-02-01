import json
import xml.etree.ElementTree as et

class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist



class SongSerializer:

    def serialize(self, song, format):
        if format == 'JSON':
            payload = {
                'id': song.song_id,
                'title': song.title,
                'artist': song.artist
            }
            return json.dumps(payload)
        elif format == 'XML':
            song_element = et.Element('song', attrib={'id': song.song_id})
            title = et.SubElement(song_element, 'title')
            title.text = song.title
            artist = et.SubElement(song_element, 'artist')
            artist.text = song.artist
            return et.tostring(song_element, encoding='unicode')
        else:
            raise ValueError(format)
            


if __name__=='__main__':
    song = Song('1', 'Sultans of Swing', 'Dire Straits')
    serializer = SongSerializer()
    serialized = serializer.serialize(song, 'JSON')
    print(serialized)
    serialized = serializer.serialize(song, 'XML')
    print(serialized)
    serializer.serialize(song, 'OTHER')
