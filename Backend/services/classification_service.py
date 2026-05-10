import numpy as np
import joblib
from schemas.predict_schema import InputData
from schemas.predict_schema import LinearRegressionInput


# Charger modèle + scaler
knn_model = joblib.load("models/knn_model.pkl")
scaler = joblib.load("models/scaler.pkl")

def predict_knn(data: InputData):

    # Assemblage des données dans l'ordre EXACT du notebook
    arr = np.array([[
        data.Gender,
        data.Age,
        data.Academic_Pressure,
        data.CGPA,
        data.Study_Satisfaction,
        data.Work_Study_Hours,
        data.Financial_Stress,
        data.City_Code,
        data.Sleep_Duration_Code,
        data.Dietary_Habits_Code,
        data.Degree_Code,
        data.Suicidal_Thoughts,
        data.Family_History_Mental_Illness,
        data.Profession_Code
    ]])

    # Normalisation (comme dans ton notebook)
    arr_scaled = scaler.transform(arr)

    # Prédiction KNN (même code que dans ton notebook)
    prediction = knn_model.predict(arr_scaled)[0]

    # Résultat final (même logique)
    result = {
        1: "🛑 L'étudiant montre des signes de dépression.",
        0: "✅ Aucun signe de dépression détecté."
    }

    return {
        "prediction": int(prediction),
        "message": result[prediction]
    }

svm_model = joblib.load("models/svm_model.pkl")
svm_scaler = joblib.load("models/svm_scaler.pkl")

def predict_svm(data: InputData):
   
    # Assemblage des données dans l'ordre EXACT du notebook
    arr = np.array([[
        data.Gender,
        data.Age,
        data.Academic_Pressure,
        data.CGPA,
        data.Study_Satisfaction,
        data.Work_Study_Hours,
        data.Financial_Stress,
        data.City_Code,
        data.Sleep_Duration_Code,
        data.Dietary_Habits_Code,
        data.Degree_Code,
        data.Suicidal_Thoughts,
        data.Family_History_Mental_Illness,
        data.Profession_Code
    ]])

    # Normalisation avec le scaler SVM
    arr_scaled = svm_scaler.transform(arr)

    # Prédiction SVM
    prediction = svm_model.predict(arr_scaled)[0]

    # Résultat final
    result = {
        1: "🛑 L'étudiant montre des signes de dépression (SVM).",
        0: "✅ Aucun signe de dépression détecté (SVM)."
    }

    return {
        "model": "SVM",
        "prediction": int(prediction),
        "message": result[prediction]
    }

Dtree_model = joblib.load("models/Dtree_model.pkl")
Dtree_scaler = joblib.load("models/Dtree_scaler.pkl")

def predict_Dtree(data: InputData):
   
    # Assemblage des données dans l'ordre EXACT du notebook
    arr = np.array([[
        data.Gender,
        data.Age,
        data.Academic_Pressure,
        data.CGPA,
        data.Study_Satisfaction,
        data.Work_Study_Hours,
        data.Financial_Stress,
        data.City_Code,
        data.Sleep_Duration_Code,
        data.Dietary_Habits_Code,
        data.Degree_Code,
        data.Suicidal_Thoughts,
        data.Family_History_Mental_Illness,
        data.Profession_Code
    ]])

    # Normalisation avec le scaler Dtree
    arr_scaled = Dtree_scaler.transform(arr)

    # Prédiction Dtree
    prediction = Dtree_model.predict(arr_scaled)[0]

    # Résultat final
    result = {
        1: "🛑 L'étudiant montre des signes de dépression (Desicion tree).",
        0: "✅ Aucun signe de dépression détecté (Desicion tree)."
    }

    return {
        "model": "Desicion tree",
        "prediction": int(prediction),
        "message": result[prediction]
    }
Rf_model = joblib.load("models/Rf_model.pkl")
Rf_scaler = joblib.load("models/Rf_scaler.pkl")

def predict_Rf(data: InputData):
   
    # Assemblage des données dans l'ordre EXACT du notebook
    arr = np.array([[
        data.Gender,
        data.Age,
        data.Academic_Pressure,
        data.CGPA,
        data.Study_Satisfaction,
        data.Work_Study_Hours,
        data.Financial_Stress,
        data.City_Code,
        data.Sleep_Duration_Code,
        data.Dietary_Habits_Code,
        data.Degree_Code,
        data.Suicidal_Thoughts,
        data.Family_History_Mental_Illness,
        data.Profession_Code
    ]])

    # Normalisation avec le scaler Dtree
    arr_scaled = Rf_scaler.transform(arr)

    # Prédiction Dtree
    prediction = Rf_model.predict(arr_scaled)[0]

    # Résultat final
    result = {
        1: "🛑 L'étudiant montre des signes de dépression (Random forest).",
        0: "✅ Aucun signe de dépression détecté (Random forest)."
    }

    return {
        "model": "Random forest",
        "prediction": int(prediction),
        "message": result[prediction]
    }

xgb_model = joblib.load("models/xgb_model.pkl")
def predict_xgb_service(data: InputData):

    # Préparation des données... (Identique à KNN)
    arr = np.array([[
        data.Gender,
        data.Age,
        data.Academic_Pressure,
        data.CGPA,
        data.Study_Satisfaction,
        data.Work_Study_Hours,
        data.Financial_Stress,
        data.City_Code,
        data.Sleep_Duration_Code,
        data.Dietary_Habits_Code,
        data.Degree_Code,
        data.Suicidal_Thoughts,
        data.Family_History_Mental_Illness,
        data.Profession_Code
    ]])

    # Normalisation (pour la cohérence)
    arr_scaled = scaler.transform(arr)

    # Prédiction XGBoost
    prediction = xgb_model.predict(arr_scaled)[0]
   
    # Résultat final
    result = {1: "🛑 L'étudiant montre des signes de dépression.", 0: "✅ Aucun signe de dépression détecté."}

    return {"prediction": int(prediction), "message": result[prediction]}

#mariem

# Charger le modèle et le scaler pour la régression linéaire
linear_model = joblib.load("models/linear_model.pkl")
linear_scaler = joblib.load("models/scaler_linear.pkl")


def predict_linear_regressionM(data: LinearRegressionInput):
    # Préparer les features (ordre des features doit correspondre à celui du modèle)
    features = np.array([[
        data.Gender,
        data.Age,
        data.CGPA,
        data.Study_Satisfaction,
        data.Work_Study_Hours,
        data.Financial_Stress,
        data.City_Code,
        data.Sleep_Duration_Code,
        data.Dietary_Habits_Code,
        data.Degree_Code,
        data.Suicidal_Thoughts,
        data.Family_History_Mental_Illness,
        data.Profession_Code,
        data.Depression
    ]])

    # Normaliser les features avec le scaler
    scaled_features = linear_scaler.transform(features)

    # Prédiction avec le modèle linéaire
    prediction = linear_model.predict(scaled_features)[0]

    return float(prediction)


#bilel

model_poly = joblib.load("models/model_poly.pkl")
poly_features = joblib.load("models/poly_features.pkl")

def predict_academic_pressure(data: LinearRegressionInput):

    # Respecter l’ordre EXACT de X = df.drop(["Academic Pressure", "id"], axis=1)
    arr = np.array([[
        data.Gender,
        data.Age,
        data.CGPA,
        data.Study_Satisfaction,
        data.Work_Study_Hours,
        data.Financial_Stress,
        data.City_Code,
        data.Sleep_Duration_Code,
        data.Dietary_Habits_Code,
        data.Degree_Code,
        data.Suicidal_Thoughts,
        data.Family_History_Mental_Illness,
        data.Profession_Code,
        data.Depression
    ]])

    # Transformation polynomiale (même que lors de l'entraînement)
    arr_poly = poly_features.transform(arr)

    # Prédiction
    prediction = model_poly.predict(arr_poly)[0]

    return {
        "predicted_academic_pressure": float(prediction)
    }

# Charger modèle et scaler EXACTEMENT comme dans le dossier
log_model = joblib.load("models/logistique_model.pkl")
log_scaler = joblib.load("models/scaler_logistique.pkl")

def predict_logistic_regression(data: InputData):

    # Respecter l'ordre EXACT des colonnes du dataset
    arr = np.array([[  
        data.Gender,
        data.Age,
        data.Academic_Pressure,
        data.CGPA,
        data.Study_Satisfaction,
        data.Work_Study_Hours,
        data.Financial_Stress,
        data.City_Code,
        data.Sleep_Duration_Code,
        data.Dietary_Habits_Code,
        data.Degree_Code,
        data.Suicidal_Thoughts,
        data.Family_History_Mental_Illness,
        data.Profession_Code
    ]])

    # Scaling
    scaled = log_scaler.transform(arr)

    # Prédictions
    pred = log_model.predict(scaled)[0]
    prob = log_model.predict_proba(scaled)[0][1]

    messages = {
        1: "🛑 L'étudiant montre des signes de dépression.",
        0: "✅ Aucun signe de dépression détecté."
    }

    return {
        "prediction": int(pred),
        "probability": float(prob),
        "message": messages[pred]
    }