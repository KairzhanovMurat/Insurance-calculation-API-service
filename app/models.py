from tortoise import models, fields
from datetime import date


class Tariff(models.Model):
    id = fields.IntField(pk=True)
    cargo_type = fields.CharField(30)
    rate = fields.DecimalField(max_digits=4, decimal_places=3)
    date = fields.DateField(default=date.today())

    def __str__(self):
        return self.cargo_type
