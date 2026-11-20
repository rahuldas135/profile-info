from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def illustration(self):
        name = self.name.casefold()
        if "tote" in name or "carry" in name:
            return "tote"
        if "candle" in name:
            return "candle"
        if "mug" in name or "cup" in name or "ceramic" in name and "vase" not in name:
            return "mug"
        if "bottle" in name or "flask" in name:
            return "bottle"
        if "planter" in name or "plant" in name:
            return "plant"
        if "notebook" in name or "journal" in name:
            return "book"
        if "bowl" in name:
            return "bowl"
        if "soap" in name:
            return "soap"
        if "runner" in name or "linen" in name:
            return "linen"
        return "vase"

    @property
    def photo_url(self):
        name = self.name.casefold()
        if "sunday ceramic" in name:
            photo = "sunday-ceramic.jpg"
        elif "cloud stoneware" in name:
            photo = "mug-cloud.jpg"
        elif "espresso cup" in name:
            photo = "mug-espresso.jpg"
        elif "tote" in name or "carry" in name:
            photo = "tote.jpg"
        elif "candle" in name:
            photo = "candle.jpg"
        elif "flask" in name or "bottle" in name:
            photo = "bottle.jpg"
        elif "little leaf" in name:
            photo = "planter-green.jpg"
        elif "planter" in name or "plant" in name:
            photo = "planter.jpg"
        elif "notebook" in name or "journal" in name:
            photo = "journal.jpg"
        elif "bowl" in name:
            photo = "bowl.jpg"
        elif "soap" in name:
            photo = "soap.jpg"
        elif "runner" in name or "linen" in name:
            photo = "linen.jpg"
        else:
            photo = "vase.jpg"
        return f"store/products/{photo}"
