from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import ProfileUpdateForm
from .models import Profile


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/profile.html'

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/profile_update.html'

class ProfileDeleteView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/profile_delete.html'

class ProfileCreateView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/profile_create.html'







# Create your views here.
