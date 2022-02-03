from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_field
import datetime
#https://stackoverflow.com/questions/37841612/django-rest-auth-custom-registration-fails-to-save-extra-fields
class CustomUserAccountAdapter(DefaultAccountAdapter):
    """
    Saves a new `User` instance using information provided in the
    signup form.
    """
    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, False)
        data = form.cleaned_data

        user_field(user, 'name', request.data.get('name', ''))
        user_field(user, 'date', request.data.get('date', datetime.datetime.now()))
        user_field(user, 'gender', request.data.get('gender', '남'))
        user_field(user, 'address', request.data.get('address', ''))
        user_field(user, 'phone_num', request.data.get('phone_num', ''))
        
        user.save()
        return user
