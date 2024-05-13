from django.urls import path
from products_app import views


urlpatterns = [
    path("", views.home_view, name="home"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_view, name="logout")
]