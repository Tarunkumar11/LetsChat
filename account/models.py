from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("Please provide the email")
        if not username:
            raise ValueError("Please provide the username")
        user = self.model(email = self.normalize_email(email),username=username)
        user.set_password(password)
        user.save(using = self._db) 
        return user

    def create_superuser(self,email,username,password=None):
        if not email:
            raise ValueError("Please provide the email")
        if not username:
            raise ValueError("Please provide the username")
        user = self.create_user(email = self.normalize_email(email),username=username,password = password)
        user.is_admin =   True
        user.is_staff  =    True
        user.is_superuser = True
        user.is_host = True
        user.save(using = self._db) 
        return user


# Create your models here.
class User(AbstractBaseUser):
    name = models.CharField(max_length=20,null=False)
    email =  models.EmailField(verbose_name="email",max_length=60,unique=True)
    username = models.CharField(max_length=20,unique=True)
    date_joined = models.DateTimeField(verbose_name='Date joined',auto_now_add=True)
    last_login= models.DateTimeField(verbose_name='Last login',auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)
    is_host = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()
    def __str__(self):
        return "Email :{0}".format(self.email)
    
    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_perms(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True
