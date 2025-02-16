from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.create_act_code()
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)





class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)
    act_code = models.CharField(max_length=128, blank=True)

    USERNAME_FIELD = "email"
    objects = UserManager()
    REQUIRED_FIELDS = []

    def create_act_code(self):
        from uuid import uuid4
        self.act_code = str(uuid4())

    def __str__(self):
        return self.email
    

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'



class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='profiles')
    avatar = models.ImageField(null=True, blank=True, upload_to='images/avatar/')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
    def __str__(self) -> str:
        return f'{self.user.email}'
        
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
