from django.urls import path

from .views import (
    HomeView,
    LoginView,
    LogoutView,
    CompaniesView,
    ActivityView,
    CategoriesView,
    RegistrationView,
    AboutView,

)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("home/", HomeView.as_view(), name="home"),
    path("categories/", CategoriesView.as_view(), name="categories"),
    path("categories/<str:pk>/", ActivityView.as_view(), name="categories"),
    path("all_companies/", CompaniesView.as_view(), name="companies"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("about/", AboutView.as_view(), name="about"),

]
