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


class Place(models.Model):
    name = models.CharField('Nome', max_length=255)
    active = models.BooleanField("Ativo", default=True)

    class Meta:
        verbose_name = "Posto de Trabalho"
        verbose_name_plural = "Postos de Trabalho"

    def __str__(self):
        return self.name


class Address(models.Model):
    country = models.CharField('País', max_length=255)
    state = models.CharField('Estado', max_length=255)
    city = models.CharField('Cidade', max_length=255)
    district = models.CharField('Bairro', max_length=255)
    street = models.CharField('Rua', max_length=255)
    number = models.CharField('Número', max_length=255)
    place = models.OneToOneField(Place, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    def __str__(self):
        return (
            f"{self.street}, {self.number}, {self.district}, "
            f"{self.city}, {self.state}, {self.country}"
        )


class DayOf(models.Model):
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6
    SATURDAY = 7

    WEEKDAYS = [
        (MONDAY, 'Segunda'),
        (TUESDAY, 'Terça'),
        (WEDNESDAY, 'Quarta'),
        (THURSDAY, 'Quinta'),
        (FRIDAY, 'Sexta'),
        (SATURDAY, 'Sábado'),
        (SUNDAY, 'Domingo'),
    ]

    day = models.IntegerField("Folga", choices=WEEKDAYS)
    doctor = models.ForeignKey(
        Doctor,
        verbose_name="Médico",
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Folga"
        verbose_name_plural = "Folgas"
        unique_together = ['day', 'doctor']

    def convert_weekday(self):
        if self.day == 1:
            return 'Domingo'
        if self.day == 2:
            return 'Segunda'
        if self.day == 3:
            return 'Terça'
        if self.day == 4:
            return 'Quarta'
        if self.day == 5:
            return 'Quinta'
        if self.day == 6:
            return 'Sexta'
        if self.day == 7:
            return 'Sábado'

    def __str__(self):
        return self.convert_weekday()
