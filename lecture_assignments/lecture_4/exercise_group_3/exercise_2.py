data_list = [{'email': 'johan@gmail.com', 'is_board_member': False}, {'email': 'fredrik@gmail.com', 'is_board_member': True}, {'email': 'johanna@gmail.com', 'is_board_member': True},  ]

class EmployeeHandler():

    def __init__(self, employee_list):
        self.employee_list = employee_list

    def send_mail_to_board_members(self):
        for person in self.employee_list:
            if person.get('is_board_member') == True:
                email_address = person.get('email')
                self.send_mail(email_address)

    def send_mail(self, email_address):
        print('Sent mail to', email_address)


handler = EmployeeHandler(data_list)
handler.send_mail_to_board_members()



