from django.urls import path
from .views import home,privateNote

urlpatterns = [
    path('', home),
    path('note/<int:pk>/', privateNote.as_view()),
    path('note/', privateNote.as_view()),
]