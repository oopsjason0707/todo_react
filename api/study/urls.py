from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()     
router.register('Student', views.Studentview)   # 2개의 URL을 만들어준다. 
router.register('Score', views.Scoreview)

urlpatterns = [
    path('', include(router.urls)),
    path('test', views.StudentBasicView),
    path('test'/'<pk>', views.StudentDetailBasicView)
    # path('students', views.StudentView.as_view()), 
    # path('students/<pk>', views.StudentDetailView.as_view()),
    # path('scores', views.ScoreView.as_view()),
    # path('scores/<id>', views.ScoreDetailView.as_view()),
    # path('students/', views.StudentView),
    # path('students/<id>', views.StudentDetailView),
    # path('scores/', views.ScoreView),
    # path('scores/<id>', views.ScoreDetailView)
    
]

 