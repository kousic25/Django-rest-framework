from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='reviews')
    menu_item_id = models.UUIDField(db_index=True) 
    order_id = models.UUIDField(null=True, blank=True) 
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('user', 'menu_item_id')
    def __str__(self):
        return f"{self.rating} Stars - Item {self.menu_item_id} by {self.user}"