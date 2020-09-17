from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    # User 테이블 조인걸때
    memo = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=13, null=True)   # 추가할때마다 cmd 창에서 pyton manage.py makemigrations 그리고 migrate 해줘야한다.    
    reg_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

                                       


class Scores(models.Model):
    subject = models.CharField(max_length=10)
    math = models.IntegerField()
    english = models.IntegerField()
    science = models. IntegerField()
    reg_date = models.DateField(auto_now_add=True)
    reg_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
