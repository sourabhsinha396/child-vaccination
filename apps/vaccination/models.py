from django.db import models

from .utils import random_slug

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name + " ---" + " " + self.subject


class Parent(models.Model):
    slug = models.SlugField(max_length=20, unique=True,blank=True,null=True)
    aadhar = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10,unique=True,blank=True,null=True)

    def __str__(self):
        return self.name 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = random_slug(name=self.name) 
        super().save(*args, **kwargs)
    

blood_group_choices = (("b+ve", "B Positive"), ("b-ve", "B Negative"), ("o+ve", "O Positive"), ("o-ve", "O Negative"), ("a+ve", "A Positive"), ("a-ve", "A Negative"), ("ab+ve", "AB Positive"), ("ab-ve", "AB Negative"))

class Mother(models.Model):
    mode_of_delivery = (("normal", "Normal"), ("cesarean", "Cesarean"), ("forceps", "Forceps"), ("vacuum", "Vacuum"), ("other", "Other"))

    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, related_name="mother")
    slug = models.SlugField(max_length=20, unique=True,blank=True,null=True)
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=10, choices=blood_group_choices,blank=True,null=True)
    last_delivery_date = models.DateField(blank=True,null=True)
    mode_of_delivery = models.CharField(max_length=10, choices=mode_of_delivery,blank=True,null=True)
    place_of_delivery = models.CharField(max_length=100,blank=True,null=True)
    remarks = models.TextField(help_text="Any other remarks/complications")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = random_slug(name=self.name) 
        super().save(*args, **kwargs)


class Child(models.Model):
    gender_choices = (("male","Male"),("female","Female"),("others","Others"))

    slug = models.SlugField(max_length=20, unique=True,blank=True,null=True)
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True,related_name="child")
    mother = models.ForeignKey(Mother, on_delete=models.SET_NULL, blank=True, null=True,related_name="child")
    name = models.CharField(max_length=100,blank=True,null=True)
    gender = models.CharField(max_length=10,choices=gender_choices,blank=True,null=True)
    blood_group = models.CharField(max_length=10, choices=blood_group_choices,blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    place_of_delivery = models.CharField(max_length=100,blank=True,null=True)
    remarks = models.TextField(help_text="Any other remarks/complications")

    def __str__(self):
        return self.name + " ---" + " " + self.parent.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = random_slug(name=self.name) 
        super().save(*args, **kwargs)
