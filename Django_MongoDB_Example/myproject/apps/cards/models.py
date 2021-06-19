from django.db import models
from apps.decks.models import Deck

# Create your models here.
class Card(models.Model):
    question =models.CharField(max_length=250)
    answer =models.TextField()
    # Foreign Key
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.question
    