from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"), # Hooks up root URL of app to the project_index view
    # Allows dynamic generation of URLs depending on the view (project)
    # Tells Django the value passed for pk in the URL is an int
    path("<int:pk>/", views.project_detail, name="project_detail"),
]