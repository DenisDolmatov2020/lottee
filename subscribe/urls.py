from django.urls import path
from django.views.generic import TemplateView

from . import views
urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('home', TemplateView.as_view(template_name="subscribe/home.html"), name='home'),
    path('send-form-email/', views.SendFormEmail.as_view(), name='send_email'),
]
