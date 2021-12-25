from django.contrib import auth
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.messages.views import SuccessMessageMixin



from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes



class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    success_message = "Uspješno ste kreirali profil!"

    def form_valid(self, form):
        to = super().form_valid(form)
        user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
        login (self.request, user)
        return to

    


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
                
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "main/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
                        
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
                        
						return HttpResponse('Invalid header found.')
    
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password_reset.html", context={"password_reset_form":password_reset_form})