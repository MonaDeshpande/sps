from django.db import models

# Create your models here.
class administrator_login(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    admin_id = models.CharField(max_length=100)
    admin_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    reenter_password = models.CharField(max_length=100)
    

    def __str__(self):
        return self.firstname 