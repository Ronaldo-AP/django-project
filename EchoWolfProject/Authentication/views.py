from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, SignUpForm

from .models import User
from .toastMessages import ToastMessagesModel, mapValidationMessages

@login_required
def logoutView(request):
    logout(request)
    return redirect('login')


@login_required
def feedView(request):
    return render(request, 'feed.html')

# Build a custom login view with form
class CustomLoginView (LoginView):
    redirect_authenticated_user = True
    authentication_form = LoginForm
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('feed')
    
    def form_invalid(self, form):
        messages.error(self.request, ToastMessagesModel.unauthorized())
        return self.render_to_response(self.get_context_data(form=form))

class CustomSignUpView (FormView):
    template_name = 'login.html'
    success_url = '/feed/'
    form_class = SignUpForm

    def form_valid(self, form: SignUpForm):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            messages.success(self.request, ToastMessagesModel.signUpSuccess())
            return redirect(self.success_url)
        except:
            return self.form_invalid(form)
        
    def form_invalid(self, form: SignUpForm):
        mapValidationMessages(self.request, form.errors)
        return self.render_to_response(self.get_context_data(form=form))
