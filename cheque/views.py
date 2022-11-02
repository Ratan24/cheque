from django.shortcuts import  redirect , render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import *

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def homepage( request):
  
    if request.method == 'POST':
        form = chequeForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = chequeForm()
    return render(request, 'cheque/upload.html', {'form' : form})

def success(request):
    return render(request, 'cheque/sucess.html')
  
  

    

class CustomLoginView(LoginView):
    template_name = 'cheque/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) :
        return reverse_lazy('homepage')


class RegisterPage(FormView):
    template_name = 'cheque/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('homepage')

    def form_valid(self, form) :
        user = form.save()
        if user is not None:
            login(self.request , user)
        return super(RegisterPage , self).form_valid(form)

    def get(self ,*args ,**kwargs) :
        if self.request.user.is_authenticated:
            return redirect('homepage')
        return super(RegisterPage , self).get(*args ,**kwargs)
