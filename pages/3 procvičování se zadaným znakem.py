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





# CVIČENÍ 1
st.write("PROCVIČOVÁNÍ SE ZADANÝM ZNAKEM")
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
 prelozeno = "Napiš písmeno nebo číslo Morseovým písmem"
else:
 prelozeno = "CHYBA"

st.write('''Do horního textového pole napiš jeden Morseův kód (písmeno nebo číslici) 
         a do dolního odpovídající písmeno nebo číslici.
         Můžeš to zkusit i obráceně.''')
text = st.text_input("Latinské písmeno nebo arabská císlice:",max_chars=2,key="text",placeholder="Q")

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



















 