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
        #Skapar en boole och ger den värdet falskt
        name_found = False

        #Loopar genom entiteterna i doc
        for ent in doc.ents:
            # Om input är en entitet av typen "person" så kommer personligt meddelande skrivas ut
            if ent.label_ == "PERSON":
                #Variabeln blir sann då ett namn hittats
                name_found = True
                #Personligt meddelande skrivs ut och loopen bryts
                print(f"Tom Riddle: Hello {ent.text}. My name is Tom Riddle. How did you come by my app?")
                break

        #Loopen bryts om namn hittats
        if name_found:
            break
        #Om SpaCy inte känner igen det inmatade värdet som ett namn så kommer en uppmaning att uppge ett riktigt namn
        else:
            print("Tom Riddle: I can tell when people are lying to me and that is not a real name. I will ask "
                  "you again. What is your name?")

# Ber användaren skriva in sitt namn
get_name("What is your name? ")


# Funktion för att skriva ut ett svar baserat på användarens inmatning
# def generate_response(user_input):
#     response = respond_name(user_input)
#     return response

def get_user_response(prompt):
    user_input = input(prompt)
    doc = nlp(user_input)
    matches = matcher(doc)
    return doc, matches

first_reply_keywords = ["github", "computer", "online"]
patterns = [nlp.make_doc(text) for text in first_reply_keywords]
matcher.add("FirstReplyKeywords", None, *patterns)

def respond_to_first_reply(doc):
    matches = matcher(doc)
    for match_id, start, end in matches:
        span = doc[start:end]
        if span.text.lower() in ("github", "computer", "online"):
                return ("(Tom Riddle: Lucky that I recorded my memories in some more lasting way than ink. But I always "
                        "knew that there would be those who would not want this read.")
        return ("Tom Riddle: Is that some muggle technology? Anyway, it was lucky that  I recorded my memories in some"
                "more lasting way than ink. But I always knew that there would be those who would not want this "
                "read. Would you like me to tell you more?")













def chat():
    user_name_input = get_name("What is your name? ")
    response = respond_to_first_reply(user_name_input)
    print("Tom Riddle: ", response)

while True:
    user_input = get_name("")
    doc = nlp(user_input.text)

# #Anropar funktionen som genererar ett svar
# response = generate_response(user_input)
# # Skriver ut ett svar till användaren
# print(response)




