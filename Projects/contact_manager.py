# CONTACT MANAGER

print('Welcome to the contact manager!'.title())

class Contact:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        names = input('Enter name of your contact: ').title()
        phone_numbers = input('Enter phone number of your contact: ')
        email_address = input('Enter email address of your contact: ')
        self.contacts[names] = (phone_numbers, email_address)
    def delete_contact(self):
        option = input('Enter name of contact you would like to delete: ')
        if option in self.contacts:
            del self.contacts[option]
            print('{} has been removed from contacts'.format(option))
        else:
            print('Contact Not Found')
    def view_contacts(self):
        for name, (phone, email) in self.contacts.items():
            print('Name: {}|, Email: {}|, Phone: {}'.format(name, email, phone))

    def search_contacts(self):
        option = input('Enter name of contact you would like to search: ')
        if option in self.contacts:
            print(self.contacts[option])
        else:
            print('No contact under the name of {}'.format(option))

manager = Contact()
while True:
    choice = input('Enter 1 to add contact, 2 to view contacts, 3 to search for contact, 4 to delete contact, or 5 to exit: ')
    if choice == '1':
        manager.add_contact()
    elif choice == '2':
        manager.view_contacts()
    elif choice == '3':
        manager.search_contacts()
    elif choice == '4':
        manager.delete_contact()
    elif choice == '5':
        print('Goodbye!')
        break
    else:
        continue





