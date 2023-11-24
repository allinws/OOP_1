class DiaryStepOne():

    def __init__(self, entries, name, owner):
        self.entries = entries
        self.name = name
        self.owner = owner

    def add_entry(self, entry):
        self.entries.append(entry)

    def get_entries(self):
        return self.entries
    
    def get_entry_by_index(self, index):
        return self.entries[index]
    
entries = ["Entry 1", "Entry 2"]
my_diary = DiaryStepOne(entries=entries, name="My Diary", owner="Me")
my_diary.add_entry("Entry 3")
my_diary.add_entry("Entry 4")
print('All entries ', my_diary.get_entries())
print('Entry by index ', my_diary.get_entry_by_index(1))

    


    
