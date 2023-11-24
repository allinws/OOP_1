# Skapa en class som heter DiaryStepThree

## Användning av `datetime`:
    # I detta steg introducerar vi användningen av `datetime` objekt för att hantera datum, vilket gör programmet mer robust och flexibelt.

## Attribut för DiaryStepThree:
    # `entries`: En lista av entries. Varje entry är en dictionary med 'entry' och 'date' (som ett `datetime` objekt).

## Metoder för DiaryStepThree:
    # `add_entry`: Tar emot en sträng `entry` och ett `datetime` objekt `date`, och lägger till detta som en dictionary i `entries`.
    # `get_entries`: Returnerar alla entries.
    # `get_entry_by_date`: Söker efter och returnerar entries baserat på ett `datetime` objekt. Returnerar "Entry not found" om inget entry hittas.
    # `get_entry_by_index`: Returnerar ett entry baserat på ett index. Använder try och except för att hantera IndexError, om indexet inte finns i listan returnera "Entry not found".
    # `get_entry_by_date`: Formaterar och returnerar entries som strängar, där datum visas i ett läsbart format.
    # `print_formatted_entries`: Printar först ut "ALL ENTRIES: ", sedan printar den ut alla entries, en i taget, i ett lättläst format, som t.ex. "2021-01-01: Entry 1". (använd strftime för att formatera datumet och f-string för att skapa strängen)
    # `get_entries_for_month`: Returnerar alla entries för en specifik månad. Använd `datetime` objekt för att hantera månaden. Returnerar "No entries for this month" om inga entries hittas.

## Uppgifter att genomföra efter att klassen har skapats:
    # 1. Skapa en instans av `DiaryStepThree`.
    # 2. Använd `add_entry`-metoden för att lägga till minst två entries med `datetime` datum.
    # 3. Använd `get_entries` för att hämta och skriva ut alla entries.
    # 4. Använd `get_entry_by_date` med ett specifikt `datetime` objekt och skriv ut resultatet.
    # 5. Använd `get_entry_by_index` med ett specifikt index och skriv ut resultatet.
    # 7. Använd `get_entries_for_month` för en specifik månad och skriv ut resultatet.
    # 6. Använd `print_formatted_entries` för att visa alla entries i ett lättläst format.