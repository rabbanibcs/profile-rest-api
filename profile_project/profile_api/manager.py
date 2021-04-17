from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self,email,username,password=None,**others):

        user=self.model(email=email,username=username)
        user.set_password(password)
        user.save()


def create_superuser(self,email,username,password=None,**others):
    user=create_user(email,username,password)
    user.is_staff=True
    user.is_superuser=True
    user.save()















#,first_name=others[first_name],last_name=others[last_name]