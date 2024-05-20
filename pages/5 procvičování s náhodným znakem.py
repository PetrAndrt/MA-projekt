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
st.write("_______________________________________________")












 