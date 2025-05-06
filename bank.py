# class BankAccount:
#     def __init__(self, account_number, account_holder):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = 0.0

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             return f"Deposited ${amount} successfully."
#         return "Deposit amount must be greater than zero."

#     def withdraw(self, amount):
#         if amount <= 0:
#             return "Withdrawal amount must be greater than zero."
#         if amount > self.balance:
#             return "Insufficient balance."
#         self.balance -= amount
#         return f"Withdrawn ${amount} successfully."

#     def get_details(self):
#         return {
#             "Account Number": self.account_number,
#             "Account Holder": self.account_holder,
#             "Balance": self.balance
#         }


# class BankSystem:
#     def __init__(self):
#         self.accounts = {}

#     def create_account(self, account_number, holder_name):
#         if account_number in self.accounts:
#             return "Account already exists!"
#         self.accounts[account_number] = BankAccount(account_number, holder_name)
#         return "Account created successfully."

#     def deposit_to_account(self, account_number, amount):
#         account = self.accounts.get(account_number)
#         if account:
#             return account.deposit(amount)
#         return "Account not found."

#     def withdraw_from_account(self, account_number, amount):
#         account = self.accounts.get(account_number)
#         if account:
#             return account.withdraw(amount)
#         return "Account not found."

#     def show_account_details(self, account_number):
#         account = self.accounts.get(account_number)
#         if account:
#             details = account.get_details()
#             print("\n----- Account Details -----")
#             for key, value in details.items():
#                 print(f"{key}: {value}")
#             print("---------------------------")
#         else:
#             print("Account not found.")


# # Main interaction
# bank = BankSystem()

# while True:
#     print("\n=== Bank Menu ===")
#     print("1. Create Account")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Show Account Details")
#     print("5. Exit")

#     choice = input("Select an option: ")

#     if choice == "1":
#         acc_no = input("Enter Account Number: ")
#         name = input("Enter Account Holder Name: ")
#         print(bank.create_account(acc_no, name))

#     elif choice == "2":
#         acc_no = input("Enter Account Number: ")
#         amt = float(input("Enter amount to deposit: "))
#         print(bank.deposit_to_account(acc_no, amt))

#     elif choice == "3":
#         acc_no = input("Enter Account Number: ")
#         amt = float(input("Enter amount to withdraw: "))
#         print(bank.withdraw_from_account(acc_no, amt))

#     elif choice == "4":
#         acc_no = input("Enter Account Number: ")
#         bank.show_account_details(acc_no)

#     elif choice == "5":
#         print("Thank you for using the Bank Management System.")
#         break

#     else:
#         print("Invalid choice. Try again.")


# class Person:
#     def __init__(self, name, age):
#         self.__name = name     # private
#         self.__age = age       # private

#     def get_info(self):
#         return f"{self.__name} is {self.__age} years old."

# p = Person("Ali", 25)
# print(p.get_info())




# from abc import ABC, abstractmethod

# class Animal(ABC):  # Abstract Base Class
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         print("Woof!")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")

# # You cannot create an object of abstract class
# # animal = Animal()  ❌

# dog = Dog()
# cat = Cat()
# dog.make_sound()  # Woof!
# cat.make_sound()  # Meow!



# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

#     def start(self):
#         print(f"{self.brand} vehicle started.")

# class Car(Vehicle):
#     def open_doors(self):
#         print("Car doors opened.")

# c = Car("Honda")
# c.start()         # Inherited from Vehicle
# c.open_doors()    # Specific to Car


# class Bird:
#     def speak(self):
#         print("Chirp")

# class Parrot(Bird):
#     def speak(self):
#         print("Squawk")

# class Sparrow(Bird):
#     def speak(self):
#         print("Tweet")

# def make_bird_speak(bird):
#     bird.speak()

# make_bird_speak(Parrot())   # Squawk
# make_bird_speak(Sparrow())  # Tweet
# make_bird_speak(Bird())  # Tweet





from abc import ABC, abstractmethod

# Abstraction
class Person(ABC):
    def __init__(self, name, age):
        self.__name = name       # Encapsulation
        self.__age = age

    @abstractmethod
    def show_info(self):
        pass

    # Encapsulated getter
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


# Inheritance + Polymorphism
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = student_id

    def show_info(self):
        print(f"Student: {self.get_name()}, Age: {self.get_age()}, ID: {self.__student_id}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.__subject = subject

    def show_info(self):
        print(f"Teacher: {self.get_name()}, Age: {self.get_age()}, Teaches: {self.__subject}")


# Main function to test
def main():
    people = []

    while True:
        print("\n1. Add Student")
        print("2. Add Teacher")
        print("3. Show All People")
        print("4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter age: "))
            sid = input("Enter student ID: ")
            people.append(Student(name, age, sid))

        elif choice == "2":
            name = input("Enter teacher name: ")
            age = int(input("Enter age: "))
            subject = input("Enter subject: ")
            people.append(Teacher(name, age, subject))

        elif choice == "3":
            if not people:
                print("No records found.")
            for person in people:
                person.show_info()  # Polymorphism in action

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

main()
