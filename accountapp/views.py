from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from accountapp.models import HelloWorld
from django.views.generic import CreateView


# Create your views here.

def hello_world(request):
    # return HttpResponse("Hello World")
    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        # return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') #계정 만드는데 성공했다면 어느 URL로 redirect 될것인가
    template_name = 'accountapp/create.html'