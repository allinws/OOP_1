
# Skapa en class som heter DiaryStepTwo

# NOTERING: Du skall INTE använda datetime här, utan alla datum är fortfarande strängar

## Attribut för DiaryStepTwo:
    # `entries`: En lista av entries. Varje entry kommer sedan vara en dictionary med 'entry' och 'date' som keys.

## Metoder för DiaryStepTwo:
    # `add_entry`: Tar emot en sträng `entry` och en sträng med ett `date`, och lägger till detta som en dictionary i `entries`.
    # `get_entries`: Returnerar alla entries.
    # `get_entry_by_date`: Itererar över alla entries, och om ett entrys 'date' (i form av en sträng) är samma som det datum som skickas in som argument, returnera det entryt. Annars returnera "Entry not found".
    # `get_entry_by_index`: Returnerar ett entry baserat på ett index. Använder try och except för att hantera IndexError, om indexet inte finns i listan returnera "Entry not found".

## Uppgifter att genomföra efter att klassen har skapats:
    # 1. Skapa en instans av `DiaryStepTwo`.
    # 2. Använd `add_entry`-metoden för att lägga till minst två entries med olika datum (kalla på den två gånger)
    # 3. Använd `get_entries` för att hämta och skriva ut alla entries.
    # 4. Använd `get_entry_by_date` med ett specifikt datum och skriv ut resultatet.
    # 5. Använd `get_entry_by_index` med ett specifikt index och skriv ut resultatet.

    
