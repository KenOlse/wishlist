from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView
from django.views.generic import CreateView

from .models import AdvUser
from .forms import RegisterUserForm


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


class WishlistLoginView(LoginView):
    template_name = 'accounts/login.html'


class WishlistLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/logout.html'


class WishlistPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('users:profile')
    success_message = 'The Password is changed'


class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'accounts/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('users:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'accounts/register_done.html'


class DeleteUserView(DeleteView):
    model = AdvUser
    template_name = 'accounts/delete_user.html'
    success_url = reverse_lazy('main:index')


    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        logout(request)
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset
        return get_object_or_404(AdvUser, pk=self.user_id)