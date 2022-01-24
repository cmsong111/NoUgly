from enum import unique
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):

    def create_user(self, email, name, gender, date, address, phone_num, password=None):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('must have user email')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            gender=gender,
            date=date,
            address=address,
            phone_num=phone_num
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, gender, date, address, phone_num, password):
        user = self.create_user(
            email,
            password=password,
            name=name,
            gender=gender,
            date=date,
            address=address,
            phone_num=phone_num,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
# Create your models here.


class User(AbstractBaseUser):
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
    date = models.DateField()

    gender = models.CharField(max_length=20, choices=Gender_choices)

    address = models.CharField(max_length=250, blank=True, null=True)
    phone_num = models.CharField(max_length=16, null=False, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
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
