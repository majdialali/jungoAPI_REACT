from django.db import models
from django.contrib.auth.models import AbstractUser
#UserProfile as a database table (to save new users)
"""OBS
""Why Don’t we See Passwords in my  models.py?
Because we are using Django's built-in User model, not UserProfile.
Django already stores passwords inside auth_user table, which models.py does not need to define manually."""


class UserProfile(AbstractUser):  # ✅ Custom user model with extra fields
    phone_number = models.IntegerField( blank=True, null=True)  # ✅ Extra field
    #what abuout id, password, email, or username? Since your model extends AbstractUser, Django automatically includes these fields for you.
    def __str__(self):
        return self.username  # ✅ Displays username in Django admin




"""


🎯 Summary
Feature	Example
Create a Model	    class UserProfile(models.Model): ...
Define Fields	    username = models.CharField(max_length=150)
Use Relationships	user = models.ForeignKey(User, on_delete=models.CASCADE)
Control Ordering	class Meta: ordering = ['-created_at']
Save Data	        user.save()


Command	                What It Does	                                               When To Use
makemigrations	        Creates migration files (instructions for database changes)	   After modifying models.py
migrate	                Applies migration files to update the database	               After running makemigrations

Think of it like this:

makemigrations writes a plan (creates migration files).
migrate executes the plan (updates the actual database).

makemigrations: creates migration files, which are instructions for how Django should modify the database. (see 0001_intial/002_intial)

migrate: Django reads the migration file (0001_initial.py) and actually creates the table in the database.

"""

"""
Django’s AbstractUser already comes with these fields:

Field Name	        Purpose
id	                Auto-increment primary key (Django always adds this automatically).
username	        Unique identifier for login.
email	            Stores the user's email.
password	        Stores a hashed version of the password.
first_name	        Optional first name.
last_name	        Optional last name.
is_staff	        Boolean: Can the user access Django admin?
is_active	        Boolean: Is the user’s account active?
date_joined	        Timestamp when the user registered.

"""