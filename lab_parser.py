# Lab Parser
def analyze_lab(crp, wbc):
    if crp > 10 and wbc > 11000:
        return "Infection likely"
    elif crp <= 10 and wbc <= 11000:
        return "Normal"
    else:
        return "Further analysis needed"
