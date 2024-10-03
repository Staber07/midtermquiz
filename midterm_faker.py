
from faker import Faker



# Create a Faker instance

fake = Faker()



# Generate and print 10 fake names, emails, and phone numbers

for _ in range(10):

    print(f"Name: {fake.name()}, Email: {fake.email()}, Phone Number: {fake.phone_number()}")