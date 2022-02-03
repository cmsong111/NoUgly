from enum import unique
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('must have user email')

        user = self.model(
            email=self.normalize_email(email),
            # self.normalize_email? - >email을 정규화
            # -> @ 뒤에 값을 대소문자 구분 x로 만듦으로서 다중 가입 방지
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(
            email,
            password=password,
            **extra_fields
        )
        user.is_admin = True

        user.save(using=self._db)
        return user
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    Gender_choices = {
        ('남', '남자'),
        ('여', '여자')
    }
    name = models.CharField(max_length=15)
    date = models.DateField(blank=True)

    gender = models.CharField(max_length=20, choices=Gender_choices)

    address = models.CharField(max_length=250, blank=True, null=True)
    phone_num = models.CharField(max_length=16,blank=True, null=True, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
  


    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'date', 'gender', 'phone_num', 'address']

    class Meta:
        db_table = 'accounts'
        verbose_name = '유저',
        verbose_name_plural = '유저'

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
