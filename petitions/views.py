from django.views.generic import ListView, DetailView
from core.models import Petition

class PetitionListView(ListView):
    model = Petition
    template_name = "petitions/petition_list.html"
    context_object_name = "petitions"


class PetitionDetailView(DetailView):
    model = Petition
    template_name = "petitions/petition_detail.html"
    context_object_name = "petition"
