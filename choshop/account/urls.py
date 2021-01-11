from django.urls import path
from . import views 
from django.contrib.auth.views import LoginView
from . import forms 
app_name = 'account'

urlpatterns = [
    path('create/', views.AccountCreateView.as_view(), name='create_account'),
    path('edit/<int:pk>', views.AccountUpdateView.as_view(), name='update_account'),
    path('<int:pk>', views.AccountDetailView.as_view(), name='detail_account'),
    path('login/', LoginView.as_view(template_name='account/login.html', form_class=forms.AuthenticationForm), name='login'),

    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegistrationView.as_view(), name='register'),
]

