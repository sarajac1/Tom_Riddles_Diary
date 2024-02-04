# Importerar SpaCy
import spacy

#Importerar PhraseMatcher
from spacy.matcher import PhraseMatcher

# Ladda SpaCy modellen med engelska språkpaketet
nlp = spacy.load("en_core_web_lg")

#Ställer in språkinställningar, case-insensitive
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")


# Funktion för att få användaren att mata in sitt namn (eller annat korrekt namn)
def get_name(prompt):
    while True:
        # Sparar värdet av användarens input
        user_input = input(prompt)
        #Skapar ett Doc objekt av användarens inmatning
        doc = nlp(user_input)

        #Loopar genom entiteterna i doc
        for ent in doc.ents:
            # Om input är en entitet av typen "person" så kommer personligt meddelande skrivas ut
            if ent.label_ == "PERSON":
                #Personligt meddelande skrivs ut och loopen bryts
                print(f"Tom Riddle: Hello {ent.text}. My name is Tom Riddle.")
                return ent.text
        #Om SpaCy inte känner igen det inmatade värdet som ett namn så kommer en uppmaning att uppge ett riktigt namn
            print("Tom Riddle: I can tell when people are lying to me and that is not a real name. I will ask "
                  "you again. What is your name?")

#Funktion som ska få användarens input
def get_user_response(prompt):
    #Skapar variabel som användarens input sparas i
    user_input = input(prompt)
    #Input blir ett doc objekt
    doc = nlp(user_input)
    #Returnerar objektet doc
    return doc

#Funktion för att matcha första nyckelorden
def first_matcher():
    #Anger vilka nyckelord som ska matchas
    keywords = ["github", "computer", "online"]
    patterns = [nlp.make_doc(text) for text in keywords]
    matcher.add("FirstReplyWords", None, *patterns)




def respond_to_first_reply(doc):
    matches = matcher(doc)
    for match_id, start, end in matches:
        span = doc[start:end]
        if span.text.lower() in ["github", "computer", "online"]:
                return ("Lucky that I recorded my memories in some more lasting way than ink. But I always "
                        "knew that there would be those who would not want this read. Would you like me to tell you "
                        "more?")
        return ("Is that some muggle technology? Anyway, it was lucky that  I recorded my memories in some"
                "more lasting way than ink. But I always knew that there would be those who would not want this "
                "read. Would you like me to tell you more?")

def chat():
    first_matcher()
    get_name("What is your name? ")
    doc = get_user_response("How did you come by my app? ")
    response = respond_to_first_reply(doc)
    print("Tom Riddle: ", response)

chat()
















# #Anropar funktionen som genererar ett svar
# response = generate_response(user_input)
# # Skriver ut ett svar till användaren
# print(response)




