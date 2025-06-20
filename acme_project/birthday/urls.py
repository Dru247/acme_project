from django.urls import path

from .views import (BirthdayCreateView, BirthdayDeleteView, BirthdayDetailView,
                    BirthdayListView, BirthdayUpdateView)

app_name = 'birthday'

urlpatterns = [
    path('', BirthdayCreateView.as_view(), name='create'),
    path('list/', BirthdayListView.as_view(), name='list'),
    path('<int:pk>/', BirthdayDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', BirthdayUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', BirthdayDeleteView.as_view(), name='delete')
]
