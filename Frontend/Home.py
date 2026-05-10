import streamlit as st
import pandas as pd
from sidebar import create_sidebar
from dialogs import show_data_analysis_dialog,  show_ml_prediction_dialog, show_insights_dialog




# Désactiver la navigation automatique de Streamlit
st.set_page_config(
    page_title="Votre App",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cacher la navigation automatique
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# Configuration de la page
st.set_page_config(
    page_title="Student Depression Analysis",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
   .info-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 10px 0;
        cursor: pointer;
        transition: transform 0.2s;
    }
    .info-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🎓 Student Depression Analysis</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Understanding and analyzing the factors contributing to depression in students</p>', unsafe_allow_html=True)

# Section informative
st.markdown("---")
st.markdown("## 🎯 Application objectives")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-box">
        <h3>📈 Analyse des données</h3>
        <p>Exploration approfondie des facteurs essentiel pour déterminer le risque et des tendances de la dépression étudiante.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("📖 En savoir plus", key="btn_analysis", use_container_width=True):
        show_data_analysis_dialog()

with col2:
    st.markdown("""
    <div class="info-box">
    <h3>⚡ Prédiction ML</h3>
    <p>notre modèle de Machine Learning utilise les données fournies pour effectuer des prédictions fiables et automatisées.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("📖 En savoir plus", key="btn_prediction", use_container_width=True):
         show_ml_prediction_dialog()

with col3:
    st.markdown("""
    <div class="info-box">
    <h3>💡 Insights</h3>
    <p>Cette section met en avant les informations tirées des données analysées. Elle résume les tendances permettant de comprendre l’état mental des étudiants.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("📖 En savoir plus", key="btn_insight", use_container_width=True):
         show_insights_dialog()

# Statistiques rapides (exemple)
st.markdown("---")
st.markdown("## 📊 Aperçu des données")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="📚 Total Étudiants",
        value="1,500",
        delta="↑ 120 ce mois"
    )

with col2:
    st.metric(
        label="⚠️ Taux de Dépression",
        value="23.5%",
        delta="-2.1%",
        delta_color="inverse"
    )

with col3:
    st.metric(
        label="🎯 Précision Modèle",
        value="87.3%",
        delta="↑ 3.2%"
    )

with col4:
    st.metric(
        label="📈 Facteurs Identifiés",
        value="12",
        delta="↑ 2"
    )

# Facteurs principaux
st.markdown("---")
st.markdown("## 🔍 Facteurs principaux analysés")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    #### Facteurs académiques
    - 📖 Pression académique
    - ⏰ Charge de travail
    - 📊 Performance scolaire
    - 🎓 Niveau d'études
    """)
    
with col2:
    st.markdown("""
    #### Facteurs personnels
    - 😴 Qualité du sommeil
    - 🏃 Activité physique
    - 👨‍👩‍👧 Support familial
    - 💰 Situation financière
    """)

# Navigation
st.markdown("---")
st.markdown("## 🧭 Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊 Explorer les données", use_container_width=True):
        st.info("Accédez à la page 'Exploration des données' via la sidebar")

with col2:
    if st.button("🤖 Modèle de prédiction", use_container_width=True):
        st.info("Accédez à la page 'Modèle K-means' via la sidebar")

with col3:
    if st.button("📈 Visualisations", use_container_width=True):
        st.info("Accédez à la page 'Visualisations' via la sidebar")
        

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>💙 Application développée pour aider à comprendre et prévenir la dépression étudiante</p>
    <p><small>Données utilisées à des fins d'analyse et de recherche uniquement</small></p>
</div>
""", unsafe_allow_html=True)


# Appeler le sidebar
create_sidebar()
    