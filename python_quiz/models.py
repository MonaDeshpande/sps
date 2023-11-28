from django.db import models

# Create your models here.
class administrator_login(models.Model):
    firstname = models.CharField(max_length=20, null=False)
    lastname = models.CharField(max_length=20, null=False)
    admin_id = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to="administrator_login/", blank=True)
    email_id = models.EmailField(blank=True)
    password = models.CharField(max_length=100, null=False)
    reenter_password = models.CharField(max_length=100, null=False)
    

    def __str__(self):
        return self.firstname