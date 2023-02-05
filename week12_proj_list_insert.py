# Create a new empty list:
services = []

# Populate the new list using insert
services.insert(0, "S3")
services.insert(1, "Lambda")
services.insert(2, "EC2")
services.insert(3, "RDS")
services.insert(4, "DynamoDB")

# Print the list and the length of the list
print("Services:", services)
print("Length of the list:", len(services))

# Remove two specific services by name
services.remove("Lambda")
services.remove("EC2")

# Print the new list and the new length of the list
print("Updated services:", services)
print("New length of the list:", len(services))
