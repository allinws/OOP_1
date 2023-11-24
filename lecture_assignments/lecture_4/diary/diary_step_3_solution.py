import datetime

class DiaryStepThree():
    
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
        
        def print_formatted_entries(self):
            print('ALL ENTRIES: ')
            for entry in self.entries:
                print(f"{entry['date'].strftime('%Y-%m-%d')}: {entry['entry']}")
        
        def get_entries_for_month(self, month):
            entries_for_month = []
            for entry in self.entries:
                if entry['date'].month == month:
                    entries_for_month.append(entry)
            if len(entries_for_month) == 0:
                return "No entries for this month"
            return entries_for_month
        

my_diary = DiaryStepThree()
my_diary.add_entry("Entry 1", datetime.datetime(2021, 1, 1))
my_diary.add_entry("Entry 2", datetime.datetime(2021, 1, 2))
print('All entries ', my_diary.get_entries())
print('Entry by date ', my_diary.get_entry_by_date(datetime.datetime(2021, 1, 2)))
print('Entry by index ', my_diary.get_entry_by_index(1))
print('Entries for month ', my_diary.get_entries_for_month(1))
my_diary.print_formatted_entries()
