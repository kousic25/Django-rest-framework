from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('online_customer', 'Online Customer'),
        ('driver', 'Delivery Driver'),
        ('admin', 'Admin Staff'),]

    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(
        max_length=25,
        choices=ROLE_CHOICES,
        default='online_customer')
    def __str__(self):
        return self.email

class UserAddress(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='addresses' )
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "User Addresses"
    def __str__(self):
        return f"{self.address_line_1}, {self.city}"