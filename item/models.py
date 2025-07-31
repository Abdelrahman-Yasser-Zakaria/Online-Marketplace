from django.db import models  # type: ignore
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    CONDITION_NEW = "New"
    CONDITION_USED_LIKE_NEW = "Used - Like new"
    CONDITION_USED_GOOD = "Used - Good"
    CONDITION_USED_FAIR = "Used - Fair"

    CONDITION_CHOISES = [
        (CONDITION_NEW, "New"),
        (CONDITION_USED_LIKE_NEW, "Used - Like new"),
        (CONDITION_USED_GOOD, "Used - Good"),
        (CONDITION_USED_FAIR, "Used - Fair"),
    ]

    condition = models.CharField(
        max_length=20, choices=CONDITION_CHOISES, default=CONDITION_NEW
    )
    category = models.ForeignKey(
        Category, related_name="items", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    location = models.CharField(
        max_length=255,
        default="Cairo, Egypt",
    )
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ("name",)

    @property
    def all_images(self):
        """Retrieve all images related to specific item from ItemImage model"""
        images = []
        if self.images.exists():
            for img in self.images.all():
                images.append(img.image)
        return images

    @property
    def main_image(self):
        """Retrieve the first image related to specific item from ItemImage model"""
        if self.images.exists():
            return self.images.first().image

        return None

    def __str__(self) -> str:
        return self.name


class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="item_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        return f"image for {self.item.name}"
