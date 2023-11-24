class DiaryStepTwo():

    def __init__(self):
        self.entries = []

    def add_entry(self, entry, date):
        entry = {'entry': entry, 'date': date}
        self.entries.append(entry)

    def get_entries(self):
        return self.entries
    
    def get_entry_by_date(self, date):
        for entry in self.entries:
            if entry['date'] == date:
                return entry['entry']
        return "Entry not found"
    
    def get_entry_by_index(self, index):
        try: 
            return self.entries[index]
        except IndexError:
            return "Entry not found"
    

my_diary = DiaryStepTwo()
my_diary.add_entry("Entry 1", "2021-01-01")
my_diary.add_entry("Entry 2", "2021-01-02")
print('All entries ', my_diary.get_entries())
print('Entry by date ', my_diary.get_entry_by_date("2021-01-02"))
print('Entry by index ', my_diary.get_entry_by_index(1))



    
