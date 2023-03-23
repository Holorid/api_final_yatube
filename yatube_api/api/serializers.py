from rest_framework.serializers import ModelSerializer, SlugRelatedField
from rest_framework.serializers import UniqueTogetherValidator, ValidationError
from rest_framework.serializers import CurrentUserDefault
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('__all__')
        model = Post


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('__all__')
        model = Comment
        read_only_fields = ('author', 'id', 'post')


class GroupSerializer(ModelSerializer):

    class Meta:
        fields = ('__all__')
        model = Group


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=CurrentUserDefault()
    )
    following = SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    class Meta:
        fields = ('__all__')
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following'],
                message='Вы уже подписаны на этого автора'
            )
        ]

    def validate_following(self, following):
        if self.context['request'].user == following:
            raise ValidationError(
                'На себя подписаться нельзя'
            )
        return following
