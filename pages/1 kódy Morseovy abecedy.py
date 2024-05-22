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
#>> cd Desktop\python2
#
# 3. Pro spusteni programu spustis tohle:
#>> streamlit run "home.py"


st.write("KÓDY MORSEOVY ABECEDY")
st.write("Písmena")
st.write("'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'CH': '----', 'I': '..', 'J': '.---', 'K': '-.-',")
st.write("'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',")
st.write("'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/'")
st.write("Číslice")
st.write("'1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'")
st.write("Speciální znaky")
st.write("',': '--..--', '.': '.-.-.-', ':': '---...', ';': '-.-.-.', '?': '..--..', '!': '--..-', '-': '-....-', '/': '-..-.', '=': '-...-', '_': '..--.-',")
st.write(" '''': '.-..-.', '(': '-.--.', ')': '-.--.-', '<->': '.----.', '@': '.--.-., '+': '.-.-.'")
st.write("Zvláštní znaky")
st.write("'Začátek vysílání': '-.-.-.-.', 'Konec vysílání': '...-.-', 'Rozumím': '----.-', 'Nerozumím': '.......',")
st.write("'Pomaleji': '-.-.-..', 'Čekejte': '.-...', 'Omyl': './././././.', 'Opakuji': '../../../../../..',")
st.write("'Pomoc': '.../---/...'")

st.write("Pomocná slova")
html_content = """
<table style="width:100%; text-align:center; border-collapse: collapse; table-layout: fixed;">
     
  <tr> 
    <td style="border: 1px solid black;background-color: lightblue;" colspan="3">Písmeno</td>
    <td style="border: 1px solid black;background-color: lightblue;" colspan="3">Kód</td>
    <td style="border: 1px solid black;background-color: lightblue;" colspan="3">Pomocné slovo</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">A</td>
    <td style="border: 1px solid black;" colspan="3">.-</td>
    <td style="border: 1px solid black;" colspan="3">a kát</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">B</td>
    <td style="border: 1px solid black;" colspan="3">-...</td>
    <td style="border: 1px solid black;" colspan="3">blý ska vi ce</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">C</td>
    <td style="border: 1px solid black;" colspan="3">-.-.</td>
    <td style="border: 1px solid black;" colspan="3">cí lov ní ci</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">D</td>
    <td style="border: 1px solid black;" colspan="3">-..</td>
    <td style="border: 1px solid black;" colspan="3">dá la va</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">E</td>
    <td style="border: 1px solid black;" colspan="3">.</td>
    <td style="border: 1px solid black;" colspan="3">erb</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">F</td>
    <td style="border: 1px solid black;" colspan="3">..-.</td>
    <td style="border: 1px solid black;" colspan="3">Fi li pí ny</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">G</td>
    <td style="border: 1px solid black;" colspan="3">--.</td>
    <td style="border: 1px solid black;" colspan="3">Grón ská_zem</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">H</td>
    <td style="border: 1px solid black;" colspan="3">....</td>
    <td style="border: 1px solid black;" colspan="3">hra cho vi na</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">CH</td>
    <td style="border: 1px solid black;" colspan="3">----</td>
    <td style="border: 1px solid black;" colspan="3">chvá tá k_nám_sám</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">I</td>
    <td style="border: 1px solid black;" colspan="3">..</td>
    <td style="border: 1px solid black;" colspan="3">i bis</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">J</td>
    <td style="border: 1px solid black;" colspan="3">.---</td>
    <td style="border: 1px solid black;" colspan="3">jas mín_bí lý</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">K</td>
    <td style="border: 1px solid black;" colspan="3">-.-</td>
    <td style="border: 1px solid black;" colspan="3">krá ko rá</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">L</td>
    <td style="border: 1px solid black;" colspan="3">.-..</td>
    <td style="border: 1px solid black;" colspan="3">lu pí ne ček</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">M</td>
    <td style="border: 1px solid black;" colspan="3">--</td>
    <td style="border: 1px solid black;" colspan="3">má vá</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">N</td>
    <td style="border: 1px solid black;" colspan="3">-.</td>
    <td style="border: 1px solid black;" colspan="3">ná rod</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">O</td>
    <td style="border: 1px solid black;" colspan="3">---</td>
    <td style="border: 1px solid black;" colspan="3">ó_náš_pán</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">P</td>
    <td style="border: 1px solid black;" colspan="3">.--.</td>
    <td style="border: 1px solid black;" colspan="3">pa pír ní ci</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">Q</td>
    <td style="border: 1px solid black;" colspan="3">--.-</td>
    <td style="border: 1px solid black;" colspan="3">kví lí or_kán</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">R</td>
    <td style="border: 1px solid black;" colspan="3">.-.</td>
    <td style="border: 1px solid black;" colspan="3">ra rá šek</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">S</td>
    <td style="border: 1px solid black;" colspan="3">...</td>
    <td style="border: 1px solid black;" colspan="3">so bo ta</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">T</td>
    <td style="border: 1px solid black;" colspan="3">.</td>
    <td style="border: 1px solid black;" colspan="3">tón</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">U</td>
    <td style="border: 1px solid black;" colspan="3">..-</td>
    <td style="border: 1px solid black;" colspan="3">u če ný</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">V</td>
    <td style="border: 1px solid black;" colspan="3">...-</td>
    <td style="border: 1px solid black;" colspan="3">vy vo le ný</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">W</td>
    <td style="border: 1px solid black;" colspan="3">.--</td>
    <td style="border: 1px solid black;" colspan="3">dvo jité_vé</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">X</td>
    <td style="border: 1px solid black;" colspan="3">-..-</td>
    <td style="border: 1px solid black;" colspan="3">Xé no kra tés</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">Y</td>
    <td style="border: 1px solid black;" colspan="3">-.--</td>
    <td style="border: 1px solid black;" colspan="3">Ý kar_má vá</td>    
  </tr>
  <tr> 
    <td style="border: 1px solid black;" colspan="3">Z</td>
    <td style="border: 1px solid black;" colspan="3">--..</td>
    <td style="border: 1px solid black;" colspan="3">zrá dná_že na</td>    
  </tr>

  

</table>
"""



# Display the HTML content in Streamlit
st.markdown(html_content, unsafe_allow_html=True)

st.write(" ")
st.write("Dešifrovací tabulka Morseovy abecedy")
# Define the HTML content
html_content = """
<table style="width:100%; text-align:center; border-collapse: collapse; table-layout: fixed;">
     
  <tr> 
    <td style="border: 1px solid black;background-color: lightblue;" colspan="16">- T</td>
    <td style="border: 1px solid black;" colspan="16">. E</td>   
  </tr>

  <tr>
    <td style="border: 1px solid black;background-color: lightblue;" colspan="8">- M</td>
    <td style="border: 1px solid black;" colspan="8">. N</td>
    <td style="border: 1px solid black;background-color: lightblue;" colspan="8">- A</td>
    <td style="border: 1px solid black;" colspan="8">. I</td>
  </tr>

  <tr>
    <td style="border: 1px solid black;background-color: lightblue;" colspan="4">- O</td>
    <td style="border: 1px solid black;" colspan="4">. G</td>
    <td style="border: 1px solid black;background-color: lightblue;" colspan="4">- K</td>
    <td style="border: 1px solid black;" colspan="4">. D</td>
    <td style="border: 1px solid black;background-color: lightblue;" colspan="4">- W</td>
    <td style="border: 1px solid black;" colspan="4">. R</td>
    <td style="border: 1px solid black;background-color: lightblue;" colspan="4">- U</td>
    <td style="border: 1px solid black;" colspan="4">. S</td>
  </tr>

  <tr>  
    <td style="border: 1px solid black;background-color: lightblue;" colspan="2">-CH</td>
    <td style="border: 1px solid black;" colspan="2">. Ö</td>
    <td style="border: 1px solid black;background-color: lightblue;" colspan="2">- Q</td>
    <td style="border: 1px solid black;" colspan="2">. Z</td>
    <td style="border: 1px solid black;background-color: lightblue;" colspan="2">- Y</td>
    <td style="border: 1px solid black;" colspan="2">. C</td>
    <td style="border: 1px solid black;background-color: lightblue;" colspan="2">- X</td>
    <td style="border: 1px solid black;" colspan="2">. B</td>
    <td style="border: 1px solid black;background-color: lightblue;" colspan="2">- J</td>
    <td style="border: 1px solid black;" colspan="2">. P</td>
    <td style="border: 1px solid black;background-color: lightblue;" colspan="2">- Ä</td>
    <td style="border: 1px solid black;" colspan="2">. L</td>
    <td style="border: 1px solid black;background-color: lightblue;" colspan="2">- Ü</td>
    <td style="border: 1px solid black;" colspan="2">. F</td>
    <td style="border: 1px solid black;background-color: lightblue;" colspan="2">- V</td>
    <td style="border: 1px solid black;" colspan="2">. H</td>
  </tr>

</table>
"""



# Display the HTML content in Streamlit
st.markdown(html_content, unsafe_allow_html=True)
st.write("_______________________________________________")











 