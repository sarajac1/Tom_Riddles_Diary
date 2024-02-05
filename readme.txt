Tom Riddle's Diary Chatbot

Baserad på boken, Harry Potter and the Chamber of Secrets av J.K. Rowling
Textutdrag som används som bas för appen finns i filen "Harry_Potter.txt"

Öppna i PyCharm, ladda ner Jupyter notebooks och SpaCy

I terminalen, skriv följande för att installera det stora Engelska språkpaketet:
python -m spacy download en_core_web_lg

Kör programmet och svara på frågorna som ställs. För mer information om frågorna och möjliga svar, se nedan.

Boten kommer att börja med att be om ditt namn. Om det inmatade värdet inte känns igen som ett namn (entitet: person)
så kommer du att få en uppmaning att skriva in ett korrekt namn tills dess att det känns igen som ett riktigt namn.

Du får sedan frågan från boten om hur du hittade appen. Ord som godkänns är "online", "github", eller "computer". Du kan
skriva meningar som innehåller orden för att de ska matchas eller så skriver du endast ett av orden ovan. Om det inte
matchas så får du ett lämpligt meddelande.

Boten kommer sedan att fråga om du vill veta mer om de händelser som skedde på skolan. Godkända ord som svar på detta är
"yes", "tell me" och "why". Använder du någon av dessa så får du en historia om vad som hände med the Chamber of Secrets
förra gången.


