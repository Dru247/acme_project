from django.urls import path

from .views import delete_birthday, birthday, birthday_list

app_name = 'birthday'

urlpatterns = [
    path('', birthday, name='create'),
    path('list/', birthday_list, name='list'),
    path('<int:pk>/edit/', birthday, name='edit'),
    path('<int:pk>/delete/', delete_birthday, name='delete')
]
