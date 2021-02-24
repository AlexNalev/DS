'''
# --------------------------------------------------------------------------
# table trained_in
class Training:
    def __init__(self):
        self.table = []

    def read_values(self):
        self.file = open("trained_in", "r")
        if self.file.mode == "r":
            for i in range(15):
                content = self.file.readline()
                row = content.split(' | ')
                self.table.append(row)
        self.file.close()

    def transform_values(self):
        for entry in self.table:
            entry[0] = int(entry[0])
            entry[1] = int(entry[1])

    def generate_document(self):
        self.file = open("TrainingValues", "w")
        self.file.write("INSERT INTO trained_in\nVALUES\n")
        for entry in self.table:
            self.file.write(f"({entry[0]}, {entry[1]}, '{entry[2]}', '{entry[2]}'),\n")
        
        self.file.close()


r = Training()
r.read_values()
r.transform_values()
r.generate_document()

# ----------------------------------------------------------------------------
# Med_procedure table
class Procedure:
    def __init__(self):
        self.room = []

    def read_values(self):
        self.file = open("med_procedure", "r")
        if self.file.mode == "r":
            for i in range(7):
                content = self.file.readline()
                row = content.split(' | ')
                self.room.append(row)
        self.file.close()

    def transform_values(self):
        for entry in self.room:
            entry[0] = int(entry[0])
            entry[2] = int(entry[2])

    def generate_document(self):
        self.file = open("ProcedureValues", "w")
        self.file.write("INSERT INTO med_procedure\nVALUES\n")
        for entry in self.room:
            self.file.write(f"({entry[0]}, '{entry[1]}', {entry[2]}),\n")
        
        self.file.close()


r = Procedure()
r.read_values()
r.transform_values()
r.generate_document()

# ----------------------------------------------------------------------------
# room table
class Room:
    def __init__(self):
        self.room = []

    def read_values(self):
        self.file = open("room", "r")
        if self.file.mode == "r":
            for i in range(36):
                content = self.file.readline()
                row = content.split(' | ')
                self.room.append(row)
        self.file.close()

    def transform_values(self):
        for entry in self.room:
            entry[0] = int(entry[0])
            entry[2] = int(entry[2])
            entry[3] = int(entry[3])

            entry[4] = entry[4].rstrip()
            if entry[4] == 'f':
                entry[4] = 0
            elif entry[4] == 't':
                entry[4] = 1

    def generate_document(self):
        self.file = open("RoomValues", "w")
        self.file.write("INSERT INTO room\nVALUES\n")
        for entry in self.room:
            self.file.write(f"({entry[0]}, '{entry[1]}', {entry[2]}, {entry[3]}, {entry[4]}),\n")
        
        self.file.close()


r = Room()
r.read_values()
r.transform_values()
r.generate_document()

# ---------------------------------------------------------------------------
# Appointment table
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
