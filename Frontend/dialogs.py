import streamlit as st

@st.dialog("📈 Analyse des données")
def show_data_analysis_dialog():
    st.markdown("""
    ### 🎯 Notre application Analyse:
    
    #### 🔴 Découvrir les seuils critiques de pression académique
   
    
    #### 👥 Identifier les profils d'étudiants les plus vulnérables
   
    """)
    
    if st.button("Fermer", type="primary", use_container_width=True):
        st.rerun()



@st.dialog("⚡ Prédiction ML")
def show_ml_prediction_dialog():
    st.markdown("""
    ### 🎯 Notre application prédit :
    
    #### Prédire la probabilité de dépression chez un étudiant
    #### Détecter précocement les étudiants à risque suicidaire

                
    
    """)
    
    if st.button("Fermer", type="primary", use_container_width=True):
        st.rerun()

@st.dialog("💡 Insights")
def show_insights_dialog():
    st.markdown("""
    ### 🎯 Visualisations disponibles :
    
    #### Résultats du prétraitement
    #### Résultats de clustering
    ### Performance des modèles
  
    """)
    
    if st.button("Fermer", type="primary", use_container_width=True):
        st.rerun()