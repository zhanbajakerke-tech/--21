from django.urls import path
from . import views

urlpatterns = [
    path('', views.process, name='process'),                  # басты бет
    path('exam1/', views.exam1, name='exam1'),                  # 1-емтихан
    path('exam2/', views.exam2, name='exam2'),               # 2-емтихан
    path('ratings/', views.ratings, name='ratings'),            # рейтинг
    path('students/', views.student_list, name='students'),  # students list
]
