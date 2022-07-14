
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Perfils
User = get_user_model()


@receiver(post_save, sender=User)
def crete_profile(sender, instancia, created, *args, **kwargs):
    if created:
        profile = Perfils.objects.create(author=instancia)
        profile.save()
