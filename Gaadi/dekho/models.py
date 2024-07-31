from django.db import models

class UserInfo(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=128)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class CarBrand(models.Model):
    brand_name=models.CharField(max_length=128)
    brand_popularity_score=models.IntegerField()
    Brand_Accesibility_Score=models.IntegerField()
    Service_Quality_Score=models.IntegerField()
    Maintainence_Spares_Score=models.IntegerField()
    Reliability_Score=models.IntegerField()
    Resale_Value_Score=models.IntegerField()
    Safety_Score=models.IntegerField()
    
class CarType(models.Model):
    Car_Name=models.CharField(max_length=128)
    Min_Price=models.FloatField()
    Max_Price=models.FloatField()
    Vehicle_Type=models.CharField(max_length=128)
    

class CarVariant(models.Model):
    variant_name=models.CharField(max_length=128)
    Mileage=models.FloatField()
    Power=models.FloatField()
    Transmission=models.CharField(max_length=128)


