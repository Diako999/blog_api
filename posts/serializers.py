from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at'] 

    
    def create(self, validated_data):
         # Remove the author from validated_data if it exists
        validated_data.pop('author', None)
        # This will create a new Post instance and automatically assign the author (user)
        return Post.objects.create(author=self.context['request'].user, **validated_data)