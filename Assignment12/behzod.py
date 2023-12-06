import re
#IN BO ZABONI TOJIKI
contacts = dict()

print('Choose operation: \n1. add \n2. edit \n3. view \n4. delete \n5. all \n0. exit')

while True:
    operation = input('Enter operation number or name: ')


    def add_contact():
        name = input('Nomro vorid kuned: ')
        if name.lower() in contacts:
            print('in nom vujud dorad !')
        else:
            number = input('Raqami hudro vorid kuned: ')
            if validate_number(number):
                if is_unique(number):
                    contacts[name.lower()] = number
                    print('Bo muvafaqiyat doxil karda shud!') 
                else:
                    print('raqam vujud dorad!')
            else:
                print('Bo chunin tarz vorid kuned: nn-nnn-nn-nn')


    def view_contact():
        name = input('Nomro vorid kuned: ')
        if contacts.get(name.lower()):
            print(f"Name: {name.capitalize()} \nNumber: {contacts[name.lower()]}")
        else:
            print(f'In {name} vujud nadorad!')


    def edit_contact():
        if not len(contacts):
            print('Injo holi ast!')
        else:
            name = input('Enter name: ')
            if contacts.get(name.lower()):
                number = (input('Enter number: '))
                if is_unique(number) and validate_number(number):
                    contacts[name.lower()] = number
                    print(f'{name} Bo muvaqiyat vorid shud!')
                else:
                    print('Xatogi dar rafti kor')
            else:
                print(f' {name} Vujud nadorad!')


    def delete_contact():
        if not len(contacts):
            print('injo xoli ast!')
        else:
            name = input('Enter name: ')
            if contacts.get(name.lower()):
                contacts.pop(name.lower())
                print(f' {name} bo muvafaqiyat toza shud!!')
            else:
                print(f' {name} Vujud nadorad!')


    def view_all():
        if not len(contacts):
            print(' Vujud nadorad!')
        else:
            counter = 1
            for name, value in contacts.items():
                print(f"{counter}. Name: {name.capitalize()} \n   Number: {value}")
                counter += 1


    def validate_number(number):
        pattern = re.compile(r'\d{2}-\d{3}-\d{2}-\d{2}')
        if pattern.match(number):
            return True
        else:
            return False

    def is_unique(number):
        for i in contacts.values():
            if i == number:
                return False
        return True


    if operation in ['add', '1']:
        add_contact()
    elif operation in ['edit', '2']:
        edit_contact()
    elif operation in ['delete', '4']:
        delete_contact()
    elif operation in ['view', '3']:
        view_contact()
    elif operation in ['all', '5']:
        view_all()
    elif operation in ['exit', 'break', 'quit', '0']:
        break
    else:
        print('This kind of operation not found!')