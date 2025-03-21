from django.contrib import messages
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic
from . import models
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
# Create your views here.

User = get_user_model()

class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ("user", 'genre')


class USerPosts(generic.ListView):
    model = models.Post
    template_name = "posts/user_post_list.html"


    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related("posts").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist as e:
            raise Http404 from e

        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context


class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ("user", "genre")

    def get_queryset(self):
        queryset = super().get_queryset()
        print("###########POST", self.request.user.username)
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )

class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ("name", "content", "genre")
    model = models.Post


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = models.Post
    select_related = ("user", "genre")
    success_url = reverse_lazy("posts:all")
    success_message = "Post Deleted"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # If the post doesn't belong to the current user, raise PermissionDenied
        if obj.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this post.")
        return obj

    def delete(self, *args, **kwargs):
        # Optionally, you could log the deletion or do any additional actions here
        print("###########Delete")
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)