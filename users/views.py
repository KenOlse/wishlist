from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView, LogoutView


class WishlistLoginView(LoginView):
	template_name = 'accounts/login.html'


class WishlistLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/logout.html'


@login_required
def profile(request):
	return render(request, 'accounts/profile.html')