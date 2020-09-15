from django.urls import path, include
from . import views


urlpatterns = [
    path('students/', views.StudentView),
    path('students/<id>', views.StudentDetailView),
    path('Scores/<id>', views.ScoreDetailView),
    path('scores/', views.ScoreView),
    path('scores', views.ScoreView.as_view)
]

 