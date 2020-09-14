from rest_framework.serializers import ModelSerializer
from .models import Students 
from .models import Scores

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Students
        fields = ['name', 'address', 'email']


class ScoreSerializer(ModelSerializer):
    class Meta:
        model = Scores
        fields = ['subject', 'math', 'english', 'science']