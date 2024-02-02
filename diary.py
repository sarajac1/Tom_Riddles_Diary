# Importerar SpaCy
import spacy

# Ladda SpaCy modellen med engelska språkpaketet
nlp = spacy.load("en_core_web_lg")

# Funktion för att få användaren att mata in sitt namn (eller annat korrekt namn)
def get_name(prompt):
    while True:
        # Sparar värdet av användarens input
        user_input = input(prompt)
        #Skapar ett Doc objekt av användarens inmatning
        doc = nlp(user_input)
        #Skapar en variabel och ger den värdet falskt
        person_found = False

        #Loopar genom entiteterna i doc
        for ent in doc.ents:
            # Om input är en entitet av typen "person" så kommer personligt meddelande skrivas ut
            if ent.label_ == "PERSON":
                #Variabeln blir sann då ett namn hittats
                person_found = True
                #Personligt meddelande skrivs ut och loopen bryts
                print(f"Tom Riddle: Hello {ent.text}. My name is Tom Riddle. How did you come by my app?")
                break

        #Loopen bryts om namn hittats
        if person_found:
            break
        #Om SpaCy inte känner igen det inmatade värdet som ett namn så kommer en uppmaning att uppge ett riktigt namn
        else:
            print("Tom Riddle: I don't recognize that as a name. I can tell when people are lying to me. I will ask "
                  "you again. What is your name?")


# Funktion för att skriva ut ett svar baserat på användarens inmatning
# def generate_response(user_input):
#     response = respond_name(user_input)
#     return response


# Ber användaren skriva in sitt namn
user_input = get_name("What is your name? ")

# #Anropar funktionen som genererar ett svar
# response = generate_response(user_input)
# # Skriver ut ett svar till användaren
# print(response)




