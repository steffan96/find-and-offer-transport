from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
)
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import LikeDislike, Post, Comment
from .forms import PostCreateForm, CommentForm


class HomePageView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 4
    template_name = "posts/home.html"

    def get_queryset(self):
        ordering = ["-updated", "-created"]
        searched = self.request.GET.get("searched", "")
        offering = self.request.GET.get("offering", "")
        looking = self.request.GET.get("looking", "")

        if searched and looking and offering:
            object_list = self.model.objects.filter(
                author__city__icontains=searched
            ).order_by(*ordering)
        elif searched and offering:
            object_list = self.model.objects.filter(
                offering=True, author__city__icontains=searched
            ).order_by(*ordering)
        elif searched and looking:
            object_list = self.model.objects.filter(
                looking=True, author__city__icontains=searched
            ).order_by(*ordering)
        else:
            object_list = self.model.objects.filter(
                author__city__icontains=searched
            ).order_by(*ordering)
        return object_list


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"


class PostUpdateView(SuccessMessageMixin, UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    fields = ["title", "body"]
    success_url = reverse_lazy("posts:home")
    success_message = "Uspješno!"


class PostDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = reverse_lazy("posts:home")
    success_message = "Obrisano!"


class PostCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = PostCreateForm
    template_name = "posts/post_new.html"
    success_url = reverse_lazy("posts:home")
    success_message = "Uspješno!"

    def form_valid(self, form):
        form.instance.author = self.request.user
        offering = self.request.GET.get("offering", "")
        looking = self.request.GET.get("looking", "")
        if looking:
            form.instance.looking = True
        elif offering:
            form.instance.offering = True
        return super().form_valid(form)


class AddCommentView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "posts/add_comment.html"
    success_url = reverse_lazy("posts:home")
    success_message = "Uspješno!"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def like_dislike(request, post_id):
    post = Post.objects.get(pk=post_id)
    try:
        like = LikeDislike.objects.get(user=request.user, post=post)
        if like.value == 1:
            like.value -= 1
            post.likes -= 1
            post.users_liked.remove(request.user)
            like.save()
            post.save()
            return redirect("posts:home")
        elif like.value == 0:
            like.value += 1
            post.likes += 1
            post.users_liked.add(request.user)
            like.save()
            post.save()
            return redirect("posts:home")
    except:
        new_like = LikeDislike(user=request.user, post=post, value=1)
        post.likes += 1
        post.users_liked.add(request.user)
        post.save()
        new_like.save()
        return redirect("posts:home")
    return HttpResponse("Greška! Molimo pokušajte ponovo.")
