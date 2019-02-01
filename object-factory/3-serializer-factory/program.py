import serializers
import songs
import yaml_serializer

song = songs.Song('1', 'Sultans of Swing', 'Dire Straits')
serializer = serializers.ObjectSerializer()
print(serializer.serialize(song, 'JSON'))
print(serializer.serialize(song, 'XML'))
print(serializer.serialize(song, 'YAML'))