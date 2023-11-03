from django.db import models

# Create your models here.
class Students(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    student_id = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname 
    

