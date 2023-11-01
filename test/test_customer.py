#!/usr/bin/python3

# import unittest
# from customer import Customer

# class TestCustomer(unittest.TestCase):

#     def setUp(self):
#         self.customer1 = Customer('John', 'Brad', 5000)
#         self.customer2 = Customer('Tina', 'Smith', 3000)

#     def test_customer_mail(self):
#         self.assertEqual(self.customer1.customer_mail, 'John.Brad@gmail.com')
#         self.assertEqual(self.customer2.customer_mail, 'Tina.Smith@gmail.com')

#     def test_fullname(self):
#         self.assertEqual(self.customer1.customer_fullname, 'John Brad')
#         self.assertEqual(self.customer2.customer_fullname, 'Tina Smith')

#     def test_apply_discount(self):
#         self.customer1.apply_discount()
#         self.customer2.apply_discount()


#         self.assertEqual(self.customer1.purchase, 4750)
#         self.assertEqual(self.customer2.purchase, 2850)

    

# if __name__ == '__main__':
#     unittest.main()

''' Using doctest'''
import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):
    """
    Test cases for the Customer class.
    """

    def setUp(self):
        """
        Set up common fixtures and initialize Customer instances for testing.
        """
        self.customer_1 = Customer('John', 'Brad', 5000)
        self.customer_2 = Customer('Tina', 'Smith', 3000)

    def test_customer_mail(self):
        """
        Test the correctness of the customer_mail property.

        Examples:
        >>> customer = Customer('John', 'Brad', 0)
        >>> customer.customer_mail
        'John.Brad@email.com'
        """
        self.assertEqual(self.customer_1.customer_mail, 'John.Brad@email.com')
        self.assertEqual(self.customer_2.customer_mail, 'Tina.Smith@email.com')

    def test_customer_fullname(self):
        """
        Test the correctness of the customer_fullname property.

        Examples:
        >>> customer = Customer('Tina', 'Smith', 0)
        >>> customer.customer_fullname
        'Tina Smith'
        """
        self.assertEqual(self.customer_1.customer_fullname, 'John Brad')
        self.assertEqual(self.customer_2.customer_fullname, 'Tina Smith')

    def test_apply_discount(self):
        """
        Test the apply_discount method.

        Examples:
        >>> customer = Customer('Sam', 'Wilson', 100)
        >>> customer.apply_discount()
        >>> customer.purchase
        95
        """
        self.customer_1.apply_discount()
        self.customer_2.apply_discount()

        self.assertEqual(self.customer_1.purchase, 4750)
        self.assertEqual(self.customer_2.purchase, 2850)
