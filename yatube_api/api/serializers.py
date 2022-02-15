from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from posts.models import Post, Comment, Group, Follow, User
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
        read_only = ['post']


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(queryset=User.objects.all(),
                                             slug_field='username')
    user = serializers.SlugRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
        slug_field='username'
    )

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [UniqueTogetherValidator(queryset=Follow.objects.all(),
                      fields=['user', 'following'])]

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!')
        return data
