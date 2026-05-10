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
    </style>
""", unsafe_allow_html=True)
accuracies = {
    "KNN": 0.817355,
    "SVM": 0.854219,                 # SVM RBF (meilleur)
    "SVM_Linear": 0.842490,
    "DecisionTree": 0.818552,
    "RandomForest": 0.838181,
    "XGBoost": 0.841412,             # version grid
    "XGBoost_random": 0.842849,
    "LogisticRegression": 0.8460212582591209
}
f1_scores = {
    "SVM": 0.878613,
    "SVM_Linear": 0.868242,
    "KNN": 0.848250,
    "DecisionTree": 0.844990,
    "RandomForest": 0.864746,
    "XGBoost": 0.867088,
    "XGBoost_random": 0.868186,
    "LogisticRegression": 0.85   # approx (macro avg f1-score = 0.84 / weighted 0.85)
}


# Appel du sidebar
create_sidebar()

st.markdown("## 🧠 Discover Your Mental State")
st.markdown("### Remplissez le formulaire pour obtenir une prédiction")

# ---- FORMULAIRE ----
with st.form("prediction_form"):
    
    col1, col2 = st.columns(2)

    with col1:
        Gender = st.selectbox(
            "Gender",
            [0, 1],
            format_func=lambda x: "Male" if x == 0 else "Female"
        )

        Age = st.number_input("Age", min_value=10, max_value=100, value=20)

        Academic_Pressure = st.selectbox(
            "Academic Pressure",
            [1, 2, 3, 4, 5],
            format_func=lambda x: {
                1: "Very Low",
                2: "Low",
                3: "Medium",
                4: "High",
                5: "Very High"
            }[x]
        )

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
            format_func=lambda x: {
                1: "Very Unsatisfied",
                2: "Unsatisfied",
                3: "Neutral",
                4: "Satisfied",
                5: "Very Satisfied"
            }[x]
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

    with col2:

        # --- CITY ---
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

        # --- SLEEP ---
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

        # --- DIET ---
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

        # --- DEGREE ---
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

    # --------------------------------------------------
    #  BOUTON → doit être dans le form (sinon erreur)
    # --------------------------------------------------
    submitted = st.form_submit_button("🚀 Envoyer")


# ---- APPEL API APRÈS CLIC ----
if submitted:
    st.info("📡 Envoi des données au serveur...")

    payload = {
        "Gender": Gender,
        "Age": Age,
        "Academic_Pressure": Academic_Pressure,
        "CGPA": CGPA,
        "Study_Satisfaction": Study_Satisfaction,
        "Work_Study_Hours": Work_Study_Hours,
        "Financial_Stress": Financial_Stress,
        "City_Code": City_Code,
        "Sleep_Duration_Code": Sleep_Duration_Code,
        "Dietary_Habits_Code": Dietary_Habits_Code,
        "Degree_Code": Degree_Code,
        "Suicidal_Thoughts": Suicidal_Thoughts,
        "Family_History_Mental_Illness": Family_History_Mental_Illness,
        "Profession_Code": Profession_Code
    }

    # Créer deux lignes avec deux colonnes chacune
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)

    backend_url = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

    # KNN Prediction
    with col1:
        st.markdown(f"### 🔍 Résultat KNN — F1-score : {f1_scores['KNN'] * 100:.2f}%")

        try:
            response = requests.post(f"{backend_url}/api/predict-knn", json=payload)
            result = response.json()

            if result["prediction"] == 1:
                st.error("🛑 L'étudiant montre des signes de dépression.")
            else:
                st.success("✅ Aucun signe de dépression détecté.")

        except Exception as e:
            st.error(f"Erreur KNN : {e}")

    # SVM Prediction
    with col2:
        st.markdown(f"### 🎯 Résultat SVM — F1-score : {f1_scores['SVM'] * 100:.2f}%")

        try:
            response = requests.post(f"{backend_url}/api/predict-svm", json=payload)
            result = response.json()

            if result["prediction"] == 1:
                st.error("🛑 L'étudiant montre des signes de dépression.")
            else:
                st.success("✅ Aucun signe de dépression détecté.")

        except Exception as e:
            st.error(f"Erreur SVM : {e}")

    # Decision Tree Prediction
    with col3:
        st.markdown(f"### 🌳 Résultat Decision Tree — F1-score : {f1_scores['DecisionTree'] * 100:.2f}%")
        try:
            response = requests.post(f"{backend_url}/api/predict-Dtree", json=payload)
            result = response.json()

            if result["prediction"] == 1:
                st.error("🛑 L'étudiant montre des signes de dépression.")
            else:
                st.success("✅ Aucun signe de dépression détecté.")

        except Exception as e:
            st.error(f"Erreur Decision Tree : {e}")

    # Random Forest Prediction
    with col4:
        st.markdown(f"### 🌲 Résultat Random Forest - F1-score : {f1_scores['RandomForest'] * 100:.2f}%")
        try:
            response = requests.post(f"{backend_url}/api/predict-Rf", json=payload)
            result = response.json()

            if result["prediction"] == 1:
                st.error("🛑 L'étudiant montre des signes de dépression.")
            else:
                st.success("✅ Aucun signe de dépression détecté.")

        except Exception as e:
            st.error(f"Erreur Random Forest : {e}")
# Random Forest Prediction
    with col5:
        st.markdown(f"### ⚡ Résultat XGBOOST — F1-score : {f1_scores['XGBoost_random'] * 100:.2f}%")

        try:
            response = requests.post(f"{backend_url}/api/predict-Xg", json=payload)
            result = response.json()

            if result["prediction"] == 1:
                st.error("🛑 L'étudiant montre des signes de dépression.")
            else:
                st.success("✅ Aucun signe de dépression détecté.")

        except Exception as e:
            st.error(f"Erreur Xgboost : {e}")
    with col6:
        st.markdown(f"### 🧪 Résultat Logistic Regression — F1-score : {f1_scores['LogisticRegression'] * 100:.2f}%")

        try:
           response = requests.post(f"{backend_url}/api/predict-logistic", json=payload)
           result = response.json()

           if result["prediction"] == 1:
            st.error("🛑 L'étudiant montre des signes de dépression.")
           else:
            st.success("✅ Aucun signe de dépression détecté.")

        except Exception as e:
             st.error(f"Erreur Logistic Regression : {e}")




         