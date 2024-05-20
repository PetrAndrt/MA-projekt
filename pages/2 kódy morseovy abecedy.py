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
#>> streamlit run morseova_abeceda.py

# Nastavení nadpisu
st.write("KÓDY MORSEOVY ABECEDY")

# Textový vstup
skola = st.text_input("Napiš písmeno, číslici nebo speciální znak:", key="skola_2", max_chars=2).upper()

# Diagnostický výstup pro kontrolu hodnoty
st.write(f"Zadaný znak: {skola}")

# Funkce pro resetování text_input
def reset_text_input():
    st.session_state['skola_1'] = ''

# Kontrola stisknutí tlačítka
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
        st.write("'tečka' .-.-.-")
    elif skola == ",":
        st.write("'čárka' --..--")
    elif skola == "?":
        st.write("'otazník' ..--..")
    elif skola == "!":
        st.write("'vykřičník' --...-")
    elif skola == ";":
        st.write("'středník' -.-.-.")
    elif skola == ":":
        st.write("'dvojtečka' ---...")
    elif skola == "(":
        st.write("'kulatá závorka otevírací' -.--.")
    elif skola == ")":
        st.write("'kulatá závorka zavírací' -.--.-")
    elif skola == '"':
        st.write("'uvozovky' .-..-.")
    elif skola == "_":
        st.write("'podtržítko' ..--.-")
    elif skola == "@":
        st.write("'zavináč' .--.-")
    elif skola == "-":
        st.write("'pomlčka' -....-")
    elif skola == "/":
        st.write("'lomítko' -..-.")
    elif skola == "=":
        st.write("'rovnítko' -...-")
    else:
        st.write("Není zaznamenán")

    # Reset textového vstupu
    reset_text_input()

# Morseovka slovníky a funkce
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

# Zobrazení oddělovače
st.write("_______________________________________________")











 