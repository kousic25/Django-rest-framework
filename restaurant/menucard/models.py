from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="items" )
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    image_url = models.URLField(blank=True, null=True)
    def __str__(self):
        return f"{self.name} (₹{self.price})"

class MenuItemOption(models.Model):
    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE,
        related_name="options")
    option_name = models.CharField(max_length=100)
    additional_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0.00)

    def __str__(self):
        return f"{self.option_name} (+₹{self.additional_price})"