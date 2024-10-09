from django.db import models


# Create your models here.
class fun(models.Model):
    fno = models.DecimalField(max_digits=10, decimal_places=3)
    lno = models.DecimalField(max_digits=10, decimal_places=3)
    operands = models.CharField(max_length=20, default='Select the operand')

    def __str__(self):
        return self.operands


class invest(models.Model):
    start_amount = models.DecimalField(max_digits=6, decimal_places=2)
    no_yor = models.PositiveIntegerField()
    rate = models.DecimalField(max_digits=3, decimal_places=3)
    add_cont = models.DecimalField(max_digits=6, decimal_places=2)


