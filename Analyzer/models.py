from django.db import models

# Create your models here.

class user_profile(models.Model):
    Email=models.EmailField(max_length=264, primary_key=True)
    FirstName=models.CharField(max_length=264)
    LastName=models.CharField(max_length=264)
    Password=models.CharField(max_length=264)
    PhoneNo=models.IntegerField()
    Wallet=models.IntegerField()
    frequent_wallet_addition_amount=models.IntegerField()
    amount_to_be_added=models.IntegerField()

    def __str__(self):
        return self.name

class general_expenses(models.Model):
    T_id=models.IntegerField(primary_key=True)
    Email=models.ForeignKey(user_profile,  on_delete=models.CASCADE,)
    amount=models.IntegerField()
    categories=(
    (1,'Food9'),
    (2,'Travel'),
    (3,'Groceries'),
    (4, 'Electronics'),
    (5,'Clothing or Footwear'),
    (6, 'Household shopping'),
    (7, 'Other- specify in remarks'),
    )
    category=models.IntegerField(choices=categories)
    remarks=models.CharField(max_length=264)

    def __str__(self):
        return self.name

class mandatory_expenses(models.Model):
    T_id=models.IntegerField(primary_key=True)
    Email=models.ForeignKey(user_profile, on_delete=models.CASCADE,)
    amount=models.IntegerField()
    categories=(
    (1,'Food9'),
    (2,'Travel'),
    (3,'Groceries'),
    (4, 'Electronics'),
    (5,'Clothing or Footwear'),
    (6, 'Household shopping'),
    (7, 'Other- specify in remarks'),
    )
    category=models.IntegerField(choices=categories)
    remarks=models.CharField(max_length=264)
    def __str__(self):
        return self.name

class debts(models.Model):
    T_id=models.IntegerField(primary_key=True)
    Email=models.ForeignKey(user_profile,  on_delete=models.CASCADE,)
    amount=models.IntegerField()
    reciever=models.CharField(max_length=264)
    remarks=models.CharField(max_length=264)
    Deadline=models.DateField()
    def __str__(self):
        return self.name
