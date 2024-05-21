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
    st.session_state['skola_2'] = ''

# Kontrola stisknutí tlačítka
if st.button("Ukaž"):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
        '?': '..--..', '!': '--...-', ';': '-.-.-.', ':': '---...', '(': '-.--.', ')': '-.--.-', '"': '.-..-.',
        '_': '..--.-', '@': '.--.-', '-': '-....-', '/': '-..-.', '=': '-...-', '+': '.-.-.', 'CH': '----'
    }

    if skola in morse_code_dict:
        st.write(f"Morseův kód: {morse_code_dict[skola]}")
    else:
        st.write("Není zaznamenán")

    # Reset textového vstupu
    reset_text_input()

# Morseovka slovníky a funkce
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

# Textový vstup pro převod na Morseovku
text_input = st.text_input("Napiš text pro převod do Morseovy abecedy:", key="text_input")

if st.button("Převést na Morseovku"):
    morse_output = text_to_morse(text_input.upper())
    st.write(f"Morseova abeceda: {morse_output}")

# Textový vstup pro převod z Morseovky
morse_input = st.text_input("Napiš text v Morseových kódech (písmena a číslice):", key="morse_input")

if st.button("Převést na text"):
    text_output = morse_to_text(morse_input)
    st.write(f"Přeložený text: {text_output}")

# Zobrazení oddělovače
st.write("_______________________________________________")











 