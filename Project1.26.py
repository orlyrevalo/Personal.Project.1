

employee_file = open("employees.txt", "w")
employee_file.write("\nKelly - Customer Service")
employee_file.close()

employee_file = open("employees.txt", "a")
employee_file.write("\nToby - Human Resources")
employee_file.write("\nKelly - Customer Service")
employee_file.close()

employee_file = open("employees.txt", "a")
employee_file.write("\nJim - Salesman\nDwight - Salesman\nPam - Receptionist\nMichael - Manager\nOscar - Accountant")
employee_file.write("\nToby - Human Resources")
employee_file.write("\nKelly - Customer Service")
employee_file.close()
