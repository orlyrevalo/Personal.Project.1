
employee_file = open("employee.txt", "r")
print(employee_file.readable())
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readlines())
employee_file.close()

print("==============================================================================")
employee_file = open("employee.txt","r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()
