from django.urls import path

from .views import Homepage

app_name = 'pages'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
]
