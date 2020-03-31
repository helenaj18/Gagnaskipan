from enum import Enum

class OperationType(Enum):
    ADD = 1
    UPDATE = 2
    DELETE = 3

class OperationInfo:
    def __init__(self, type, data):
        self.type = type
        self.data = data



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
        self.stack = []
    

    def add_contact(self, name, phone, email):
        self.contact_id +=1 
        self.contact_map[self.contact_id] = Contact(name, phone, email)
        self.name_map[name] = self.contact_id
        self.phone_map[phone] = self.contact_id
        self.email_map[email] = self.contact_id
        info = OperationInfo(OperationType.ADD, (name,phone,email))
        self.stack.append(info)
    

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
        info = OperationInfo(OperationType.DELETE, id)
        self.stack.append(info)
        del self.name_map[contact.name]
        del self.phone_map[contact.phone]
        del self.email_map[contact.email]
        del self.contact_map[id]
        
    

    def get_contacts_ordered_by_name(self):
        ordered_contact_list = []
        for name in self.name_map:
            id = self.name_map[name]
            ordered_contact_list.append(self.contact_map[id])
        
        return ordered_contact_list



    def undo(self):
        some_info = self.stack.pop()

        if some_info.type == OperationType.DELETE:
            self.add_contact(some_info.data[0], some_info.data[1], some_info.data[2])
        elif some_info.type == OperationType.ADD:
            self.remove(some_info.data)