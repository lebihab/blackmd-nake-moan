import random
import string

# Number of EC2 instances
num_instances = int(input("Enter the number of EC2 instances: "))

# Department name
department_name = input("Enter your department name: ")

# Generate unique names for the specified number of instances
for i in range(num_instances):
    # Generate random characters and numbers to include in the name
    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    # Create the unique name
    unique_name = department_name + '-' + random_chars
    print(unique_name)