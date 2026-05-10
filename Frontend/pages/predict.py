import streamlit as st
import requests
import os
from sidebar import create_sidebar

# Configuration de la page
st.set_page_config(page_title="Prediction", page_icon="🤖", layout="wide")

# Cacher la navigation automatique + Style personnalisé
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
        
        /* Réduire la taille du titre */
        h2 {
            font-size: 1.8rem !important;
            margin-top: 0 !important;
            padding-top: 0 !important;
        }
        
        h3 {
            font-size: 1.2rem !important;
            margin-top: 0.5rem !important;
        }
        
        /* Réduire le padding en haut du formulaire */
        [data-testid="stForm"] {
            padding-top: 0.5rem !important;
            margin-top: 0 !important;
        }
        
        [data-testid="stForm"] button[type="submit"] {
            width: 100% !important;
            margin: 1rem auto !important;
            display: block !important;
        }
        
        .block-container {
            padding-top: 2rem !important;
        }
        
        /* Style pour les cartes de résultats */
        .result-card {
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
            border-left: 5px solid;
        }
        
        .result-linear {
            background-color: #e3f2fd;
            border-left-color: #2196F3;
        }
        
        .result-poly {
            background-color: #f3e5f5;
            border-left-color: #9c27b0;
        }
        
        .prediction-value {
            font-size: 2.5rem;
            font-weight: bold;
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Appel du sidebar
create_sidebar()

st.markdown("## 🧠 Discover Your Mental State")
st.markdown("### Remplissez le formulaire pour obtenir une prédiction des deux modèles")

# ---- FORMULAIRE ----
with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    # ============================================
    # 🔹 COLONNE 1 — ATTRIBUTS GÉNÉRAUX
    # ============================================
    with col1:

        Gender = st.selectbox(
            "Gender",
            [0, 1],
            format_func=lambda x: "Male" if x == 0 else "Female"
        )

        Age = st.number_input("Age", min_value=10, max_value=100, value=20)

        CGPA = st.selectbox(
            "CGPA (Grade)",
            [2.0, 5.0, 7.0, 9.0],
            format_func=lambda x: {
                2.0: "0 - 4 (Weak)",
                5.0: "4 - 6 (Average)",
                7.0: "6 - 8 (Good)",
                9.0: "8 - 10 (Excellent)"
            }[x]
        )

        Study_Satisfaction = st.selectbox(
            "Study Satisfaction",
            [1, 2, 3, 4, 5],
            format_func=lambda x: [
                "Very Unsatisfied",
                "Unsatisfied",
                "Neutral",
                "Satisfied",
                "Very Satisfied"
            ][x - 1]
        )

        Work_Study_Hours = st.selectbox(
            "Daily Work/Study Hours",
            [1, 3, 5, 7, 9],
            format_func=lambda x: {
                1: "0–2 hours",
                3: "2–4 hours",
                5: "4–6 hours",
                7: "6–8 hours",
                9: "8+ hours"
            }[x]
        )

        Financial_Stress = st.selectbox(
            "Financial Stress Level",
            [1, 2, 3, 4, 5],
            format_func=lambda x: {
                1: "None",
                2: "Low",
                3: "Medium",
                4: "High",
                5: "Extreme"
            }[x]
        )

        Depression = st.selectbox(
            "Depression Level",
            [1, 2, 3, 4, 5],
            format_func=lambda x: {
                1: "Very Low",
                2: "Low",
                3: "Moderate",
                4: "High",
                5: "Very High"
            }[x]
        )

    # ============================================
    # 🔹 COLONNE 2 — ATTRIBUTS ENCODÉS DU DATASET
    # ============================================
    with col2:

        # ---- City ----
        city_values = list(range(1, 31))
        city_labels = [
            "Visakhapatnam", "Bangalore", "Srinagar", "Varanasi",
            "Jaipur", "Pune", "Thane", "Chennai", "Nagpur",
            "Nashik", "Vadodara", "Kalyan", "Rajkot", "Ahmedabad",
            "Kolkata", "Mumbai", "Lucknow", "Indore", "Surat",
            "Ludhiana", "Bhopal", "Meerut", "Agra", "Ghaziabad",
            "Hyderabad", "Vasai-Virar", "Kanpur", "Patna",
            "Faridabad", "Delhi"
        ]

        City_Code = st.selectbox(
            "City",
            city_values,
            format_func=lambda x: city_labels[x - 1]
        )

        # ---- Sleep Duration ----
        Sleep_Duration_Code = st.selectbox(
            "Sleep Duration",
            [1, 2, 3, 4, 5],
            format_func=lambda x: {
                1: "Less than 5 hours",
                2: "5–6 hours",
                3: "7–8 hours",
                4: "More than 8 hours",
                5: "Others"
            }[x]
        )

        # ---- Diet ----
        Dietary_Habits_Code = st.selectbox(
            "Dietary Habits",
            [1, 2, 3, 4],
            format_func=lambda x: {
                1: "Healthy",
                2: "Moderate",
                3: "Unhealthy",
                4: "Others"
            }[x]
        )

        # ---- Degree ----
        degree_values = list(range(1, 29))
        degree_labels = [
            "B.Pharm", "BSc", "BA", "BCA", "M.Tech", "PhD", "Class 12", "B.Ed",
            "LLB", "BE", "M.Ed", "MSc", "BHM", "M.Pharm", "MCA", "MA", "B.Com",
            "MD", "MBA", "MBBS", "M.Com", "B.Arch", "LLM", "B.Tech", "BBA",
            "ME", "MHM", "Others"
        ]

        Degree_Code = st.selectbox(
            "Degree",
            degree_values,
            format_func=lambda x: degree_labels[x - 1]
        )

        Suicidal_Thoughts = st.selectbox(
            "Suicidal Thoughts",
            [0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes"
        )

        Family_History_Mental_Illness = st.selectbox(
            "Family History of Mental Illness",
            [0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes"
        )

        Profession_Code = st.selectbox(
            "Profession",
            [1],
            format_func=lambda x: "Student"
        )

    submitted = st.form_submit_button("🚀 Obtenir les Prédictions")


# ---- APPEL AUX DEUX APIs ----
if submitted:
    st.info("📡 Envoi des données aux deux serveurs...")

    payload = {
        "Gender": float(Gender),
        "Age": float(Age),
        "CGPA": float(CGPA),
        "Study_Satisfaction": float(Study_Satisfaction),
        "Work_Study_Hours": float(Work_Study_Hours),
        "Financial_Stress": float(Financial_Stress),
        "Depression": float(Depression),
        "City_Code": float(City_Code),
        "Sleep_Duration_Code": float(Sleep_Duration_Code),
        "Dietary_Habits_Code": float(Dietary_Habits_Code),
        "Degree_Code": float(Degree_Code),
        "Suicidal_Thoughts": float(Suicidal_Thoughts),
        "Family_History_Mental_Illness": float(Family_History_Mental_Illness),
        "Profession_Code": float(Profession_Code)
    }

    # Créer deux colonnes pour afficher les résultats côte à côte
    col_result1, col_result2 = st.columns(2)

    # ---- RÉGRESSION LINÉAIRE ----
    with col_result1:
        st.markdown("### 📈 Régression Linéaire")
        backend_url = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
        try:
            response_linear = requests.post(f"{backend_url}/api/predict-linear", json=payload)
            result_linear = response_linear.json()
            
            prediction_linear = result_linear['predicted_academic_pressure']
            
            # Déterminer le statut
            if prediction_linear < 3:
                status = "🟢 Faible"
                color = "#4caf50"
            elif prediction_linear < 7:
                status = "🟡 Modéré"
                color = "#ff9800"
            else:
                status = "🔴 Élevé"
                color = "#f44336"
            
            st.markdown(f"""
            <div class="result-card result-linear">
                <h4>Prédiction de la Pression Académique</h4>
                <div class="prediction-value" style="color: #2196F3;">{prediction_linear:.2f}</div>
                <p style="font-size: 1.2rem;"><strong>Statut:</strong> {status}</p>
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Erreur lors de la connexion à l'API Linéaire : {e}")

    # ---- RÉGRESSION POLYNOMIALE ----
    with col_result2:
        st.markdown("### 📊 Régression Polynomiale")
        try:
            response_poly = requests.post(f"{backend_url}/api/predict-poly", json=payload)
            result_poly = response_poly.json()
            
            prediction_poly = result_poly['predicted_academic_pressure']
            
            # Déterminer le statut
            if prediction_poly < 3:
                status = "🟢 Faible"
                color = "#4caf50"
            elif prediction_poly < 7:
                status = "🟡 Modéré"
                color = "#ff9800"
            else:
                status = "🔴 Élevé"
                color = "#f44336"
            
            st.markdown(f"""
            <div class="result-card result-poly">
                <h4>Prédiction de la Pression Académique</h4>
                <div class="prediction-value" style="color: #9c27b0;">{prediction_poly:.2f}</div>
                <p style="font-size: 1.2rem;"><strong>Statut:</strong> {status}</p>
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Erreur lors de la connexion à l'API Polynomiale : {e}")


