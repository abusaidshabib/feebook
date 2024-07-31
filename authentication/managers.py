from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, passwrod=None, **extra_fields):
        """
        Create and saves a users with the given email, username and password
        """
        if not email:
            raise ValueError("Users must haven and email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        if passwrod:
            user.set_password(passwrod)

        user.save(using=self._db)
        return user
    def create_superuser(self, email, password=None):

        """
        Create and saves a super users with the given emailj, username and password
        """

        user = self.create_user(email, password)
        user.is_active = True
        user.is_seller = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
