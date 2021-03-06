from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
# Create your models here.
#

class UserManager(BaseUserManager):
    def create_user(self, email, name, password = None):
        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email = email, name = name)
        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True

        user.staff  =True
        user.save(using = self.db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    active = models.BooleanField(default = True)
    staff = models.BooleanField(default = True)
    admin = models.BooleanField(default = False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'usuarios'
        verbose_name = 'usuario'
        ordering = ['id']

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin
