from django.urls import path

from .views import home, about, detail, create_review, update_review, delete_review


urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("movies/<int:movie_id>/", detail, name="detail"),
    path("movies/<int:movie_id>/create/", create_review, name="create_review"),
    path("movies/review/<int:review_id>/update/", update_review, name="update_review"),
    path("movies/review/<int:review_id>/delete/", delete_review, name="delete_review"),
]
