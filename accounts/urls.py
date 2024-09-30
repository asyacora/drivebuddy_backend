from django.urls import path
from .views import UserCreate, SignInView

urlpatterns = [
    path('sign-up/', UserCreate.as_view(), name='sign_up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),

]
