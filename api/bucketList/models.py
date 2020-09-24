from django.db import models

# Create your models here.
class LanguageGroup(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    reg_date = models.DateField(auto_now_add=True)
    del_yn = models.BooleanField(default=False)

class FavoriteLanguageGroup(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    reg_date = models.DateField(auto_now_add=True)

class Languages(models.Model): 
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    reg_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(blank=True)
    del_yn = models.BooleanField(default=False)
    group = models.ForeignKey(LanguageGroup, on_delete=models.CASCADE)

class FavoriteLanguage(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    memo = models.TextField()
    reg_date = models.DateField(auto_now_add=True)
    group = models.ForeignKey(FavoriteLanguageGroup, on_delete=models.CASCADE)


