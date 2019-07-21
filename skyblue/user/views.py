from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView
from user.forms import UserRegistrationForm

class UserRegistrationView(View):
    def post(self, request):
        user_registration_form = UserRegistrationForm(request.POST)

        if user_registration_form.is_valid():
            user_registration_form.save()
            username = user_registration_form.cleaned_data.get('username')
            raw_password = user_registration_form.cleaned_data.get('password1')
            
            first_name = user_registration_form.cleaned_data["first_name"]
            last_name = user_registration_form.cleaned_data["last_name"]

            messages.success(request, f"Congrats, { first_name }, { last_name }, you've made an account!")
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return HttpResponseRedirect(reverse_lazy('media:media-list'))

        context = {
            'user_registration_form': user_registration_form
        }
        
        return render(request, 'user/register.html', context)

    def get(self, request):
        user_registration_form = UserRegistrationForm()
        
        context = {
            'user_registration_form': user_registration_form
        }

        return render(request, 'user/register.html', context)

class UserLoginView(LoginView):
    template_name = 'user/login.html'
    success_url = reverse_lazy('media:media-list')

    def get_success_url(self):
        return success_url

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        
        messages.info(request, 'You are now logged out')
        return HttpResponseRedirect(reverse_lazy('media:media-list'))

class UserList(ListView):
    model = User
    context_object_name = 'users'
    template_name='user/user_list.html'
    paginate_by = 7
    
    # In case we need to define new dictionary elements
    # in the context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context