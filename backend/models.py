from django.db import models



# Create your models here.


class MetaUser(models.Model):
    meta_username = models.CharField(max_length=40, default='raven88')
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, default='hacker@trill.com')
    created_at = models.DateField() ##the date when this user was created.
    modified_at = models.DateTimeField()  ##the timezone when the user_data was modified


    def __str__(self):
        #returns username & ID

        return 'username: %s -- ID: %s' % (self.meta_username, self.id)






