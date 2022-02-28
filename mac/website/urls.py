from django.urls import path
from . import views
# from .views import RegisterView
from .views import RegisterView

urlpatterns = [
    path('', views.index, name="login"),
    path('change_password/', views.ChangePasswordView.as_view(), name="auth_change_password"),
    path('get/', views.getData),
    path('teacher/', views.Teacher, name='teacher'),
    path('register/', RegisterView.as_view()),
    path('about/', views.about, name='about'),
    path('table/', views.table, name="Table"),

]
