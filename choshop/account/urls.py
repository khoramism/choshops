from django.urls import path
from . import views 

app_name = 'account'

urlpatterns = [
    path('create/', views.AccountCreateView.as_view(), name='create_account'),
    path('edit/<int:pk>', views.AccountUpdateView.as_view(), name='update_account'),
    path('<int:pk>', views.AccountDetailView.as_view(), name='detail_account'),
   # path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegistrationView.as_view(), name='register'),
]

