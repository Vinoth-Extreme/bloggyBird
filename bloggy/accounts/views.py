from django.shortcuts import render, get_object_or_404
from  django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from .forms import SignupForm, CreateProfileForm, UserEditForm, PasswordChangingForm
from django.urls import reverse_lazy
from blog.models import Profile, Post
from django.views.generic import DetailView

# Create your views here.
class UserRegisterView(generic.CreateView):
    model = User
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = UserEditForm
    template_name = 'registration/edit_user_form.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordUpdateView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change_pass.html'
    success_url = reverse_lazy('password_success')

def PassSuccess(request):
    return render(request, 'registration/password_success.html')


class CreateProfileFormPage(generic.CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'registration/create_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ShowProfileView(DetailView):
    model = Profile
    template_name = 'registration/view_profile.html'

    def get_context_data(self, *args, **kwargs):
        articles = Post.objects.all()
        articles_count = Post.objects.filter(author=self.request.user.id).count()
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
        curr_profile = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['curr_profile'] = curr_profile
        context['articles'] = articles
        context['count'] = articles_count
        return context

class EditProfileView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = ('profile_pic', 'website_url', 'facebook_url', 'instagram_url', 'twitter_url', 'linkedin_url', 'bio')
    success_url = reverse_lazy('home')