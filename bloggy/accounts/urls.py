from django.urls import path
from .views import UserRegisterView, CreateProfileFormPage, ShowProfileView, EditProfileView, UserEditView,\
    PasswordUpdateView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_account/', UserEditView.as_view(), name='edit-account'),
    path('password/', PasswordUpdateView.as_view(), name='change-password'),
    path('password_success/', views.PassSuccess, name='password_success'),
    path('Build_profile/', CreateProfileFormPage.as_view(), name='build-profile'),
    path('<int:pk>/View_profile/', ShowProfileView.as_view(), name='view-profile'),
    path('<int:pk>/edit_profile/', EditProfileView.as_view(), name='edit-profile'),
]