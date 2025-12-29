from django import forms
from core.models import PetitionSigner

class PetitionSignerForm(forms.ModelForm):
    class Meta:
        model = PetitionSigner
        fields = ["name", "email"]
