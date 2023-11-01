#!/usr/bin/python3
# '''Working with unittest'''


# class Customer:
#     '''A sample of customer class'''


#     discount = 0.95


#     def __init__(self, first_name, last_name, purchase):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.purchase = purchase

#     @property
#     def customer_mail(self):
#         return f"{self.first_name}.{self.last_name}@gmail.com"
    
#     @property
#     def customer_fullname(self):
#         return f"{self.first_name} {self.last_name}"
    
#     def apply_discount(self):
#         self.purchase = int(self.purchase * self.discount)

'''Working with Doctest'''
class Customer:
    """
    A sample customer class.

    Attributes:
        discount (float): A class attribute representing the discount rate for customers.
    """

    discount = 0.95

    def __init__(self, first_name, last_name, purchase):
        """
        Initializes a Customer instance.

        Args:
            first_name (str): The first name of the customer.
            last_name (str): The last name of the customer.
            purchase (float): The purchase amount made by the customer.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.purchase = purchase

    @property
    def customer_mail(self):
        """
        Generates the customer's email address.

        Returns:
            str: The customer's email address.

        Examples:
        >>> customer = Customer('John', 'Doe', 0)
        >>> customer.customer_mail
        'John.Doe@email.com'
        """
        return f'{self.first_name}.{self.last_name}@email.com'

    @property
    def customer_fullname(self):
        """
        Generates the customer's full name.

        Returns:
            str: The customer's full name.

        Examples:
        >>> customer = Customer('Alice', 'Smith', 0)
        >>> customer.customer_fullname
        'Alice Smith'
        """
        return f'{self.first_name} {self.last_name}'

    def apply_discount(self):
        """
        Applies the discount to the purchase amount.

        Examples:
        >>> customer = Customer('Bob', 'Johnson', 100)
        >>> customer.apply_discount()
        >>> customer.purchase
        95
        """
        self.purchase = int(self.purchase * self.discount)
