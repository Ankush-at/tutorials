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


<<<<<<< HEAD
# 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
=======

# git token
# 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
>>>>>>> 4c44bcf1c004599d97e2df873f1d06fca43d9840
