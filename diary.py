# Importerar SpaCy
import spacy

# Importerar PhraseMatcher
from spacy.matcher import PhraseMatcher

# Ladda SpaCy modellen med engelska språkpaketet
nlp = spacy.load("en_core_web_lg")

# Ställer in språkinställningar, case-insensitive
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")


# Funktion för att få användaren att mata in sitt namn (eller annat korrekt namn)
def get_name(prompt):
    while True:
        # Sparar värdet av användarens input
        user_input = input(prompt)
        # Skapar ett doc objekt av användarens inmatning
        doc = nlp(user_input)

        # Om användarens input (case-insensitive) innehåller någon av orden nedan så skrivs ett meddelande ut och
        # applikationen avslutas
        if user_input.lower() in ["exit", "quit", "stop", "no"]:
            print("You are not worthy of this app, muggle. It is now closing down.")
            return

        # Initierar en ny boole och antar att namn ej hittats
        name_found = False

        # Loopar genom entiteterna i doc
        for ent in doc.ents:
            # Om input är en entitet av typen "person" så kommer personligt meddelande skrivas ut
            # _(understreck) här gör så att det är sträng-värdet som hanteras och inget numeriskt värde
            if ent.label_ == "PERSON":
                # Personligt meddelande skrivs ut och loopen bryts
                print(f"Tom Riddle: Hello {ent.text}. My name is Tom Riddle.")
                # Returnerar namnet som hämtats
                return ent.text
        # Om SpaCy inte känner igen entiteten som ett namn så kommer en uppmaning att uppge ett riktigt namn
        if not name_found:
            print("Tom Riddle: I know when people are lying to me and that is not a real name.\nI will ask "
                  "you again.")


# Funktion som ska få användarens input
def get_user_response(prompt):
    # Skapar variabel som användarens input sparas i
    user_input = input(prompt)
    # Kontrollerar om användaren matat in ett ord som tyder på att de vill avsluta programmet, skriver ut meddelande och
    # avslutar programmet
    if user_input.lower() in ["exit", "quit", "stop", "no"]:
        print("You are not worthy of this app, muggle. It is now closing down.")
        return
    # Input blir ett doc objekt
    doc = nlp(user_input)
    # Returnerar objektet doc
    return doc


# Funktion för att matcha första nyckelorden
def first_matcher():
    # Anger vilka nyckelord som ska matchas
    keywords = ["github", "computer", "online"]
    # Skapar en lista av doc-objekt för varje nyckelord
    patterns = [nlp.make_doc(text) for text in keywords]
    # Lägger till listan ovan till matcher.
    matcher.add("FirstReplyKeywords", patterns)


# Funktion som svarar på första matchningen
def respond_to_first_reply(doc):
    # Matcher-objektet letar efter matchningar i doc
    matches = matcher(doc)
    # Skapar en variabel för att hålla koll på om matchning hittats, initialiseras till falskt
    match_found = False
    # Loopar genom varje matchning och hittar dess start- och stopposition
    for match_id, start, end in matches:
        # Kontrollerar om matchning till nyckelord
        if nlp.vocab.strings[match_id] == "FirstReplyKeywords":
            # Loopen avbryts när matchning hittats och variabeln ändras
            match_found = True
            break

    # Om matchning hittats så skrivs passande meddelande ut
    if match_found:
        return ("Lucky that I recorded my memories in some more lasting way than ink.\n"
                "This app holds memories of terrible things involving Hogwarts and the Chamber of Secrets.")
    # Om ingen matchning hittats så skrivs ett annat meddelande ut där användaren har möjlighet att fortsätta
    else:
        return ("Is that some muggle technology? Anyway, this app holds memories of terrible things involving "
                "Hogwarts and the Chamber of Secrets.")


# Funktion för att matcha fler nyckelord
def second_matcher():
    # Anger nyckelord att leta efter
    keywords = ["yes", "tell me", "chamber of secrets", "sure"]
    # Skapar en lista av doc-objekt för varje nyckelord
    patterns = [nlp.make_doc(text) for text in keywords]
    # Lägger till i matcher
    matcher.add("SecondReplyKeywords", patterns)


# Funktion för att svara på användarens input
def respond_to_second_reply(doc):
    # Matcher-objektet letar efter matchningar
    matches = matcher(doc)
    # Ny boole som startar på falskt
    match_found = False
    # Loopar genom varje matchning och hittar start- och stopposition
    for match_id, start, end in matches:
        # Kontrollerar om matchning till nyckelord
        if nlp.vocab.strings[match_id] == "SecondReplyKeywords":
            # Ändrar variabelns värde till sant och bryter loopen
            match_found = True
            break
    # Passande meddelande skrivs ut om matchning hittats
    if match_found:
        return ("In my fifth year, the Chamber of Secrets was opened and a monster attacked several students,\n"
                "finally killing one. I caught the person who had opened the Chamber and he was expelled. \n"
                "The story was covered up as an accident and I was warned to keep my mouth shut. \n"
                "But the monster is still alive and it can happen again.")
    # Passande meddelande skrivs ut om matchning EJ har hittats
    else:
        return "It seems you are not interested in the Chamber of Secrets. Even if... "


# Funktion för tredje matchningen
def third_matcher():
    # Skapar nyckelord att matcha
    keywords = ["who", "so", "and"]
    # Skapar en lista av doc-objekt för varje nyckelord
    patterns = [nlp.make_doc(text) for text in keywords]
    # Lägger till i matcher
    matcher.add("ThirdReplyKeywords", patterns)


# Funktion för tredje svaret
def respond_to_third_reply(doc):
    # Matcher-objektet letar efter matchningar
    matches = matcher(doc)
    # Ny variabel som är falsk
    match_found = False
    # Loopar genom varje matchning och hittar deras start- och stopposition
    for match_id, start, end in matches:
        #  Kontrollerar om matchning till nyckelord
        if nlp.vocab.strings[match_id] == "ThirdReplyKeywords":
            # Ändrar variabeln och bryter
            match_found = True
            break
    # Lämpligt meddelande skrivs ut om matchning hittats
    if match_found:
        return ("IT WAS ME ALL ALONG. \n"
                "THE HEIR OF SLYTHERIN HAS INFECTED YOUR COMPUTER WITH A VIRUS. *HISSES IN PARSELTONGUE* \n"
                """
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣄⣶⣶⣶⣶⣾⣿⣿⣿⣶⣶⣶⣦⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⢰⣦⣄⣀⠀⠀⠀⠀⣀⣀⡀⠀⢀⣀⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⡿⠿⣟⠻⠏⢩⢹⣿⣿⣿⣿⡿⠿⢿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⢀⣘⠻⠯⢑⣊⣉⣀⠀⠀⢸⡘⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡆⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠙⠛⠛⠿⢿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⡏⠀⣠⡾⠛⠻⣿⡿⠟⠃⠸⡇⢀⣴⣷⠀⠀⠀⠀⠀⠀⢀⣴⣧⡀⢹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢧⡀⠀⠀⠀⠀⠀
        ⠀⠀⡀⠄⠒⡇⠀⣿⣦⡀⠀⠉⠀⠀⠀⠀⡇⠀⣿⣿⠀⠀⣀⠀⠀⣀⢨⣿⡏⠀⢸⣿⣧⣴⣦⡀⠀⣴⣶⣶⣄⠀⣀⣴⣤⣤⡀⠀⣿⠇⠀⠀⠀⠀⠈⠧⠤⢄⡀⠀
        ⣠⠊⠀⠀⠀⠃⠀⠙⣿⣿⣶⣄⠀⠀⠀⠀⡇⠀⣿⣿⠘⣿⣿⠀⣿⡇⢸⣿⡇⠀⢸⣿⠃⢹⣿⡇⢸⣿⠁⣸⠿⠀⣿⣿⠛⠟⠁⣤⣴⡆⢀⣀⣠⡀⠀⠀⠀⠀⠉⡦
        ⠈⠢⣤⠀⠀⢸⠀⠀⠈⠻⣿⣿⣿⣦⡀⠀⠇⠀⣿⣿⠀⠸⣿⣦⣿⠁⠘⣿⣇⠄⣸⣿⡀⢸⣿⡇⢸⣿⡋⢀⡆⠀⣿⣿⠀⠀⢀⣿⡿⠀⢸⣿⡿⢻⣿⡆⠀⢀⠞⠁
        ⠀⠀⠀⠰⡀⣸⣤⣤⣤⣄⠈⠻⣿⣿⣧⠀⠀⠀⠾⠿⠂⠀⢹⡿⠃⠀⠈⠛⠁⠈⠉⠁⠀⠚⠛⠓⠈⠛⠷⠛⠁⠠⠿⠿⠄⠀⣼⣿⡇⠀⣸⣿⠁⢸⣿⠇⢠⠋⠀⠀
        ⠀⠀⠀⠀⣿⣿⠋⠁⠉⢿⣷⠀⠸⣿⣿⠀⢠⠀⠀⣴⣷⡾⠟⠁⣀⡤⠔⠒⠉⠉⠉⠉⠉⠓⠢⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠠⠿⠇⢀⣾⣿⠀⢳⠀⠀⠀
        ⠀⠀⠀⢸⣿⠁⠀⢦⣤⣾⡿⠀⢠⣿⣿⠂⢸⠀⣀⠠⣄⣒⢉⡿⠋⠀⠀⠀⢰⣄⣠⣀⣄⢀⠀⠀⠈⠣⣉⣲⢶⣤⣤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠉⠙⠃⢀⡏⠀⠀⠀
        ⠀⠀⠀⢹⣿⣆⠀⠀⠀⠀⠀⢀⣾⣿⠟⠀⠸⠉⢰⣿⣿⢏⡞⠀⠀⠀⣠⣾⢟⣻⣯⣭⣟⡻⢿⣄⠀⠀⢶⣶⣍⠚⠋⠉⢽⢻⣷⣦⣄⡀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀
        ⠀⠀⠀⠀⠻⣿⣿⣶⣦⣴⡶⠟⠋⣁⣀⡤⠃⢀⣼⣿⡟⣼⡃⠀⠀⢰⡟⠀⠈⢻⡟⠁⠈⢻⣇⢿⡇⠀⣠⣤⠔⠒⠤⡂⢌⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⡜⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⡇⠀⠀⣀⠤⣒⣭⡍⢰⣾⣿⣿⣿⣿⣿⡇⡟⡁⠀⠀⢸⡇⣄⠰⣿⣿⠆⣴⣿⣿⣮⡳⡀⠹⡇⠐⠢⡔⣿⣿⣿⣿⡿⢿⣿⣿⣿⡇⠉⠙⠃⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠧⠒⠉⣶⣿⣿⣿⡇⠈⢿⣿⣿⣿⠿⢻⣇⢿⣷⠀⠀⠀⠙⢎⡳⣌⣡⣾⣿⣿⣿⣿⡇⠀⣥⣢⠅⣒⠛⣢⣽⡿⠋⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⣤⡙⣿⢱⢹⢸⣿⣌⢿⣷⣀⠀⠀⠀⠙⠢⢝⡻⢿⣿⣿⣿⣷⣠⣿⣿⣿⣶⣶⣿⣫⣶⣄⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⢸⣿⣿⡌⢸⠀⣞⢿⣿⣷⣝⠿⣷⣦⣄⣀⡀⠀⠉⠐⠨⢝⡻⢿⣿⣿⣿⣿⣿⠟⠹⣿⣿⣿⠆⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⢹⡟⡱⠟⣇⠘⢷⡒⢭⡻⣷⣮⣝⡻⣿⣿⣦⣀⠀⠀⠀⠉⠒⢭⡻⠿⢟⣅⠀⠀⣹⣿⡁⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⡇⢠⡿⡸⠁⢸⡾⢦⡀⠳⡀⠹⡽⣿⣿⣿⣷⠍⠻⢿⣿⣶⣤⣀⠀⠀⠈⢳⣝⢿⡆⢴⣿⣿⣷⡄⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠸⡇⡇⠀⢾⡀⣀⡷⠰⣧⠀⡇⣹⣿⣿⣿⣄⣠⣶⣭⡻⢿⣿⣷⠄⠀⠈⠻⢧⡀⠈⢻⡿⠋⠀⣼⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⢀⣷⢻⣄⠀⠉⠉⠀⢀⡿⢠⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣝⢿⣷⣄⠀⠀⠀⢻⣀⣾⣷⣄⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠘⣿⣷⢉⣓⠶⠾⣴⣾⠃⢸⠇⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠹⣿⣦⠀⠀⢈⣇⣿⣿⡿⠁⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡇⠀⢈⣴⣿⣿⣿⣿⢹⣿⠀⢿⢠⣾⣿⣿⣿⣿⡿⣿⣿⣿⣿⣷⣄⣤⢻⣿⠀⠀⠸⣿⣹⣯⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⢰⣿⣿⣿⣿⡿⠿⢸⣿⠀⢸⣼⣿⣿⣿⠿⣫⣾⣮⠻⣿⣿⣿⣿⡿⣼⣿⠀⢠⣀⡇⣿⣿⣷⡄⣿⣿⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⡅⢀⢸⣿⠀⠸⣷⡻⠟⠁⠀⠹⣿⠋⠀⠈⠻⣿⠟⣱⣿⠏⢀⣿⣿⠁⣿⣿⣿⡇⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⡜⣿⣧⡀⠉⢹⢤⡀⠀⣴⣿⣦⠀⠀⣀⣴⡾⠟⠀⢀⣾⣿⣇⣰⣿⣿⣿⡇⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣷⡘⠻⢿⣿⣿⣿⣿⣿⣼⣿⣿⣶⡀⠀⠉⠛⠒⠒⠶⠟⠛⠋⠉⢀⣠⣶⣿⣿⣿⣿⣿⡿⢟⣫⣵⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣷⣦⣈⠙⠻⠿⠟⣱⣦⣍⡻⢿⣿⣿⣿⣆⣠⣶⣦⣤⣴⡾⠿⠛⣋⡻⣿⠿⣋⣥⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠙⠻⠿⠛⢷⣶⣬⡭⣭⣭⣭⡭⣥⣴⣶⠊⠻⢟⣫⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠋⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠈⠻⡏⠀⢘⣿⣟⠀⠈⡿⣋⣤⣶⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⡚⠿⢟⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """)
    # Meddelande skrivs ut om matchning ej hittats
    else:
        return "Are you a muggle? You seem rather dim."


# Funktion för att få till en konversation med chatbot
def chat():
    # Anropar metod för att användaren ska mata in sitt namn
    name = get_name("What is your name? ")
    # Returnerar noll om inget namn matas in eller om ord för att avsluta matats in och avslutar
    if name is None:
        return

    # Anropar metoder för matchningarna av nyckelord
    first_matcher()
    second_matcher()
    third_matcher()

    # Skapar första svaret från chatbot med en prompt att användaren ska skriva in ett svar
    doc = get_user_response("How did you come by my app? ")
    # Appen avslutas om inget doc hittats t.ex. om användaren valt att avsluta
    if doc is None:
        return
    # Skriver ut ett lämpligt svar beroende på om matchning hittats eller ej
    response = respond_to_first_reply(doc)
    print("Tom Riddle:", response)

    # Användaren promptas att mata in ett svar för att påbörja nästa del av konversationen
    doc = get_user_response("Would you like to know more? ")
    # Appen avslutas om inget doc hittats
    if doc is None:
        return
    # Lämpligt svar matas ut om ord matchats
    response = respond_to_second_reply(doc)
    print("Tom Riddle:", response)

    # Användaren får möjlighet att få reda på den sista biten i historien genom att skriva in rätt svar som matchas
    doc = get_user_response("I know who it was last time... ")
    # Appen avslutas om inget doc hittats
    if doc is None:
        return
    # Lämpligt svar skrivs ut om orden matchats
    response = respond_to_third_reply(doc)
    print("Tom Riddle:", response)
