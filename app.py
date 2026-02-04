import streamlit as st
import time
import random

# =================================================================
# 1. CONFIGURAZIONE E STILE "SALOTTO DEL SOMMELIER"
# =================================================================
st.set_page_config(page_title="Gaspare Sommelier", page_icon="🤵‍♂️", layout="centered")

st.markdown("""
<style>
    header {visibility: hidden !important;}
    .main { background-color: #fdfaf5; }
    
    /* STILE FUMETTO */
    .bubble {
        position: relative;
        background: #ffffff;
        border: 2px solid #800020;
        border-radius: 20px;
        padding: 15px;
        margin-bottom: 20px;
        text-align: center;
        font-weight: bold;
        color: #333;
    }
    .bubble:after {
        content: '';
        position: absolute;
        bottom: -15px;
        left: 50%;
        border-width: 15px 15px 0;
        border-style: solid;
        border-color: #800020 transparent;
        display: block;
        width: 0;
        margin-left: -15px;
    }
    
    /* ANIMAZIONE SCHEDA VINO */
    @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    .wine-card {
        animation: fadeIn 0.8s ease-out;
        text-align: center;
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        margin-bottom: 20px;
        border: 1px solid #eee;
    }
    .wine-title { color: #b00000; font-size: 30px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# =================================================================
# 2. IL PERSONAGGIO (Gaspare)
# =================================================================
def parla_gaspare(messaggio):
    st.markdown(f'<div class="bubble">{messaggio}</div>', unsafe_allow_html=True)
    # Immagine di un sommelier (Placeholder elegante)
    st.markdown("<h1 style='text-align: center; font-size: 80px;'>🤵‍♂️</h1>", unsafe_allow_html=True)

# =================================================================
# 3. DATABASE VINI (Esempio ridotto per test)
# =================================================================
vini = [
    {"nome": "Sassicaia", "produttore": "Tenuta San Guido", "prezzo": 350, "abbinamento": "Carne", "mood": "Occasione Speciale", "immagine": "https://www.tenutasanguido.com/images/bottiglia_sassicaia.png"},
    {"nome": "Petite Arvine", "produttore": "Les Cretes", "prezzo": 36, "abbinamento": "Pesce", "mood": "Incontro di lavoro", "immagine": "https://www.lescretes.it/wp-content/uploads/2021/04/Petite-Arvine-Les-Cretes.png"}
]

# =================================================================
# 4. LOGICA E INTERFACCIA
# =================================================================
st.title("🍷 Wine Selector 2.5")

# Gaspare ci accoglie
if 'benvenuto' not in st.session_state:
    parla_gaspare("Benvenuto nella mia cantina privata. Cosa desidera degustare oggi?")
    st.session_state.benvenuto = True
else:
    parla_gaspare("Ottima scelta... vedo che ha gusto!")

st.write("---")

# Scelte dell'utente
c1, c2 = st.columns(2)
with c1:
    cibo = st.selectbox("Cosa mangerà?", ["Scegli...", "Aperitivo", "Pesce", "Carne", "Dessert"])
with c2:
    mood = st.selectbox("Qual è l'occasione?", ["Scegli...", "Cena con amici", "Incontro di lavoro", "Occasione Speciale"])

if st.button("CHIEDI UN CONSIGLIO A GASPARE 🍇"):
    if cibo == "Scegli..." or mood == "Scegli...":
        st.warning("Gaspare ha bisogno di più dettagli per scegliere!")
    else:
        # Animazione Gaspare che "pensa"
        with st.empty():
            for i in range(3):
                parla_gaspare("Mmm... sto pensando al calice perfetto...")
                time.sleep(0.5)
                parla_gaspare("...scendo un momento in cantina...")
                time.sleep(0.5)
        
        # Filtro
        match = [v for v in vini if v["abbinamento"] == cibo and v["mood"] == mood]
        
        if match:
            parla_gaspare("Ho trovato un tesoro per lei. Guardi qui:")
            for v in match:
                st.markdown(f"""
                <div class="wine-card">
                    <img src="{v['immagine']}" width="150">
                    <div class="wine-title">{v['nome']}</div>
                    <div class="wine-producer">{v['produttore']}</div>
                    <div style="font-size: 24px; color: #800020; font-weight: bold; margin-top: 10px;">€ {v['prezzo']}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            parla_gaspare("Purtroppo la mia cantina non ha ciò che cerca... ma posso offrirle dell'acqua?")
