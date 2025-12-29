from django.urls import path
from .views import PetitionListView, PetitionDetailView

urlpatterns = [
    path("", PetitionListView.as_view(), name="petition_list"),
    path("<int:pk>/", PetitionDetailView.as_view(), name="petition_detail"),
]
