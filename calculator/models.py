from django.db import models


# Create your models here.
class fun(models.Model):
    fno = models.DecimalField(max_digits=10, decimal_places=3)
    lno = models.DecimalField(max_digits=10, decimal_places=3)
    operands = models.CharField(max_length=20, default='Select the operand')

    def __str__(self):
        return self.operands
