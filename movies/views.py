from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Movie, Review
from .forms import ReviewForm


def home(request):
    searchTerm = request.GET.get("searchMovie")
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(
        request, "movies/home.html", {"searchTerm": searchTerm, "movies": movies}
    )


def about(request):
    return render(request, "movies/about.html", {})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    context = {"movie": movie, "reviews": reviews}
    return render(request, "movies/detail.html", context)


@login_required
def create_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == "POST":
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.movie = movie
            new_review.save()
            return redirect("detail", new_review.movie.id)

    form = ReviewForm()
    context = {"form": form, "movie": movie}
    return render(request, "movies/create_review.html", context)


@login_required
def update_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == "POST":
        form = ReviewForm(data=request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("detail", review.movie.id)
    form = ReviewForm(instance=review)
    context = {"form": form, "review": review}
    return render(request, "movies/update_review.html", context)


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect("detail", review.movie.id)
