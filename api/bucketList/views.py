from rest_framework.decorators import api_view
from .models import Languages, FavoriteLanguage, LanguageGroup, FavoriteLanguageGroup
from .serializers import LanguagesSerializer, LanguageGroupSerializer, FavoriteLanguageGroupSerializer, FavoriteLanguageSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets

# Create your views here.


# @api_view(['GET'])
# def LanguagesView(request):
#     qs = Languages.objects.filter()
#     serializer = LanguagesSerializer(qs, many=True)
#     return Response(serializer.data)

# def get_queryset(self):
#     qs = super().get_queryset()

#     name = self.request.query_params.get('name')
    
#     if name:
#         qs = qs.filter(name=name)
#     return qs
    

class FavoriteLanguageGroupViewSet(viewsets.ModelViewSet):
    queryset = FavoriteLanguageGroup.objects.all()
    serializer_class = FavoriteLanguageGroupSerializer

class LanguageGroupViewSet(viewsets.ModelViewSet):
    queryset = LanguageGroup.objects.all()
    serializer_class = LanguageGroupSerializer

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Languages.objects.all()
    serializer_class = LanguagesSerializer

class FavoriteLanguageViewSet(viewsets.ModelViewSet):
    queryset = FavoriteLanguage.objects.all()
    serializer_class = FavoriteLanguageSerializer




