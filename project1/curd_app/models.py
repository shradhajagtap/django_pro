from django.db import models


class Company(models.Model):
    PAYMENT_CHOICE = [("OL", "Online"), ("OFF", "Offline")]
    CITY_CHOICE = [("MUMBAI", "Mumbai"), ("PUNE", "Pune"), ("NASHIK", "Nashik"), ("OBAD", "Obad")]
    company_name = models.CharField(max_length=20)
    company_owner = models.CharField(max_length=20)
    company_total_emp = models.IntegerField()
    company_state = models.CharField(max_length=10)
    city_pincode = models.IntegerField()
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_CHOICE)
    city_mode = models.CharField(max_length=20, choices=CITY_CHOICE, default="Pune")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
