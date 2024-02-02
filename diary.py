# Importerar SpaCy
import spacy

# Ladda SpaCy modellen med engelska språkpaketet
nlp = spacy.load("en_core_web_lg")

# Funktion för att få användarens namn genom en prompt
def get_name(prompt):
    # Sparar värdet av användarens input i prompten
    user_input = input(prompt)
    # Returnerar ett Doc objekt av användarens inmatning
    return nlp(user_input)


# Funktion för att svara på användarens input av namn
def respond_name(doc):
    # Om input är en entitet av typen "person" så kommer personligt meddelande skrivas ut, annars kommer ett annat meddelande.
    # Loopar genom de entiteter som finns i användarens inmatning
    for ent in doc.ents:
        # Understrecket innebär att programmet ger strängvärde istället för numeriskt värde på ent.label
        if ent.label_ == "PERSON":
            # Om entiteten/erna känns igen som namn så returneras ett trevligt meddelande
            return f"Tom Riddle: Hello {ent.text}. My name is Tom Riddle. How did you come by my app?"
        # Om det inmatade värdet inte känns igen som ett namn så promptas användaren att skriva in ett riktigt namn
    get_name(
        prompt="Tom Riddle: I don't recognize that as a name. I can tell when people are lying to me. I will ask you again. What is your name? ")


# Funktion för att skriva ut ett svar baserat på användarens inmatning
def generate_response(user_input):
    response = respond_name(user_input)
    return response


# Ber användaren skriva in sitt namn
user_input = get_name("What is your name? ")

response = generate_response(user_input)
# Skriver ut ett svar till användaren
print(response)