from django.db import models


class Doctor(models.Model):
    firstname = models.CharField('Nome', max_length=255)
    lastname = models.CharField('Sobrenome', max_length=255)
    admission_date = models.DateField('Data de Admissão')
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"
        unique_together = ['firstname', 'lastname', 'admission_date']

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Address(models.Model):
    country = models.CharField('País', max_length=255)
    state = models.CharField('Estado', max_length=255)
    city = models.CharField('Cidade', max_length=255)
    district = models.CharField('Bairro', max_length=255)
    street = models.CharField('Rua', max_length=255)
    number = models.CharField('Número', max_length=255)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    def __str__(self):
        return (
            f"{self.street}, {self.number}, {self.district}, "
            f"{self.city}, {self.state}, {self.country}"
        )
