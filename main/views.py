from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.conf import settings
from django.template.loader import get_template
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


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

def listing(request):
    contact_list = AdvUser.objects.all()
    paginator = Paginator(contact_list, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'users/advuser.html', {'page_obj': page_obj})

class UserList(ListView):
    model = AdvUser
    context_object_name = 'users_owners'
    paginate_by = 2
    


