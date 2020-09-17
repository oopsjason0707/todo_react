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



class ScoresBasicSerialzier(Serialzier):
    name = serializers.CharField()
    math = serializers.IntegerField()
    science = serializers.IntegerField()
    english = serializers.IntegerField()



    def create



    def Meta:
        model = Scores
        fields =['name', 'math', 'science', 'english', 'reg_user', '']



    def validate_math(self, value):
        if not(0 < math 100): # 만약에 수학이 100 이상이면 
          raise ValidataionError("0~100 사이면 입력해주세요!") # 이렇게 메세지가 뜨게만드는 기능
        return value 


    def validate_phone_number(self, math):
        re.match("")
        if result == None:  # 전화번호가 아닌 다른 언어를 적었을때
            raise ValidationError('전화번호 형식이 맞지 않습니다.')  # 이렇게 메세지가 뜬다
        return value

        
    

    
