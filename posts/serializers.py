from rest_framework import serializers
from .models import Post
from .models import Comment

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    tag_list = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at','tags', 'tag_list'] 
    def get_tag_list(self, obj):
        return obj.tag_list()
    
    def create(self, validated_data):
         # Remove the author from validated_data if it exists
        validated_data.pop('author', None)
        # This will create a new Post instance and automatically assign the author (user)
        return Post.objects.create(author=self.context['request'].user, **validated_data)
    
class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_username', 'content', 'created']