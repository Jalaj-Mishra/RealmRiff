from django.db import IntegrityError
from django.urls import reverse
from . import models
from posts.models import Post
from django.views import View, generic
from django.shortcuts import render
from django.contrib import messages
from .models import Genre, GenreFellow
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
class CreateGenre(LoginRequiredMixin, generic.CreateView):
    fields = ["name", "description"]
    model = Genre

class SingleGenre(View):

    def get(self, request, *args, **kwargs):
        genre_opened = get_object_or_404(Genre, slug=self.kwargs.get('slug'))
        print("#################2", genre_opened)
        Post_to_displayed = []
        PostList = Post.objects.all()
        Post_to_displayed.extend(
            item
            for item in PostList
            if str(item.genre) == str(genre_opened.name)
        )
        print("##########33", Post_to_displayed)
        return render(request, 'genres/genre_detail.html', {"post_list": Post_to_displayed, 'genre': genre_opened})


class ListGenre(generic.ListView):
    model = Genre



class JoinGenre(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("genres:single", kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        genre = get_object_or_404(Genre, slug=self.kwargs.get("slug"))

        try:
            GenreFellow.objects.create(user=self.request.user, genre=genre)
        except IntegrityError:
            messages.warning(self.request, f"Warning, already a fellow of {genre.name}")

        else:
            messages.success(self.request, f"You are now a fellow of the {genre.name} genre.")

        return super().get(request, *args, **kwargs)



class LeaveGenre(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("genres:single", kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        try:
            fellowship = models.GenreFellow.objects.filter(
                user=self.request.user,
                genre__slug=self.kwargs.get("slug"),
            ).get()
        except models.GenreFellow.DoesNotExist:
            messages.warning(self.request, "You can't leave this genre because you are not in it.")

        else:
            fellowship.delete()
            messages.success(self.request, "You have successfully left this genre.")

        return super().get(request, *args, **kwargs)