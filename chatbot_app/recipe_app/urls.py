from django.urls import path
from . import views

urlpatterns=[
	path('', views.recipe_app, name="recipe_app")

]
