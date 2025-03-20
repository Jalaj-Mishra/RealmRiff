from django.views import View
from django.shortcuts import render, HttpResponse
from django.contrib.auth import get_user
from genres.models import Genre, GenreFellow
from posts.models import Post

class HomePage(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'index.html')
        user_logged_in = get_user(request)
        association_list = []
        print("Testing###########1", user_logged_in.username)

        # Accessing the items in Genre DB
        GenreItems = GenreFellow.objects.all()
        if len(GenreItems) == 0:
            return render(request, 'genres/genre_list.html')
        for item in GenreItems:     
            print("#######2",item)
            if item.user == user_logged_in:
                print("Test-item", item.user)
                association_list.append(item.genre)
        post_to_displayed = [
            post_item
            for post_item in Post.objects.all()
            if post_item.genre in association_list
        ]
        return render(request, 'user_home.html', {'post_list': post_to_displayed})
