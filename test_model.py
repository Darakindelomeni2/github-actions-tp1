from model import predict_sentiment
# fichier de test pour le modèle de prédiction de sentiment
 
def test_predict_positive(): 
    assert predict_sentiment("I am happy today") == "positive" 
 
def test_predict_negative(): 
    assert predict_sentiment("I feel sad") == "negative" 
 
def test_predict_neutral(): 
    assert predict_sentiment("The sky is blue") == "neutral"