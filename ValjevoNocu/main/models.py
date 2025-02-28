from django.db import models

# Create your models here.

class Kafic(models.Model):
    ID=models.AutoField(primary_key=True)
    Ime=models.CharField(max_length=30,null=False)
    photo = models.ImageField(upload_to='photos/',null=True)

    def __str__(self):
        return self.Ime
    
class Svirka(models.Model):
    ime=models.CharField(max_length=40)
    datum=models.DateField(null=True)
    opis=models.CharField(max_length=300)
    proslo=models.BooleanField(default=False)
    kafic = models.ForeignKey(Kafic, on_delete=models.CASCADE, related_name='svirke',null=True)

    def __str__(self):
        return self.ime
    