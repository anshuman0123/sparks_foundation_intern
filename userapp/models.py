from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=200)
    curr_balance=models.IntegerField()
    email=models.EmailField(max_length=200,unique=True)

# class Transfer(models.Model):
#     fromuser=models.ForeignKey(Customer,on_delete=models.CASCADE)
#     touser=models.ForeignKey(Customer,on_delete=models.CASCADE)
#     dateoftrans=models.DateTimeField(auto_now_add=True)
class Transfer(models.Model):
    fromuser=models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='outgoing_transfers')
    touser=models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='incoming_transfers')
    amount=models.DecimalField(decimal_places=2,max_digits=11)
    dateoftrans=models.DateTimeField(auto_now_add=True)
