from django.db import models

class Investment(models.Model):
    # Field for storing the name of the member
    member_name = models.CharField(max_length=100)

    # Field for storing the member's CPM (student registration number)
    member_cpm = models.CharField(max_length=10)

    # Field for storing the investment amount with a decimal format
    investment = models.DecimalField(max_digits=10, decimal_places=2)

    # Field for storing the date of the investment; auto-filled with the current date when a new investment is created
    date = models.DateField(auto_now_add=True)

    # String representation of the model instance
    def __str__(self):
        # Return a formatted string displaying the member's name and investment amount
        return f"{self.member_name} - {self.investment}"
