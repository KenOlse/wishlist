from django.urls import path

from .views import index, other_page, WishlistTemplateView, WishListView

app_name = 'main'


urlpatterns = [
    path('wishlist_list/<int:product_id>/', WishListView.as_view(), name='wishlist_list'),
    path('wishlist/', WishlistTemplateView.as_view(), name='wishlist'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),

]
