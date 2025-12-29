from django.views.generic import ListView, DetailView
from core.models import Petition
from django.shortcuts import get_object_or_404, redirect
from .forms import PetitionSignerForm

class PetitionListView(ListView):
    model = Petition
    template_name = "petitions/petition_list.html"
    context_object_name = "petitions"


class PetitionDetailView(DetailView):
    model = Petition
    template_name = "petitions/petition_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PetitionSignerForm()
        context["signers_count"] = self.object.signers.count()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = PetitionSignerForm(request.POST)

        if form.is_valid():
            signer = form.save(commit=False)
            signer.petition = self.object
            signer.save()
            return redirect("petitions:petition_detail", pk=self.object.pk)

        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)