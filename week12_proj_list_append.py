# Create an empty list:
services = []

# Print the list and the length of the list
print("List of Services:", services)
print("Length of the List:", len(services))

# Populate the list using "append"
services.append("S3")
services.append("Lambda")
services.append("EC2")
services.append("DynamoDB")

# Print the list and the length of the list
print("Original List of Services: ", services)
print("Original Length of the List: ", len(services))

# Remove 2 of the items
services.remove("S3")
services.remove("EC2")

# Print the new list and the new length
print("Updated List of Services: ", services)
print("Updated Length of the List: ", len(services))