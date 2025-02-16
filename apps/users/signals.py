from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def activate_user_account(sender, instance, created, **kwargs):
#     if created:
#         instance.is_active = True
#         instance.save()
        
#         email = instance.email
#         email_address = EmailAddress.objects.get_or_create(user=instance, email=email)
#         email_address[0].verified = True
#         email_address[0].save()