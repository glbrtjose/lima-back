from django.urls import path

from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('', views.HelloView.as_view(), name=''),
    path('sign-in', obtain_auth_token, name='sign-in'),
    path('credits', views.credits, name='credits'),
    path('approve-credits', views.approve_credits, name='approve_credits'),
    # path('', views.index, name=''),
]