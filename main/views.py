from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.conf import settings
from django.template.loader import get_template
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .models import Product, WishListUser
from users.models import AdvUser


def index(request):
    return render(request, 'main/index.html')


def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


class WishlistTemplateView(TemplateView):
    template_name = 'main/wishlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wishlists'] = AdvUser.objects.all()
        return context


class WishListView(ListView):
    template_name = 'main/wishlist_list.html'
    content_object_name = 'wishlists'

    def get_queryset(self):
        return Product.objects.filter(id=self.kwargs['product_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wishlists'] = WishListUser.objects.all()
        context['current_wishlist'] = WishListUser.objects.get(
            id=self.kwargs['product_id'])
        return context


# class WishListDetailView(DetailView):
#     template_name = 'main/wishlist_detail.html'
#     model = WishList

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products'] = Wishlist.objects.all()
#         return context
