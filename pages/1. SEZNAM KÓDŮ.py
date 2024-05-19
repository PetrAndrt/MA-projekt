import streamlit as st
import json
import time
import datetime as dt
import random
import string

# py_como_lekce\Scripts\activate
# 1. Po spusteni programu nainstalujes timhle:
#>> pip install streamlit
#
# 2. Az to dobehne, napis tohle:
#>> cd Desktop\PYTHON
#
# 3. Pro spusteni programu spustis tohle:
#>> streamlit run 1._SEZNAM_KÓDŮ.py

st.write("SEZNAM KÓDŮ")
st.write("'A'  'a kát' .-, 'B'  'blý ska vi ce' -..., 'C'    'cí lov ní ci' -.-.,'D'   'dá la va' -..,'E'  'erb' ., 'F'  'Fi li pí ny' ..-. ")
st.write("'G'  'Grón ská_zem' --., 'H'  'hra cho vi na' ...., 'CH'  'chléb nám dá vá' ----,'I'  'i bis' ..")
st.write("'J'  'jas mín_bí lý' .---,'K'  'krá ko rá' -.-, 'L'  'lu pí ne ček' .-.., 'M'   'má vá' --,'N'  'ná rod' -.")
st.write("'O'  'ó_náš_pán' ---, 'P'  'pa pír ní ci' .--., 'Q'  'kví lí_or kán' --.-, 'R'  'ra rá šek' .-.")
st.write("'S'  'so bo ta' ..., 'T'  'tón' -, 'U'  'u če ný' ..-, 'V'  'vy vo le ný' ...-, 'W'  'Xé no kra tés' -..- ")
st.write("'X' 'Xé no kra tés' -..-, 'Y'  'Ý kar_má vá' -.--, 'Z' 'zrá dná_že na' --.. ")
st.write
skola = st.text_input("Napiš písmeno, číslici nebo znak:", key="skola_1", max_chars=2).upper()
if st.button("Ukaž"):
    if skola == "A":
        st.write("'a kát' .-")
    elif skola == "B":
        st.write("'blý ska vi ce' -...")
    elif skola == "C":
        st.write("'cí lov ní ci' -.-.")
    elif skola == "D":
        st.write("'dá la va' -..")
    elif skola == "E":
        st.write("'erb' .")
    elif skola == "F":
        st.write("'Fi li pí ny' ..-.")
    elif skola == "G":
        st.write("'Grón ská_zem' --.")
    elif skola == "H":
        st.write("'hra cho vi na' ....")
    elif skola == "CH":
        st.write("'chléb nám dá vá' ----")
    elif skola == "I":
        st.write("'i bis' ..")
    elif skola == "J":
        st.write("'jas mín_bí lý' .---")
    elif skola == "K":
        st.write("'krá ko rá' -.-")
    elif skola == "L":
        st.write("'lu pí ne ček' .-..")
    elif skola == "M":
        st.write("'má vá' --")
    elif skola == "N":
        st.write("'ná rod' -.")
    elif skola == "O":
        st.write("'ó_náš_pán' ---")
    elif skola == "P":
        st.write("'pa pír ní ci' .--.")
    elif skola == "Q":
        st.write("'kví lí_or kán' --.-")
    elif skola == "R":
        st.write("'ra rá šek' .-.")
    elif skola == "S":
        st.write("'so bo ta' ...")
    elif skola == "T":
        st.write("'tón' -")
    elif skola == "U":
        st.write("'u če ný' ..-")
    elif skola == "V":
        st.write("'vy vo le ný' ...-")
    elif skola == "W":
        st.write("'dvoj jité vé' .--")
    elif skola == "X":
        st.write("'Xé no kra tés' -..-")
    elif skola == "Y":
        st.write("'Ý kar_má vá' -.--")
    elif skola == "Z":
        st.write("'zrá dná_že na' --..")
    elif skola == "0":
        st.write("-----")
    elif skola == "1":
        st.write(".----")
    elif skola == "2":
        st.write("..---")
    elif skola == "3":
        st.write("...--")
    elif skola == "4":
        st.write("....-")
    elif skola == "5":
        st.write(".....")
    elif skola == "6":
        st.write("-....")
    elif skola == "7":
        st.write("--...")
    elif skola == "8":
        st.write("---..")
    elif skola == "9":
        st.write("----.")
    elif skola == ".":
        st.write("'tečka'.-.-.-")
    elif skola == ",":
        st.write("'čárka'--..--")
    elif skola == "?":
        st.write("'otazník'..--..")
    elif skola == "!":
        st.write("'vykřičník'--...-")
    elif skola == ";":
        st.write("'středník'-.-.-.")
    elif skola == ":":
        st.write("'dvojtečka'---...")
    elif skola == "(":
        st.write("'kulatá závorka otevírací'-.--.")
    elif skola == ")":
        st.write("'kulatá závorka zavírací'-.--.-")
    elif skola == '"':
        st.write("'uvozovky'.-..-.")
    elif skola == "_":
        st.write("'podtržítko'..--.-")
    elif skola == "@":
        st.write("'zavináč'.--.-")
    elif skola == "-":
        st.write("'pomlčka'-....-")
    elif skola == "/":
        st.write("'lomítko'-..-.")
    elif skola == "=":
        st.write("'rovnítko'-...-")
    else:
        st.write("Není zaznamenán")
else:
    st.write("")

st.write("_______________________________________________")
# TEXTY


# Slovníky pro převod mezi latinskou abecedou a Morseovou abecedou
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/', 'CH': '----'
}

latin_code_dict = {v: k for k, v in morse_code_dict.items()}

def text_to_morse(text):
    morse_text = []
    i = 0
    while i < len(text):
        if text[i:i+2] == 'CH':
            morse_text.append(morse_code_dict['CH'])
            i += 2
        else:
            morse_text.append(morse_code_dict.get(text[i], ''))
            i += 1
    return ' '.join(morse_text)

def morse_to_text(morse):
    words = morse.split('/')
    translated_text = []
    for word in words:
        characters = word.split()
        translated_word = ''.join(latin_code_dict.get(char, '') for char in characters)
        translated_text.append(translated_word)
    return ' '.join(translated_text)

st.write("2. TEXT")
text_abeceda = st.text_input('Napiš text v latinské abecedě:', placeholder="Ab1Cd 2Ef3Gn4CHi5Jk6Lm7", 
                             key="abeceda", max_chars=48).upper()
if text_abeceda:
    morseova_abeceda = text_to_morse(text_abeceda)
    st.write(morseova_abeceda)

text_abeceda_2 = st.text_input('Napiš text v morseových kódech:', placeholder=".- -... .---- -.-. -.. / ..--- . ..-. ...-- --. / -. ....- ---- .. / ..... .--- -.- -.... .-.. / -- --...", 
                             key="abeceda_2", max_chars=108)
if text_abeceda_2:
    latin_abeceda = morse_to_text(text_abeceda_2)
    st.write(latin_abeceda)
st.write("'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..,' 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'CH': '----', 'I': '..', 'J': '.---', 'K': '-.-',")
st.write("'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',")
st.write("'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/',")
st.write("'1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'.")
# A: .-, B: -..., C: -.-., D: -.., E: ., F: ..-., G: --., H: ...., CH: ----, I: .., J: .---, K: -.-, L: .-.., M: --, N: -., O: ---, 
# P: .--., Q: --.-, R: .-. S: ..., T: -, U: ..-, V: ...-, W: .--, X: -..-, Y: -.--, Z: --.., 
# 0: -----, 1: .----, 2: ..---, 3: ...--, 4: ....-, 5: ....., 6: -...., 7: --..., 8: ---.., 9: ----., ' ': '/', 

# Použití slovníků: Vytvořil jsem dva slovníky: morse_code_dict pro převod z latinské abecedy na Morseovu abecedu a latin_code_dict pro převod zpět.
# Funkce pro převod:
# text_to_morse: Převádí text z latinské abecedy na Morseovu abecedu. Zohledňuje speciální případ pro 'CH'.
# morse_to_text: Převádí text z Morseovy abecedy zpět na latinskou abecedu. Zohledňuje mezery mezi slovy (nahrazené '/' v Morseově kódu).
# Interaktivní vstupy a výstupy: Upravil jsem vstupy a výstupy tak, aby využívaly tyto funkce a správně zobrazovaly převody.
st.write("_______________________________________________")

# CVIČENÍ 1
st.write("3. PROCVIČOVÁNÍ SE ZADANÝM ZNAKEM")
morseova_abeceda_2 = st.text_input("Morseův kód:",max_chars=5,key="cviceni",placeholder="--.-")
if morseova_abeceda_2 == "-----":
 prelozeno = "0"
elif morseova_abeceda_2 == ".----":
 prelozeno = "1"
elif morseova_abeceda_2 == "..---":
 prelozeno = "2"
elif morseova_abeceda_2 == "...--":
 prelozeno = "3"
elif morseova_abeceda_2 == "....-":
 prelozeno = "4"
elif morseova_abeceda_2 == "-----":
 prelozeno = "5"
elif morseova_abeceda_2 == "-....":
 prelozeno = "6"
elif morseova_abeceda_2 == "--...":
 prelozeno = "7"
elif morseova_abeceda_2 == "---..":
 prelozeno = "8"
elif morseova_abeceda_2 == "----.":
 prelozeno = "9"
elif morseova_abeceda_2 == "-...":
 prelozeno = "B"and"b"
elif morseova_abeceda_2 == "-.-.":
 prelozeno = "C"and"c"
elif morseova_abeceda_2 == "..-.":
 prelozeno = "F"and"f"
elif morseova_abeceda_2 == "....":
 prelozeno = "H"and"h"
elif morseova_abeceda_2 == "----":
 prelozeno = "CH"and"Ch"and"ch"
elif morseova_abeceda_2 == ".---":
 prelozeno = "J"and"j"
elif morseova_abeceda_2 == ".-..":
 prelozeno = "L"and"l"
elif morseova_abeceda_2 == ".--.":
 prelozeno = "P"and"p"
elif morseova_abeceda_2 == "--.-":
 prelozeno = "Q"and"q"
elif morseova_abeceda_2 == "...-":
 prelozeno = "V"and"v"
elif morseova_abeceda_2 == "-..-":
 prelozeno = "X"and"x"
elif morseova_abeceda_2 == "-.--":
 prelozeno = "Y"and"y"
elif morseova_abeceda_2 == "--..":
 prelozeno = "Z"and"z"
elif morseova_abeceda_2 == "-..":
 prelozeno = "D"and"d"
elif morseova_abeceda_2 == "--.":
 prelozeno = "G"and"g"
elif morseova_abeceda_2 == "-.-":
 prelozeno = "K"and"k"
elif morseova_abeceda_2 == "---":
 prelozeno = "O"and"o"
elif morseova_abeceda_2 == ".-.":
 prelozeno = "R"and"r"
elif morseova_abeceda_2 == "...":
 prelozeno = "S"and"s"
elif morseova_abeceda_2 == "..-":
 prelozeno = "U"and"u"
elif morseova_abeceda_2 == ".--":
 prelozeno = "W"and"w"
elif morseova_abeceda_2 == ".-":
 prelozeno = "A"and"a"
elif morseova_abeceda_2 == "..":
 prelozeno = "I"and"i"
elif morseova_abeceda_2 == "--":
 prelozeno = "M"and"m"
elif morseova_abeceda_2 == "-.":
 prelozeno = "N"and"n"
elif morseova_abeceda_2 == ".":
 prelozeno = "E"and"e"
elif morseova_abeceda_2 == "-":
 prelozeno = "T"and"t"
elif morseova_abeceda_2 == "":
 prelozeno = "Napiš písmeno nebo číslo morseovým písmem"
else:
 prelozeno = "CHYBA"

st.write('''Do horního textového pole napiš jeden morseův kód 
         a do dolního odpovídající písmeno nebo číslici.
         Můžeš to zkusit i obráceně.''')
text = st.text_input("Latinsé písmeno nebo arabská císlice:",max_chars=1,key="text",placeholder="Q")

if prelozeno == "CHYBA":
    st.write("Tohle přece neexistuje.")
else:
    if morseova_abeceda_2 != "" and text != "":
        if text == prelozeno:
            st.write("Dobrá práce.")
        else: 
            st.write("Nevadí, zkus to znovu.")
if text:
 velka_pismena = text.upper()
else:
 velka_pismena = text
 st.write("_______________________________________________")

# CVIČENÍ 2
st.write("4. PROCVIČOVÁNÍ S NÁHODNÝM ZNAKEM")



def generate_random_character():
    characters = string.ascii_letters + string.digits
    return random.choice(characters)

# Generování náhodného písmena nebo číslice
if st.button("Náhodný znak",key="nahodny_znak_1"):
    random_character = generate_random_character()
    st.session_state["random_character"] = random_character
    st.write("Náhodné písmeno nebo číslice:", random_character)
# Kontrola náhodného znaku proti uživatelskému vstupu
if "random_character" in st.session_state:
    random_character = st.session_state["random_character"]
    znak = st.text_input("Zadej znak:", key="test_1")

    if st.button("Kontrola",key="kontrola_1"):
        morse_code = {
            "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.",
            "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.",
            "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-",
            "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", "0": "-----",
            "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
            "7": "--...", "8": "---..", "9": "----."
        }
  # Kontrola, zda je znak v Morseově kódu
        if random_character.lower() in morse_code:
            expected_morse = morse_code[random_character.lower()]
            if znak == expected_morse:
                st.write("Dobře")
            else:
                st.write("Špatně")
        else:
            st.write("Náhodný znak není podporován pro kontrolu Morseova kódu")
else:
    st.write("Klikněte na 'Náhodný znak' pro generování znaku")




#def generate_random_character():
#    characters = string.ascii_letters + string.digits
#    return random.choice(characters)

## Generování náhodného písmena nebo číslice
#if st.button("Náhodný znak",key="nahodny_znak_2"):
#    random_character = generate_random_character()
#    st.session_state["random_character"] = random_character
#    st.write("Náhodné písmeno nebo číslice:", random_character)

## Kontrola náhodného znaku proti uživatelskému vstupu
#if "random_character" in st.session_state:
#    random_character = st.session_state["random_character"]
#    st.write("Náhodné písmeno nebo číslice:", random_character)  # Ukazuje znovu náhodný znak
#    znak = st.text_input("Zadej Morseův kód", key="text_2")

#    if st.button("Kontrola",key="kontrola_2"):
#        morse_code = {
#            "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.",
#            "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.",
#            "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-",
#            "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", "0": "-----",
#            "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
#            "7": "--...", "8": "---..", "9": "----."
#        }
#        # Kontrola, zda je znak v Morseově kódu
#        if random_character.lower() in morse_code:
#            expected_morse = morse_code[random_character.lower()]
#            if znak == expected_morse:
#                st.write("Dobře")
#            else:
#            st.write("Náhodný znak není podporován pro kontrolu Morseova kódu")
#else:
#    st.write("Klikněte na 'Náhodný znak' pro generování znaku")





# "a" or "A" == ".-"
# "b" or "B" == "-..."
# "c" or "C" == "-.-."
# "d" or "D" == "-.."
# "f" or "F" == "..-."
# "g" or "G" == "--."
# "h" or "H" == "...."
# "i" or "I" == ".."
# "j" or "J" == ".---"
# "k" or "K" == "-.-"
# "l" or "L" == ".-.."
# "m" or "M" == "--"
# "n" or "N" == "-."
# "o" or "O" == "---"
# "p" or "P" == ".--."
# "q" or "Q" == "--.-"
# "r" or "R" == ".-."
# "s" or "S" == "..."
# "t" or "T" == "-"
# "u" or "U" == "..-"
# "v" or "V" == "...-"
# "w" or "W" == ".--"
# "x" or "X" == "-..-"
# "y" or "Y" == "-.--"
# "z" or "Z" == "--.."
# "0" == "" "-----"
# "1" == "" ".----"
# "2" == "" "..---"
# "3" == "" "...--"
# "4" == "" "....-"
# "5" == "" "....."
# "6" == "" "-...."
# "7" == "" "--..."
# "8" == "" "---.."
# "9" == "" "----."







 