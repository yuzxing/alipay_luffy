from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()


class Order(models.Model):
    no = models.CharField(max_length=64)  # 订单号
    goods = models.ForeignKey(to='Goods')  # 和物品关联
    status_choices = (
        (1, '未支付'),
        (2, '已支付'),
    )
    status = models.IntegerField(choices=status_choices, default=1)
