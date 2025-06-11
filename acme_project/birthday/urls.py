from django.urls import path

from .views import birthday, birthday_list

app_name = 'birthday'

urlpatterns = [
    path('', birthday, name='create'),
    path('list/', birthday_list, name='list')
]
