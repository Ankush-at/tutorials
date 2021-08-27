from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES,STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']



# git token 
# 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        
# >>>>>>> a49fe038171edae5a202d26b58b75523759f6e1b
