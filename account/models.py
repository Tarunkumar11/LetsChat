from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.utils.translation import ugettext_lazy as _

GENDER_CHOICES = [
    ('Male', _('Male')),
    ('Female', _('Female')),
    ('Other', _('Other')),
]

class UserManager(BaseUserManager):
    def create_user(self,email,username,first_name = None,last_name = None,password=None):
        if not email:
            raise ValueError("Please provide the email")
        if not username:
            raise ValueError("Please provide the username")
        user = self.model(email = self.normalize_email(email),username=username,first_name= first_name,last_name=last_name)
        user.set_password(password)
        user.save(using = self._db) 
        return user

    def create_superuser(self,email,username,first_name = None,last_name = None,password=None):
        if not email:
            raise ValueError("Please provide the email")
        if not username:
            raise ValueError("Please provide the username")
        user = self.create_user(email = self.normalize_email(email),username=username,first_name = first_name,last_name = last_name,password = password)
        user.is_admin =   True
        user.is_staff  =    True
        user.is_superuser = True
        user.save(using = self._db) 
        return user


# Create your models here.
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email =  models.EmailField(verbose_name="email",max_length=60,unique=True)
    username = models.CharField(max_length=20,unique=True)
    date_joined = models.DateTimeField(verbose_name='Date joined',auto_now_add=True)
    last_login= models.DateTimeField(verbose_name='Last login',auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    gender = models.CharField(verbose_name  = 'Gender', max_length=20, choices=GENDER_CHOICES,  blank=True)
    dob = models.DateField(_('DoB'), blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    objects = UserManager()
    def __str__(self):
        return "Email :{0}".format(self.email)

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField()

    def __str__(self):
        return 'image_id: {} user_email: {}'.format(self.pk, self.user)

