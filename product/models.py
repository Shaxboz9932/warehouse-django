from django.db import models

class WareHouse(models.Model):
    name = models.CharField(max_length=200)
    qty = models.FloatField(default=0)
    price = models.FloatField(max_length=10)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    mato = models.ForeignKey(WareHouse, on_delete=models.CASCADE, related_name='mato')
    tugma = models.ForeignKey(WareHouse, on_delete=models.CASCADE, related_name='tugma', blank=True)
    ip = models.ForeignKey(WareHouse, on_delete=models.CASCADE, related_name='ip')
    zamok = models.ForeignKey(WareHouse, on_delete=models.CASCADE, related_name='zamok', blank=True)


    def __str__(self):
        return self.name

