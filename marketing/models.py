from django.db import models

# Create your models here.
class Signup (models.Model):
    email = models.EmailField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Contact (models.Model):
    emailcontact = models.EmailField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    messagecontact = models.CharField(max_length=500)

    def __str__(self):
        return self.emailcontact