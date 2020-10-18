from django.urls import path

from . import views

app_name = 'statsApp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.CountryView.as_view(), name='country')
]