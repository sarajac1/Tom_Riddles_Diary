Tom Riddle's Diary Chatbot

Baserad på boken, Harry Potter and the Chamber of Secrets av J.K. Rowling
Textutdrag som används som bas för appen finns i filen "Harry_Potter.txt"

Öppna i PyCharm, ladda ner SpaCy och PhraseMatcher

I terminalen, skriv följande för att installera det stora Engelska språkpaketet:
python -m spacy download en_core_web_lg

Kör programmet från filen "chatbot.py" och svara på frågorna som ställs av chatboten.
Det rekommenderas att du drar ut terminalen så att den tar mycket plats under tiden som programmet körs.
Konversationen ska efterlikna den som sker mellan Harry Potter och Tom Riddle, via skrift i en fysisk dagbok, se Harry_
Potter.txt-filen för utdrag från boken. Konversationen ser annorlunda ut beroende på dina svar.

För mer information om frågorna och möjliga svar, se facit.txt. Tanken är att du bor kunna hänga med i botens flöde.

En förklaring av programmet:

Programmet flöde:
Boten kommer att börja med att be om ditt namn. Om det inmatade värdet inte känns igen som ett namn (entitet: person)
så kommer du att få en uppmaning att skriva in ett korrekt namn tills dess att det känns igen som ett riktigt namn.
OBS att SpaCy inte är särskilt tillförlitlig när det kommer till att kunna identifiera namn korrekt då den ibland
reagerar på påhittade namn som om de vore riktiga och vice versa.

Du får sedan frågan från boten om hur du hittade appen. Du kan skriva svar som består av ett eller flera ord i en
mening eftersom det är specifika ord som matchas till lämpligt svar.
Om det inte matchas så får du ett lämpligt meddelande med möjlighet att fortsätta konversationen med chatbot.

Boten kommer sedan att fråga om du vill veta mer om de händelser som skedde på skolan med en prompt om att man kan få
reda på mer. Programmet är klart när boten avslutat sin historia eller när du själv skriver in ett ord för att avbryta.
Programmet kan även avslutas om du inte matar inte ett tillfredsställande svar/svarar "rätt".

Du kan när som helst avsluta programmet under körning genom att mata in ett av fyra ord (se facit).


