from faker import Faker





fake = Faker()





for _ in range(10):

    print(f"Name: {fake.name()}, Email: {fake.email()}, Phone Number: {fake.phone_number()}")
