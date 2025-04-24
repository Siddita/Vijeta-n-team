# Symptom rule-matching
def match_symptoms(symptoms):
    symptoms = [s.lower() for s in symptoms]
    if "fever" in symptoms and "cough" in symptoms:
        return "Possible respiratory infection"
    elif "abdominal pain" in symptoms:
        return "Possible gastrointestinal issue"
    else:
        return "Unable to determine from symptoms"
