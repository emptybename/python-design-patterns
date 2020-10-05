class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, entry):
        self.count += 1
        self.entries.append(entry)

    def remove_entry(self, position):
        del self.entries[position]
        self.count -= 1

    def __str__(self):
        return '\n'.join(self.entries)

    # Till here we are following the SRP

    # Now we are breaking the SRP by adding other responsibilities

    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def load_from_web(self, filename):
    #     pass


# To maintain SRP -

class PersistenceManager:
    @staticmethod
    def save_to_file(journal: Journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("Hello World")
j.add_entry("World is cruel")
print(f'Journal Entries: \n{j}')

p = PersistenceManager()

file = 'journal.txt'
p.save_to_file(j, file)

with open(file, 'r') as f:
    print(f.read())

