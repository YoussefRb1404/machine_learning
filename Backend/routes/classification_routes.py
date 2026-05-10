from fastapi import APIRouter
from schemas.predict_schema import InputData
from services.classification_service import predict_knn ,predict_svm, predict_Dtree, predict_Rf, predict_xgb_service
from schemas.predict_schema import LinearRegressionInput
from services.classification_service import predict_linear_regressionM
from services.classification_service import predict_academic_pressure
from services.classification_service import predict_logistic_regression
router = APIRouter()

@router.post("/predict-knn")
def predict_knn_route(data: InputData):
    return predict_knn(data)

@router.post("/predict-svm")
def predict_svm_route(data: InputData):
    return predict_svm(data)

@router.post("/predict-Dtree")
def predict_Dtree_route(data: InputData):
    return predict_Dtree(data)

@router.post("/predict-Rf")
def predict_Rf_route(data: InputData):
    return predict_Rf(data)

@router.post("/predict-Xg")
def predict_xgb_service_route(data: InputData):
    return predict_xgb_service(data)

@router.post("/predict-linear")
def predict_linear(data: LinearRegressionInput):
    # Appeler la fonction de prédiction et renvoyer la réponse
    prediction = predict_linear_regressionM(data)
    return {"predicted_academic_pressure": prediction}


#bilel
@router.post("/predict-poly")
def predict_poly_route(data: LinearRegressionInput):
    return predict_academic_pressure(data)




@router.post("/predict-logistic")
def route_logistic(data: InputData):
    return predict_logistic_regression(data)
