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
<<<<<<< Updated upstream
<<<<<<< Updated upstream
# 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
=======
# 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
>>>>>>> Stashed changes
=======
# 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
>>>>>>> Stashed changes
