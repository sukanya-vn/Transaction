#from django.db import models

# Create your models here.
#from django.db import models

import myapp.converter as converter
# Create your models here.

from django.db import models
# Creating the Transaction table to store each transaction entry
class Transaction(models.Model):

   Tran_id = models.IntegerField(default=2)
   src_currency = models.CharField(max_length = 3,default='AUD')
   dest_currency = models.CharField(max_length = 3,default='EUR')
   src_amount = models.FloatField(default=0)
   dest_amount = models.FloatField(default=0)

# Function to store transaction details
def crudops(Trans_id,src_currency,dest_currency,src_amount,dest_amount):
   # Creating an entry

   transaction = Transaction(Tran_id=Trans_id, src_currency=src_currency,
                       dest_currency=dest_currency, src_amount=src_amount, dest_amount=dest_amount)

   transaction.save()

# calling crudops to store each entry in Transaction table
trans_data = converter.convert()
for i in trans_data:
    Trans_id = i[0]
    src_currency = i[1]
    dest_currency = i[2]
    src_amount = i[3]
    dest_amount = i[4]
    crudops(Trans_id,src_currency,dest_currency,src_amount,dest_amount)