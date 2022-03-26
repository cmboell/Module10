"""
Assignment name: Basic Input and Format Output Assignment
Program: employee.py
Author: Colby Boell
Last date modified: 03/26/2022

The purpose of this program is to create a class to use encapsulation. We define a user class
and use a display method to show the results of the employees we created using the employee
class.
"""
# import
from datetime import datetime


class Employee:
    def __init__(self, last_name, first_name, address, phone_number, salaried, start_date, salary):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.phone_number = phone_number
        self.salaried = salaried
        dateformat = datetime.strptime(start_date, '%m-%d-%Y')
        self.start_date = dateformat.strftime('%m-%d-%Y')
        self.salary = salary

    def display(self):
        if self.salaried is True:
            return f'{str(self.first_name)} {str(self.last_name)}\n{str(self.phone_number)}\n{str(self.address)}\nSalaried Employee: $' + '%.2f' % float(self.salary) + '/year\nStart Date: ' + self.start_date
        return f'{str(self.first_name)} {str(self.last_name)}\n{str(self.phone_number)}\n{str(self.address)}\nHourly Employee: $' + '%.2f' % float(self.salary) + '/hour\nStart Date: ' + self.start_date


# Driver
if __name__ == "__main__":
    emp = Employee('Patel', 'Sasha', '123 Main St\nUrban, Iowa', '111-222-3333', True, '06-28-2019', 40000)  # call the constructor
    emp2 = Employee('Boell', 'Colby', '189 Main St\nUrban, Iowa', '111-222-3334', False, '12-15-2019', 22.52)
    print(emp.display())                # display returns a str, so print the information
    print(emp2.display())

"""
Results:
Sasha Patel
111-222-3333
123 Main St
Urban, Iowa
Salaried Employee: $40000.00/year
Start Date: 06-28-2019
Colby Boell
111-222-3334
189 Main St
Urban, Iowa
Hourly Employee: $22.52/hour
Start Date: 12-15-2019

"""

