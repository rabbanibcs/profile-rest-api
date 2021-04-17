from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self,email,username,password=None,**others):

        user=self.model(email=email,username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,email,username,password=None,**others):
        user=self.create_user(email,username,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user















#,first_name=others[first_name],last_name=others[last_name]