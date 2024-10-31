"""
In this program we show an example of using dictionaries to keep track of information in a phonebook.
"""
phonebook = {}

def add_contact():
  """Adds a new contact to the phonebook."""
  name = input("Enter the name of the contact: ")
  number = input("Enter the phone number: ")
  phonebook[name] = number
  print(f"Contact {name} added successfully!")

def search_contact():
  """Searches for a contact in the phonebook."""
  name = input("Enter the name of the contact to search: ")
  if name in phonebook:
    print(f"The phone number for {name} is {phonebook[name]}")
  else:
    print(f"Contact {name} not found in the phonebook.")

def delete_contact():
  """Deletes a contact from the phonebook."""
  name = input("Enter the name of the contact to delete: ")
  if name in phonebook:
    del phonebook[name]
    print(f"Contact {name} deleted successfully!")
  else:
    print(f"Contact {name} not found in the phonebook.")

def display_contacts():
  """Displays all contacts in the phonebook."""
  if not phonebook:
    print("The phonebook is empty.")
  else:
    print("Contacts in the phonebook:")
    for name, number in phonebook.items():
      print(f"{name}: {number}")

while True:
  print("\nPhonebook Menu:")
  print("1. Add a contact")
  print("2. Search for a contact")
  print("3. Delete a contact")
  print("4. Display all contacts")
  print("5. Exit")

  choice = input("Enter your choice (1-5): ")

  if choice == '1':
    add_contact()
  elif choice == '2':
    search_contact()
  elif choice == '3':
    delete_contact()
  elif choice == '4':
    display_contacts()
  elif choice == '5':
    break
  else:
    print("Invalid choice. Please try again.")

print("Thank you for using the phonebook!")
