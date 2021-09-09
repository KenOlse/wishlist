from django.urls import path
from .views import WishlistLoginView, WishlistLogoutView
from .views import profile

app_name = 'users'
urlpatterns = [
	path('accounts/profile/', profile, name='profile'),
	path('accounts/logout/', WishlistLogoutView.as_view(), name='logout'),
	path('accounts/login/', WishlistLoginView.as_view(), name='login'),
]