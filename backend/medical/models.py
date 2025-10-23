from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    ]

    MARITAL_STATUS_CHOICES = [
        ('S', 'Soltero/a'),
        ('C', 'Casado/a'),
        ('D', 'Divorciado/a'),
        ('V', 'Viudo/a')
    ]

    identification_number = models.CharField(max_length=20, unique=True, verbose_name="Número de Identificación")
    name = models.CharField(max_length=50, verbose_name="Nombre")
    last_name = models.CharField(max_length=50, verbose_name="Apellido")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Género")
    date_of_birth = models.DateField(verbose_name="Fecha de Nacimiento")
    address = models.TextField(verbose_name="Dirección")
    phone_number = models.CharField(max_length=15, verbose_name="Teléfono")
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES, verbose_name="Estado Civil")
    occupation = models.CharField(max_length=100, verbose_name="Ocupación")
    insurance_provider = models.CharField(max_length=100, blank=True, verbose_name="Proveedor de Seguro")
    insurance_number = models.CharField(max_length=50, blank=True, verbose_name="Número de Seguro")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='patients_created', verbose_name="Creado por")

    def __str__(self):
        return f"{self.get_full_name()} - {self.identification_number}"

    def get_full_name(self):
        return f"{self.name} {self.last_name}"

    class Meta:
        app_label = "medical"
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ['-created_at']
