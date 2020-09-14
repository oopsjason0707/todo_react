from django.contrib import admin
from .models import User  #models.py에 모델은 임포트한거임

# Register your models here.
@admin.register(User)  #이걸 만들면 admin 페이지에 User가 생김. (account밑에 User라는 새로운 칸이 만들어짐)
class UserAdmin(admin.ModelAdmin):
    list_display=['username', 'email', 'phone_number']  #list display라고쓰면 user밑에 이름과 이메일과 전화번호가 보여지게 됨.
    list_display_links=['username', 'email', 'phone_number'] #링크
    