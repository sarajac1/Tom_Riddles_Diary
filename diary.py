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
        # Skapar ett Doc objekt av användarens inmatning
        doc = nlp(user_input)

        # Om användarens input (case-insensitive) innehåller någon av orden nedan så skrivs ett meddelande ut och
        # applikationen avslutas
        if user_input.lower() in ["exit", "quit", "stop", "no"]:
            print("You are not worthy of this app, muggle. It is now closing down.")
            return

        # Initierar en ny boole för att rätt ska outputtas
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

        if not name_found:
            # Om SpaCy inte känner igen entiteten som ett namn så kommer en uppmaning att uppge ett riktigt namn
            print("Tom Riddle: I know when people are lying to me and that is not a real name.\n I will ask "
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
    # Loopar över varje ord i nyckelorden och skapar doc objekt av deras tokens
    patterns = [nlp.make_doc(text) for text in keywords]
    # Lägger till pattern ovan till matcher.
    matcher.add("FirstReplyKeywords", patterns)


# Funktion som svarar på första matchningen
def respond_to_first_reply(doc):
    # Skapar en variabel av innehållet i doc objektet
    matches = matcher(doc)
    # Skapar en variabel för att hålla koll på om matchning hittats, initialiseras till falskt
    match_found = False
    # Loopar genom varje matchning och hittar deras plats
    for match_id, start, end in matches:
        if nlp.vocab.strings[match_id] == "FirstReplyKeywords":
            # Loopen avbryts när matchning hittats
            match_found = True
            break

    # Om matchning hittats så skrivs passande meddelande ut
    if match_found:
        return ("Lucky that I recorded my memories in some more lasting way than ink.\n"
                "This app holds memories of terrible things involving Hogwarts and the Chamber of Secrets.")
    # Om ingen matchning hittats så skrivs ett annat meddelande ut där användaren fortsatt har möjlighet att fortsätta
    else:
        return ("Is that some muggle technology? Anyway, this app holds memories of terrible things involving "
                "Hogwarts and the Chamber of Secrets.")


# Funktion för att matcha fler nyckelord
def second_matcher():
    # Anger nyckelord att leta efter
    keywords = ["yes", "tell me", "chamber of secrets"]
    # Loopar över varje ord i nyckelorden och skapar doc objekt av deras tokens
    patterns = [nlp.make_doc(text) for text in keywords]
    # Lägger till i matcher
    matcher.add("SecondReplyKeywords", patterns)


# Funktion för att svara på användarens input
def respond_to_second_reply(doc):
    matches = matcher(doc)
    match_found = False
    for match_id, start, end in matches:
        if nlp.vocab.strings[match_id] == "SecondReplyKeywords":
            match_found = True
            break

    if match_found:
        return ("In my fifth year, the Chamber of Secrets was opened and a monster attacked several students,\n"
                "finally killing one. I caught the person who had opened the Chamber and he was expelled. \n"
                "The story was covered up as an accident and I was warned to keep my mouth shut. \n"
                "But the monster is still alive and it can happen again.")
    else:
        return "Are you not interested in the Chamber of Secrets?"


# Funktion för tredje matchningen
def third_matcher():
    keywords = ["who", "so", "and"]
    patterns = [nlp.make_doc(text) for text in keywords]
    matcher.add("ThirdReplyKeywords", patterns)


def respond_to_third_reply(doc):
    matches = matcher(doc)
    match_found = False
    for match_id, start, end in matches:
        if nlp.vocab.strings[match_id] == "ThirdReplyKeywords":
            match_found = True
            break

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


# Funktion för att få till en konversation med chatbot
def chat():
    # Anropar metod för att användaren ska mata in sitt namn
    name = get_name("What is your name? ")
    if name is None:
        return

    # Anropar metod matchningarna
    first_matcher()
    second_matcher()
    third_matcher()

    doc = get_user_response("How did you come by my app? ")
    if doc is None:
        return
    response = respond_to_first_reply(doc)
    print("Tom Riddle: ", response)

    doc = get_user_response("Would you like to know more? ")
    if doc is None:
        return
    response = respond_to_second_reply(doc)
    print("Tom Riddle: ", response)

    doc = get_user_response("But I know who it was last time... ")
    if doc is None:
        return
    response = respond_to_third_reply(doc)
    print("Tom Riddle: ", response)
