from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Skill_Pertama', views.skill1, name='Skill_Pertama'),
    path('Skill_Kedua', views.skill2, name='Skill_Kedua'),
    path('Skill_Ketiga', views.skill3, name='Skill_Ketiga'),
]