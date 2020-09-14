from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Students
from .serializers import StudentSerializer
from rest_framework.response import Response
from .serializers import ScoreSerializer
from .models import Scores

# Create your views here.

@api_view(['GET'])
def StudentView(request):  #student모델을 가져와서 
    qs = Students.objects.all()  #student studentmodel을 읽었고
    serializer = StudentSerializer(qs, many=True)  #(위에 objects.get이면 밑에 null=False)
    return Response(serializer.data)   #view 까지 만들면 urls.py를 만든다


@api_view(['GET'])
def ScoreView(request): #Score 모델을 가져와서
    qs = Scores.objects.all() #Scoremodel을 읽고
    serializer = ScoreSerializer(qs, many=True)
    return Response(serializer.data) #view 까지 만들어서 urls.py를 만든다.