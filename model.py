# modif de newbranch
# fichier de modèle de prédiction de sentiment
# test evaluate
# re re re test documentation
# test pipeline

def predict_sentiment(text): 
    if not text: 
        return "neutral" 
    if "happy" in text.lower() or "good" in text.lower(): 
        return "positive" 
    if "sad" in text.lower() or "bad" in text.lower(): 
        return "negative" 
    return "neutral" 