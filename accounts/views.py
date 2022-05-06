from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import BadHeaderError, send_mail
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView, UpdateView

from chat.models import Message
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm



class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("posts:home")
    template_name = "registration/signup.html"
    success_message = "Uspješno ste kreirali profil!"

    def form_valid(self, form):
        validator = super().form_valid(form)
        user = authenticate(
            email=form.cleaned_data["email"], password=form.cleaned_data["password1"]
        )
        login(self.request, user)
        return validator


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CustomUserChangeForm
    model = CustomUser
    success_url = reverse_lazy("posts:home")
    template_name = "accounts/profile.html"
    success_message = "Uspješno ste ažurirali profil!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # get the number of unseen messages
        context["inbox_count"] = Message.objects.filter(
            ~Q(sender=self.request.user),
            Q(seen=False),
            (Q(chat__user1=self.request.user) | Q(chat__user2=self.request.user)),
        ).count()
        return context


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data["email"]
            associated_users = CustomUser.objects.filter(Q(email=data))
            if associated_users.exists():

                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "main/password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        "domain": "127.0.0.1:8000",
                        "site_name": "Website",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        "token": default_token_generator.make_token(user),
                        "protocol": "http",
                    }
                    email = render_to_string(email_template_name, c)
                    try:

                        send_mail(
                            subject,
                            email,
                            "admin@example.com",
                            [user.email],
                            fail_silently=False,
                        )
                    except BadHeaderError:

                        return HttpResponse("Invalid header found.")

                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(
        request=request,
        template_name="password_reset.html",
        context={"password_reset_form": password_reset_form},
    )


class ChangePassword(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("posts:home")
    template_name = "accounts/password.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # get the number of unseen messages
        context["inbox_count"] = Message.objects.filter(
            ~Q(sender=self.request.user),
            Q(seen=False),
            (Q(chat__user1=self.request.user) | Q(chat__user2=self.request.user)),
        ).count()
        return context
