


from django.urls import path, include
from .views import ApiView
urlpatterns = [
  
    path('',ApiView.as_view()),
]

