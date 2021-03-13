from rest_framework import serializers

class URLSerializer(serializers.Serializer):
    id = Serializer.IntegerField(read_only=True)
    long_url = serializers.CharField(required=True, allow_blank=False, max_length=100)
    short_url = serializers.CharField(required=True, allow_blank=False, max_length=7)
    
