# Appointment table
'''
class Table:
    def __init__(self):
        self.table = []

    def get_info_from_file(self):
        self.file = open("appointments", "r")
        if self.file.mode == "r":
            for i in range(9):
                content = self.file.readline()
                row = content.split(" | ")
                self.table.append(row)
        self.file.close()

    def transform_items(self):
        # This will transform to integer some values of the table.
        # And clean the string items if they have an special character.
        for row in self.table:
            row[0] = int(row[0])
            row[1] = int(row[1])
            row[3] = int(row[3])
            if row[2] != 'NULL':
                row[2] = int(row[2])

            row[6] = row[6].rstrip('\n')

    def create_document(self):
        self.file = open("AppointmentValues", "w")
        table_name = input("What's the exact name of your table? ")
        self.file.write(f"INSERT INTO {table_name}\nVALUES\n")
        for entry in self.table:
            self.file.write(f"({entry[0]}, {entry[1]}, {entry[2]}, {entry[3]}, '{entry[4]}', '{entry[5]}', '{entry[6]}'),\n")

        self.file.close()

appointments = Table()
appointments.get_info_from_file()
appointments.transform_items()
appointments.create_document()

#-----------------------------------------------------------------------------------------------------------------------------
#Physician table
class Physician:
    def __init__(self):
        self.physician = []

    def add_from_file(self):
        self.file = open("physician", "r")
        if self.file.mode == "r":
            for i in range(10):
                content = self.file.readline()
                row = content.split(" | ")
                self.physician.append(row)
        self.physician.pop() #Because of the last inexpected element
        self.file.close()

    def modifying_datatypes(self):
        for entry in self.physician:
            entry[0] = int(entry[0])
            entry[3] = int(entry[3])

        for entry in self.physician:
           print(entry)

    def create_document_queries(self):
        self.file = open("PhysicianValues", "w")
        self.file.write("INSERT INTO physician\nVALUES\n")

        for entry in self.physician:
            self.file.write(f"({entry[0]}, '{entry[1]}', '{entry[2]}', {entry[3]}),\n")

        self.file.close()

    def print_queries(self):
        print("INSERT INTO physician\nVALUES")
        for entry in self.physician:
            print(f"({entry[0]}, '{entry[1]}', '{entry[2]}', {entry[3]}),")

p = Physician()
p.add_from_file()
p.modifying_datatypes()
p.create_document_queries()
#p.print_queries()
'''
