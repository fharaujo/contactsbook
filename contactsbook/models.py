from django.db import models

# criando a(o) classe/modelo com os campos.


class Contacts(models.Model):
    name = models.CharField(max_length=50, blank=False)
    relations = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, blank=False)

    # cria visualização amigável no admin
    def __str__(self):
        return f'{self.name} -  Telefone - {self.phone}'