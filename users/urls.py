from django.urls import path
from .views import WishlistLoginView, WishlistLogoutView, WishlistPasswordChangeView
from .views import profile, RegisterUserView, RegisterDoneView
from .views import DeleteUserView

app_name = 'users'
urlpatterns = [
    path('accounts/profile/delete/',
         DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/register/done', RegisterDoneView.as_view(),
         name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register_user'),
    path('accounts/password/change/',
         WishlistPasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', WishlistLogoutView.as_view(), name='logout'),
    path('accounts/login/', WishlistLoginView.as_view(), name='login'),
]
