from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    phone_num = models.CharField(max_length=15)



    




class Phones(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='photos/')
    description = models.TextField()



    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
