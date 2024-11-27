from mydjangoproject import models

# Create your models here.
class Customer(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
#The Customer model represents each individual with a unique email.


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name='orders')
    order_date =  models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"
#The Order model links Customer using ForeignKey,enabling customer to make multiple orders.
# on_delete=models.CASCADE ensures that all records are deleted on exiting of a customer to ensure privacy.
