from django.db import models
from account.models import UserProfile

class Dream(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    dream_detail = models.CharField(max_length=400)
    emotion_during_detail = models.CharField(max_length=400)
    emotion_waking_detail = models.CharField(max_length=400)
    event_related_detail = models.CharField(max_length=400)
    dream_symbolize_detail = models.CharField(max_length=400)
    similar_dream_detail = models.CharField(max_length=400)
    prediction_option = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.prediction_option)