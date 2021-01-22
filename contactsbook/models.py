from django.db import models

# Create your models here.


class Contacts(models.Model):
    name = models.CharField(max_length=50, blank=False)
    relations = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, blank=False)


    def __str__(self):
        return f'{self.name} -  Telefone - {self.phone}'