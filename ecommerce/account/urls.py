from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('login/', views.loginView,name="login"),
    path('register/', views.registerView ,name="register"),
    path('logout/', LogoutView.as_view(next_page='login'),name="logout"),

]