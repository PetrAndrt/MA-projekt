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
#>> #>> streamlit run 3.TEXT.py


morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/', 'CH': '----'
}

def text_to_morse(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
    }
    return ' '.join(morse_code_dict.get(char, '') for char in text)

# Define the morse_to_text function
def morse_to_text(morse):
    morse_code_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', 
        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', 
        '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', 
        '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', 
        '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '/': ' '
    }
    return ''.join(morse_code_dict.get(char, '') for char in morse.split())

# Streamlit interface
st.write("2. TEXT")

# Input for text in Latin alphabet
text_abeceda = st.text_input('Napiš text v latinské abecedě:', 
                             placeholder="Ab1Cd 2Ef3Gn4CHi5Jk6Lm7", 
                             key="abeceda", 
                             max_chars=48).upper()
if text_abeceda:
    morseova_abeceda = text_to_morse(text_abeceda)
    st.write(morseova_abeceda)

# Input for text in Morse code
text_abeceda_2 = st.text_input('Napiš text v morseových kódech:', 
                               placeholder=".- -... .---- -.-. -.. / ..--- . ..-. ...-- --. / -. ....- ---- .. / ..... .--- -.- -.... .-.. / -- --...", 
                               key="abeceda_2", 
                               max_chars=108)
if text_abeceda_2:
    latin_abeceda = morse_to_text(text_abeceda_2)
    st.write(latin_abeceda)

# Display Morse code reference
st.write("'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'CH': '----', 'I': '..', 'J': '.---', 'K': '-.-',")
st.write("'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',")
st.write("'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/',")
st.write("'1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'")













 