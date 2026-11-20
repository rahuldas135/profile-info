from django.core.management.base import BaseCommand

from store.models import Product


class Command(BaseCommand):
    help = "Create 20 example products for the storefront."

    def handle(self, *args, **options):
        products = [
            {"name": "Sunday Ceramic", "description": "A hand-finished cup for slow mornings and second coffees.", "price": "890.00", "stock": 12},
            {"name": "Daily Carry Tote", "description": "A sturdy, soft cotton tote for all the little things.", "price": "1250.00", "stock": 8},
            {"name": "Evening Glow Candle", "description": "Warm cedar and citrus, poured for the end of the day.", "price": "690.00", "stock": 15},
            {"name": "Sculpted Bud Vase", "description": "A softly sculpted stoneware vase for a single stem.", "price": "1450.00", "stock": 7},
            {"name": "Cloud Stoneware Mug", "description": "A generous, easy-grip mug finished in a milky glaze.", "price": "760.00", "stock": 18},
            {"name": "Cedar Travel Flask", "description": "A double-wall steel flask that keeps your drink close.", "price": "1690.00", "stock": 10},
            {"name": "Pocket Garden Planter", "description": "A small ceramic home for your favourite little green.", "price": "980.00", "stock": 9},
            {"name": "Sunday Reading Journal", "description": "An unhurried place for notes, lists, and passing thoughts.", "price": "540.00", "stock": 24},
            {"name": "Olive Serving Bowl", "description": "A tactile serving bowl for shared tables and everyday fruit.", "price": "1180.00", "stock": 11},
            {"name": "Terra Bud Vase", "description": "A warm-toned sculptural vase with a hand-brushed finish.", "price": "1320.00", "stock": 6},
            {"name": "Market Day Tote", "description": "A roomy reusable carryall with comfortable cotton handles.", "price": "1390.00", "stock": 13},
            {"name": "Quiet Hours Candle", "description": "Soft amber and sandalwood for a calm evening ritual.", "price": "820.00", "stock": 17},
            {"name": "Pebble Espresso Cup", "description": "A petite, palm-sized cup with a smooth satin glaze.", "price": "620.00", "stock": 20},
            {"name": "Coastline Water Bottle", "description": "A lightweight insulated bottle for everyday refills.", "price": "1540.00", "stock": 8},
            {"name": "Little Leaf Planter", "description": "A cheerful ceramic planter with a softly rounded silhouette.", "price": "890.00", "stock": 14},
            {"name": "Field Notes Notebook", "description": "A lay-flat notebook with thick, fountain-pen friendly pages.", "price": "480.00", "stock": 30},
            {"name": "Gather Salad Bowl", "description": "A broad, gently curved bowl made for passing around.", "price": "1890.00", "stock": 5},
            {"name": "Studio Flower Vase", "description": "A sculptural centrepiece with a naturally textured finish.", "price": "2100.00", "stock": 4},
            {"name": "Rosemary Hand Soap", "description": "A gentle, plant-based soap with a fresh garden scent.", "price": "390.00", "stock": 22},
            {"name": "Linen Table Runner", "description": "Soft washed linen that makes weeknight dinners feel special.", "price": "1590.00", "stock": 7},
        ]
        created_count = 0
        for values in products:
            _, created = Product.objects.get_or_create(name=values["name"], defaults=values)
            created_count += int(created)
        self.stdout.write(self.style.SUCCESS(f"Seeded products. Created {created_count}; existing examples were left unchanged."))
