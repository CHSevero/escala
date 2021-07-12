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
