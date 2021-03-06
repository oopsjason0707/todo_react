from django.contrib import admin
from .models import Languages, LanguageGroup, FavoriteLanguage, FavoriteLanguageGroup

# Register your models here.

@admin.register(Languages)  #이걸 만들면 admin 페이지에 User가 생김. (account밑에 User라는 새로운 칸이 만들어짐)
class LanguagessAdmin(admin.ModelAdmin):
    pass
     #관리자 페이지에서 students섹션에 데이터를 추가한뒤 이름, 주소, 이메일까지 보이게 나오려면 이거 넣어줘야함.
   
@admin.register(LanguageGroup)
class LanguageGroupAdmin(admin.ModelAdmin):
    pass
    

@admin.register(FavoriteLanguage)  
class FavoriteLanguageAdmin(admin.ModelAdmin):
    pass
    

@admin.register(FavoriteLanguageGroup)
class FavoriteLanguageGroupAdmin(admin.ModelAdmin):
    pass
    