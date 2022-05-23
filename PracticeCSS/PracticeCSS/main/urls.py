from django.urls import path

from PracticeCSS.main.views import index_view

urlpatterns = (
    path('', index_view, name="index"),
)