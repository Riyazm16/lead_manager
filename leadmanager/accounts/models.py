from django.db import models
from django.contrib.auth.models import BaseUserManager

# Create your models here.
# ---------------------------ADMIN CUSTOMIZATION---------------------------------
class User(BaseUserManager):
    """ This is a manager to perform duties such as CRUD(Create, Read,
     Update, Delete) """
    class Meta:
        db_table = "auth_user"
        
    def create_user(self, username,email, password=None):
        """ This creates a admin user object """

        if not email:
            raise ValueError("It is mandatory to require an email!")

     
        if not username:
            raise ValueError("Please provide a username:")

        email = self.normalize_email(email=email)
        user = self.model(email=email,username=username)

        """ This will allow us to store our password in our database
         as a hash """
        user.set_password(password)
        user.save(using=self._db)

        return user

