from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    poster_path = serializers.CharField(max_length=50)
    overview = serializers.CharField()
    release_date = serializers.DateField()
    original_title = serializers.CharField(max_length=50)
    original_language = serializers.CharField(max_length=2)
    backdrop_path = serializers.CharField(max_length=50)
    popularity = serializers.FloatField()
    vote_count = serializers.IntegerField()
    vote_average = serializers.FloatField()
    adult = serializers.BooleanField()

class Show(object):
    def __init__(self, **kwargs) -> None:
        for field in ('id', 'name', 'poster_path', 'overview'):
            setattr(self, field, kwargs.get(field, None))
            
shows = {
1: Show(id=1, name='Demo', owner='xordoquy', status='Done'),
2: Show(id=2, name='Model less demo', owner='xordoquy', status='Ongoing'),
3: Show(id=3, name='Sleep more', owner='xordoquy', status='New'),
}
class ShowSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    poster_path = serializers.CharField(max_length=50)
    overview = serializers.CharField()
    original_name = serializers.CharField(max_length=50)
    original_language = serializers.CharField(max_length=2)
    backdrop_path = serializers.CharField(max_length=50)
    popularity = serializers.FloatField()
    vote_count = serializers.IntegerField()
    vote_average = serializers.FloatField()

    def create(self, validated_data):
        return Show(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance