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
1
Maria Flores
Head Physician
14141414

2
Elliot Reid
Attending Physician
22222222
'''