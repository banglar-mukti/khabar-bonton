from django.urls import path

from core import views

urlpatterns = [
    path("user/",
        views.UserViewset.as_view(),
        name="user"
    )
]
