#streamlit
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd

#Animationen
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

# Hier wird zunächst der berechnete Verbrauch erfasst
# Als Beispielwert wird eine Stromgenerierung von 100 kWh pro Jahr genommen.
generierung_total = 100
print("Super! Dein Balkonmodul würde jährlich",generierung_total, "kWh erzeugen!")
print("Im Folgenden eine kleine Übersicht über verschiedene Geräte, welche den erzeugten Strom nutzen könnten:")

# Um die Vergleiche der Haushaltsgeräte möglichst greifbar zu gestalten, wird die Stromgenerierung (alle in kWh) auf verschiedene Ebenen heruntergebrochen
generierung_jahr = generierung_total
generierung_monat = generierung_total/12
generierung_tag = generierung_total/365
generierung_woche = generierung_total/52
generierung_stunde = generierung_tag/24

#Kühlschrank (108 kWh pro Jahr)
nutzung_kuehlschrank = round(generierung_jahr/108*12)
print("\n\nDein Kühlschrank könnte mit bei einer jährlichen Generierung von",generierung_total, "kWh insgesamt für ca.",nutzung_kuehlschrank, "Monate laufen!")

#Toaster (0,05 kWh für 2 Scheiben)
nutzung_toaster = round(generierung_tag/0.05)
print("\nTäglich könntest Du mit den", generierung_total, "kWh für Dein Frühstück ca.", nutzung_toaster, "Scheiben Toast toasten!")



#Föhn (0,03 kWh für 1 Minuten Nutzung bzw. 1,8 kWh für eine Stunde Nutzung)
nutzung_foehn_tag = round(generierung_tag/0.03)
nutzung_foehn_woche = round(generierung_woche / 0.03)
print("\nMit", generierung_total, "kWh könntest Du Dir täglich für ca.", nutzung_foehn_tag, "Minuten die Haare föhnen. In der Woche wären es ca.", nutzung_foehn_woche, "Minuten")



#Router (88 kWh pro Jahr bzw. 0,24 kWh pro Tag)
nutzung_router = round( generierung_jahr/0.24)
print("\nDein Internet-Router könnte für ca.", nutzung_router, "Tage über Deinen eigenen Solarstrom laufen!")



#Waschmaschine (0.8 kWh pro Waschgang)
nutzung_waschmaschine = round(generierung_woche/0.8)
print("\nWöchentlich könntest Du mit den jährlichen", generierung_total, "kWh ca.", nutzung_waschmaschine,"mal eine handelsübliche Waschmaschine bedienen.")



#Handyladung (0,02 kWh pro Handyladung)
nutzung_handy = round(generierung_tag/0.02)
print("\nDein Smartphone könntest Du mithilfe des Balkonmoduls ca.", nutzung_handy, "mal am Tag laden!")



#TV (0,1 kWh pro Stunde)
nutzung_tv = round(generierung_tag/0.1)
print("\nTäglich könntest Du ca.", nutzung_tv,"Stunden mithilfe Deiner Solarenergie fernsehen!")



st.set_page_config(page_title="Haushaltsgeraete", page_icon=":+1:", layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Im Folgenden eine Übersicht über Haushaltsgeräte, welche sich (teilweise) mit dem Balkonkraftwerk betreiben ließen!")
    st.title ("Haushaltsgeräte")
    st.write("Super! :tada: Dein Balkonmodul würde jährlich",generierung_total, "kWh erzeugen!")

# ---- TEXTKÖRPER ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Haushaltsgeräte")
        st.write("##")
        st.write("Beim Betrachten verschiedener Haushaltsgeräte ergeben sich folgende Möglichkeiten:")
        st.write("##")
        st.write("- Dein Kühlschrank könnte beispielsweise mit bei einer jährlichen Generierung von",generierung_total, "kWh insgesamt für ca.",nutzung_kuehlschrank,"Monate laufen!")
        lottie_fridge = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_VRZFwr.json")
        st_lottie(lottie_fridge, height=150)
        st.write("##")
        st.write("- Täglich könntest Du mit den", generierung_total, "kWh für Dein Frühstück ca.", nutzung_toaster, "Scheiben Toast toasten!")
        lottie_toaster = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_k8WCTV.json")
        st_lottie(lottie_toaster, height=150)
        st.write("##")
        st.write("- Mit", generierung_total, "kWh könntest Du Dir täglich für ca.", nutzung_foehn_tag, "Minuten die Haare föhnen. In der Woche wären es ca.", nutzung_foehn_woche, "Minuten")
        st.write("##")
        st.write("- Dein Internet-Router könnte für ca.", nutzung_router, "Tage über Deinen eigenen Solarstrom laufen!")
        lottie_router = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_v1mq5ba4.json")
        st_lottie(lottie_router, height=150)
        st.write("##")
        st.write("- Wöchentlich könntest Du mit den jährlichen", generierung_total, "kWh ca.", nutzung_waschmaschine,"mal eine handelsübliche Waschmaschine nutzen.")
        lottie_waschmaschine = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_3xjhagvt.json")
        st_lottie(lottie_waschmaschine, height=150)
        st.write("##")
        st.write("- Dein Smartphone könntest Du mithilfe des Balkonmoduls ca.", nutzung_handy, "mal am Tag laden!")
        lottie_smartphone = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_ka1ozotw.json")
        st_lottie(lottie_smartphone, height=150)
        st.write("##")
        st.write("- Täglich könntest Du ca.", nutzung_tv,"Stunden mithilfe Deiner Solarenergie fernsehen!")
        lottie_tv = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_wX69nA.json")
        st_lottie(lottie_tv, height=150)