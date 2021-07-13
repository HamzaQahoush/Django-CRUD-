from django.urls import path
from .views import (
    snackView,
    snack_Detail_View,
    SnackCreateView,
    SnackUpdateView,
    SnackDeleteView,
)


urlpatterns = [
    path("", snackView.as_view(), name="view"),
    path("<int:pk>/", snack_Detail_View.as_view(), name="detailView"),
    path("create/", SnackCreateView.as_view(), name="snack_create"),
    path("<int:pk>/update/", SnackUpdateView.as_view(), name="snack_update"),
    path("<int:pk>/delete/", SnackDeleteView.as_view(), name="snack_delete"),
]
