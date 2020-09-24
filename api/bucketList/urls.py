from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('languages', views.LanguageViewSet)
router.register('languagegroup', views.LanguageGroupViewSet)
router.register('favoritelanguage', views.FavoriteLanguageViewSet)
router.register('favoritelanguagegroup', views.FavoriteLanguageGroupViewSet)



urlpatterns = [
    # path('languages/', views.LanguagesView),
    path('', include(router.urls))

]

