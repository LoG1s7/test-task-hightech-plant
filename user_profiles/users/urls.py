from django.urls import include, path

from users import views

urlpatterns = [
    path("", views.user_list, name="user_list"),
    path("accounts/", include("allauth.urls")),
    path(
        "accounts/profile/<uuid:user_id>/",
        views.user_profile,
        name="user_profile",
    ),
    path("accounts/profile/edit/", views.edit_profile, name="edit_profile"),
]
