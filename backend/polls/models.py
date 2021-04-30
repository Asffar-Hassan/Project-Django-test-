from django.db import models

# Create your models here.
    
class Categories(models.Model):
    Nom_cat=models.CharField(max_length=20)
    Desc_cat=models.CharField(max_length=100)
    
class Gamme(models.Model):
    Nom_gam=models.CharField(max_length=20)
    Desc_gam=models.CharField(max_length=100)


class Product(models.Model):
    Nom_prod=models.CharField(max_length=20)
    Prix=models.IntegerField()
    img=models.ImageField(null=True,blank=True,upload_to='images/')
    Desc_prod=models.CharField(max_length=100)
    nbr_stock=models.IntegerField()
    id_cat=models.ForeignKey(Categories,on_delete=models.CASCADE)
    id_ga=models.ForeignKey(Gamme,on_delete=models.CASCADE)

    def __str__(self):
        return self.Nom
    
