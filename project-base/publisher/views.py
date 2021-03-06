from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, CreateView, ListView


from .forms import signUpForm, UserUpdateForm


class Home(ListView):
    template_name = 'home.html'
    queryset = []

class SignUp(CreateView):
    form_class = signUpForm
    template_name = 'user/signup.html'

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect('home')
    

class UserUpdateView(UpdateView):
    form_class = UserUpdateForm
    template_name = 'user/publisher.html'
    success_url = reverse_lazy('publisher')

    def get_object(self):
        return self.request.user

