from sortedcontainers import SortedDict

class Contact:

    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email



class ContactList:

    def __init__(self):
        self.contact_map = {}
        self.name_map = SortedDict()
        self.phone_map = {}
        self.email_map = {}
        self.contact_id = 0
        self.queue = []
        self.max_size = 5
    

    def add_contact(self, name, phone, email):
        if len(self.contact_map) == self.max_size:
            self.queue.append(Contact(name, phone, email))

        self.contact_id +=1 
        self.contact_map[self.contact_id] = Contact(name, phone, email)
        self.name_map[name] = self.contact_id
        self.phone_map[phone] = self.contact_id
        self.email_map[email] = self.contact_id
    

    def get_by_name(self, name):
        id = self.name_map[name]
        return self.contact_map[id]
    
    def get_by_phone(self, phone):
        id = self.phone_map[phone]
        return self.contact_map[id]
    
    def get_by_email(self, email):
        id = self.email_map[email]
        return self.contact_map[id]
    
    def get_by_id(self, id):
        return self.contact_map[id]


    def remove(self, id):
        contact = self.contact_map[id]
        del self.name_map[contact.name]
        del self.phone_map[contact.phone]
        del self.email_map[contact.email]
        del self.contact_map[id]

        if self.queue != []:
            contact = self.queue[0]
            self.contact_id +=1 
            self.contact_map[self.contact_id] = contact
            self.name_map[contact.name] = self.contact_id
            self.phone_map[contact.phone] = self.contact_id
            self.email_map[contact.email] = self.contact_id
            self.queue = self.queue[1:]
            print('The first contact from the queue has been added')
    

    def get_contacts_ordered_by_name(self):
        ordered_contact_list = []
        for name in self.name_map:
            id = self.name_map[name]
            ordered_contact_list.append(self.contact_map[id])
        
        return ordered_contact_list

        

if __name__ == '__main__':
    contact_list = ContactList()
    contact_list.add_contact('Hanna Hönnudóttir', '1234567', 'hanna@hanna.is')
    contact_list.add_contact('Jón Jónsson', '2345678', 'jon@jon.is')
    contact_list.add_contact('Anna Önnudóttir', '3456789', 'anna@anna.is')
    contact_list.add_contact('Guðmundur Guðmundsson', '4567890', 'gummi@gummi.is')
    contact_list.add_contact('Bryndís Bryndísardóttir', '0123456', 'disa@disa.is')
    some_contact_1 = contact_list.get_by_name('Anna Önnudóttir')
    some_contact_2 = contact_list.get_by_phone('4567890')
    some_contact_3 = contact_list.get_by_email('hanna@hanna.is')
    ordered_contact_list = contact_list.get_contacts_ordered_by_name()

    for contact in ordered_contact_list:
        print(contact.name)
