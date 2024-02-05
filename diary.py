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
        # Sparar värdet av användarens input
        user_input = input(prompt)
        #Skapar ett Doc objekt av användarens inmatning
        doc = nlp(user_input)

        #Loopar genom entiteterna i doc
        for ent in doc.ents:
            # Om input är en entitet av typen "person" så kommer personligt meddelande skrivas ut
            # _(understreck) här gör så att det är sträng-värdet som hanteras och inget numeriskt värde
            if ent.label_ == "PERSON":
                #Personligt meddelande skrivs ut och loopen bryts
                print(f"Tom Riddle: Hello {ent.text}. My name is Tom Riddle.")
                #Returnererar namnet som hämtats
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
    #Loopar över varje ord i nyckelorden och skapar doc objekt av deras tokens
    patterns = [nlp.make_doc(text) for text in keywords]
    #Lägger till pattern ovan till matcher. * i patterns gör så att varje objekt
    #hanteras för sig
    matcher.add("FirstReplyWords", None, *patterns)


#Funktion som svarar på första matchningen
def respond_to_first_reply(doc):
    #Skapar en variabel av innehållet i doc objektet
    matches = matcher(doc)
    #Skapar en variabel för att hålla koll på om matchning hittats, initialiseras till falskt
    match_found = False
    #Loopar genom varje matchning och hittar deras plats
    for match_id, start, end in matches:
        #Tar ut det spannet from dokumentet som matchar sökningen
        span = doc[start:end]
        if (span.text.lower() in ["github", "computer", "online"]):
            match_found = True
            break

    if match_found:
        return ("Lucky that I recorded my memories in some more lasting way than ink. But I always "
                    "knew that there would be those who would not want this read.\n  Would you like to know why?")
    else:
        return ("Is that some muggle technology? Anyway, it was lucky that  I recorded my memories in some"
                    "more lasting way than ink. \n But I always knew that there would be those who would not want this "
                    "read. Would you like to know why?")


#Funktion för att matcha fler nyckelord
def second_matcher():
    # Anger nyckelord att leta efter
    keywords = ["yes", "tell me", "why?"]
    # Loopar över varje ord i nyckelorden och skapar doc objekt av deras tokens
    patterns = [nlp.make_doc(text) for text in keywords]
    # Lägger till i matcher
    matcher.add("SecondReplyWords", None, *patterns)

#Funktion för att svara på användarens input
def respond_to_second_reply(doc):
    matches = matcher(doc)
    for match_id, start, end in matches:
        span = doc[start:end]
        if span.text.lower() in ["github", "computer", "online"]:
            return ("This app holds memories of terrible things. Things which were covered up. \n "
                    "Things which happened at Hogwarts School of Witchcraft and Wizardry. Would you like to know more?")
        return "Are you not interested in the Chamber of Secrets?"


#Funktion för tredje matchningen
def third_matcher (doc):
    keywords = ["chamber of secrets", "yes", "tell me"]
    patterns = [nlp.make_doc(text) for text in keywords]
    matcher.add("ThirdReplyWords", None, *patterns)


def respond_to_third_reply(doc):
    matches = matcher(doc)
    for match_id, start, end in matches:
        span = doc[start:end]
        if span.text.lower() in ["chamber of secrets", "yes", "tell me"]:
            return ("In my day they told me the Chamber of Secrets was a legend, that it did not exist.\n"
                    "In my fifth year, the Chamber was opened and the monster attacked several students, finally \n"
                    "killing one. I caught the person who had opened the Chamber and he was expelled. \n"
                    "But the Headmaster, Professor Dippet, ashamed that such a thing had happened at Hogwarts, \n"
                    "forbade me to tell the truth. A story was given out that the girl had died in a freak accident.\n"
                    "They gave me a nice, shiny, engraved trophy for my trouble and warned me to keep my mouth shut. "
                    "But I knew it could happen again. The monster lived on, and the one who had the power to release\n"
                    "it was not imprisoned.'")


#Funktion för tredje svaret


#Funktion för att få till en konversation med chatbot
def chat():
    #Anropar metod för första matchningen
    first_matcher()
    second_matcher()
    #Anropar metod för att användaren ska mata in sitt namn
    get_name("What is your name? ")
    #
    doc = get_user_response("How did you come by my app? ")
    #
    response = respond_to_first_reply(doc)

    response = respond_to_second_reply(doc)

    response = respond_to_third_reply(doc)

    print("Tom Riddle: ", response)




chat()





