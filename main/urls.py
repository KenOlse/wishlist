from django.urls import path

from .views import index, other_page, UserList

app_name = 'main'


urlpatterns = [
    path('list_owner/', UserList.as_view(), name='owner'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),

]
