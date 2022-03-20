from django.urls import path
from . import views
from .views import MyRegisterFormView

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('registration/', MyRegisterFormView.as_view(), name='registration'),
    path('logout/', views.logoutUser, name = "logout")
]