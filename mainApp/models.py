from django.db import models


class Qoshiqchi(models.Model):
    ism = models.CharField(max_length=100)
    t_sana = models.DateField(blank=True, null=True)
    davlat = models.CharField(max_length=100)

    def __str__(self):
        return self.ism


class Albom(models.Model):
    nom = models.CharField(max_length=100)
    sana = models.DateField()
    rasm = models.ImageField(upload_to='albomlar/', blank=True, null=True)
    qoshiqchi = models.ForeignKey(Qoshiqchi, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Qoshiq(models.Model):
    nom = models.CharField(max_length=100)
    janr = models.CharField(max_length=100)
    davomiylik = models.DurationField(blank=True, null=True)
    audio = models.FileField(upload_to='qoshiqlar/', blank=True, null=True)
    albom = models.ForeignKey(Albom, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom
