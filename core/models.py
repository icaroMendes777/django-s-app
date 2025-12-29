from django.db import models

class Petition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PetitionSigner(models.Model):
    petition = models.ForeignKey(
        Petition,
        on_delete=models.CASCADE,
        related_name="signers"
    )
    name = models.CharField(max_length=150)
    email = models.EmailField()
    signed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("petition", "email")  # prevents double signing

    def __str__(self):
        return f"{self.name} ({self.email})"