import time
import os

stys = os.system

def pdc():
    wait = time.sleep

    def load(text):
        print(text)
        wait(0.07)

    print('''PDC - Passage Decodability Calculator
Coding done by Samuel B.''')
    wait(1)
    print('''
------------------------------------------------------------
   
    ***IMPORTENT NOTES***

    Do not use CMD+C and CMD+V!!! CMD+C is a stop code.

    ***END IMPORTANT NOTES***

------------------------------------------------------------
''')
    input("Press [ENTER] To Accept...")
    stys('clear')
    stys('cls')
    print("Loading Words...")
    non_decodable_words = (
    "Colonel", "Queue", "Worcester", "Yacht", "Aisle", "Mnemonic", "Phlegm", "Subtle", "Island", "Sword",
    "Receipt", "Corps", "Doubt", "Honest", "Heir", "Whistle", "Debt", "Knob", "Tomb", "Plumber",
    "Ballet", "Buffet", "Bourgeois", "Gourmet", "Rendezvous", "Pneumonia", "Psalm", "Align", "Chassis", "Guacamole",
    "Comb", "Autumn", "Gnaw", "Gnat", "Chaos", "Choir", "Gauge", "Epitome", "Genre", "Paradigm",
    "Quay", "Bouquet", "Moet", "Forte", "Antique", "Poignant", "Depot", "Faux", "Camouflage", "Déjà vu",
    "Mirage", "Chameleon", "Scenario", "Cache", "Niche", "Regime", "Sovereign", "Silhouette", "Giraffe", "Fuchsia",
    "Brochure", "Cliché", "Camaraderie", "Liaison", "Tableau", "Vehement", "Ricochet", "Chauffeur", "Embassy", "Debris",
    "Vintage", "Visionary", "Aviary", "Bizarre", "Cadre", "Cathedral", "Chandelier", "Concierge", "Deja vu", "Emporium",
    "Entrepreneur", "Façade", "Finale", "Forte", "Gallery", "Genre", "Guillotine", "Harangue", "Homage", "Knapsack",
    "Labyrinth", "Loge", "Malady", "Memento", "Menagerie", "Nausea", "Opulent", "Paradox", "Phenomenon", "Plaque",
    "Pseudonym", "Rendezvous", "Reverie", "Sacrilege", "Scenario", "Silhouette", "Sovereignty", "Technique", "Theorem", "Tsunami",
    "Unique", "Utmost", "Vacuous", "Valet", "Vignette", "Virtuoso", "Vocabulary", "Vogue", "Volatile", "Write",
    "Serendipity", "Vestibule", "Epitaph", "Connoisseur", "Ebullience", "Phantom", "Remnant", "Mourning", "Eccentric", "Havoc",
    "Ignoramus", "Jubilee", "Juxtaposition", "Longevity", "Magnanimous", "Nonchalant", "Omnipresent", "Perplexing", "Renaissance", "Supersede",
    "Utopian", "Whimsical", "Zealous", "Quandary", "Obelisk", "Gastronomy", "Mosaic", "Tranquility", "Alchemy", "Sapphire",
    "Sanctuary", "Clairvoyance", "Quagmire", "Nomadic", "Effervescent", "Cascade", "Opulent", "Luminous", "Opaque", "Ethereal",
    "Knight", "Gnome", "Wrist", "Bough", "Pneumonia", "Castle", "Salmon", "Corps", "Doubt", "Honest",
    "Heir", "Whistle", "Debt", "Knob", "Tomb", "Plumber", "Ballet", "Buffet", "Subtle", "Aisle",
    "Island", "Sword", "Hour", "Know", "Kneel", "Gnash", "Knack", "Knead", "Knee", "Knave",
    "Gnarl", "Gnat", "Pterodactyl", "Psychiatrist", "Pseudo", "Psyche", "Mnemonic", "Rhythm", "Wrought", "Rapport",
    "Folk", "Yolk", "Almond", "Listen", "Fasten", "Mortgage", "Cologne", "Scissors", "Autumn", "Biscuit",
    "Cache", "Chassis", "Climb", "Comb", "Coup", "Echo", "Gnash", "Gnaw", "Knife", "Knob",
    "Knoll", "Knock", "Knowledge", "Lamb", "Psalm", "Receipt", "Subtle", "Sword", "Whistle", "Wrestle",
    "Wrinkle", "Wrong", "Wrote", "Wrist", "Write", "Bison", "Debris", "Doubt", "Ghost", "Knickers",
    "Knit", "Kneel", "Wrangle", "Wrath", "Wreath", "Wrinkle", "Writhing", "Glisten", "Moisten", "Forecastle",
    "Knuckle", "Plague", "Height", "Subtle", "Fasten", "Muscle", "Ascend", "Descend", "Tsunami", "Sovereign",
    "Resign", "Doubtful", "Receipt", "Knave", "Gnome", "Writhing", "Wrought", "Knighted", "Boughs", "Lambing",
    "Castle", "Hymn", "Malign", "Condemn", "Resumption", "Palm", "Wren", "Aplomb", "Bomb", "Thumb",
    "Climber", "Plumber", "Debt-free", "Psychic", "Psychosis", "Pharaoh", "Wrangler", "Pteranodon", "Mnemonicist", "Knife-edge",
    "Epitome", "Niche", "Genre", "Cache", "Paradigm", "Ballet", "Debris", "Bourgeois", "Receipt", "Buffet",
    "Regime", "Colonel", "Worcester", "Queue", "Quay", "Bouquet", "Moet", "Forte", "Hyperbole", "Antique",
    "Liaison", "Poignant", "Déjà vu", "Ricochet", "Croissant", "Silhouette", "Sovereign", "Chassis", "Harass", "Gourmet",
    "Depot", "Visage", "Camouflage", "Giraffe", "Zebra", "Clique", "Antique", "Foyer", "Chauffeur", "Faux",
    "Coup", "Résumé", "Mirage", "Tableau", "Escargot", "Regatta", "Alcove", "Cabaret", "Cachet", "Concierge",
    "Elite", "Embryo", "Chateau", "Naive", "Coquette", "Opaque", "Rendezvous", "Repertoire", "Bonhomie", "Debonair",
    "Bizarre", "Absurd", "Heirloom", "Guillotine", "Refugee", "Bureau", "Faux pas", "Rendezvous", "Buffet", "Vestige",
    "Epoch", "Dilemma", "Crochet", "Trebuchet", "Alcove", "Debutante", "Camouflage", "Silhouette", "Gourmand", "Chartreuse",
    "Plaque", "Gyrate", "Marquee", "Aisle", "Jubilant", "Coup", "Balletic", "Chicanery", "Fiancé", "Fillet",
    "Gallows", "Intrigue", "Archaeology", "Flamboyant", "Silhouette", "Lamentable", "Coiffure", "Renaissance", "Palindrome"
)
    wait(2)
    stys('clear')
    stys('cls')
    input_passage = input("Please Paste Passage Here:\n")

    newstring0 = input_passage.replace(".", "")
    newstring1 = newstring0.replace(",", "")
    newstring2 = newstring1.replace("!", "")
    cleaned_passage = newstring2.replace("?", "")

    OUT = 0
    IN = 1

    def countWords(word):
        state = OUT
        wc = 0
        for i in range(len(word)):

            if (word[i] == ' ' or word[i] == '\n' or word[i] == '\t'):
                state = OUT

            elif state == OUT:
                state = IN
                wc += 1
        return wc

    split_passage = list(cleaned_passage.split(" "))

    decodeable = [i for i in split_passage if i not in non_decodable_words]

    total_words = countWords(cleaned_passage)

    x_decodable = total_words - len(decodeable)
    decodable = (total_words - x_decodable)
    prec_non_decodeable = (decodable / total_words)*100

    prec_decodeable = prec_non_decodeable
    print('''------------------------------------------------------------

Your Passage is:''')
    print(round(prec_decodeable, 1), "% Decodable")

user1_password = ('test')
user1_username = ('test')

print('Welcome to PDC')
pdc()

# Thx to Geeks for Geeks and W3schools for Code Snippets
