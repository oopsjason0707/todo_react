from rest_framework.serializers import ModelSerializer
from .models import Languages, LanguageGroup, FavoriteLanguage, FavoriteLanguageGroup




class LanguagesSerializer(ModelSerializer):
    class Meta:
        model = Languages
        fields ='__all__'

class LanguageGroupSerializer(ModelSerializer):
    class Meta:
        model = LanguageGroup
        fields = '__all__' 

class FavoriteLanguageSerializer(ModelSerializer):
    class Meta:
        model = FavoriteLanguage
        fields = '__all__'

class FavoriteLanguageGroupSerializer(ModelSerializer):
    class Meta:
        model = FavoriteLanguageGroup
        fields = '__all__'
