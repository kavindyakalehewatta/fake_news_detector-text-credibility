# credibility + comparison logic

import torch

def ml_credibility_score(model, X):
    with torch.no_grad():
        outputs = model(X)
        probs = torch.exp(outputs)
        credibility = probs[:, 1].mean().item()  # probability of REAL
    return credibility

def final_decision(fact_result, ml_score):
    if fact_result is None:
        return {
            "final_score": ml_score,
            "decision": "Model-based (No fact data)",
            "confidence": ml_score
        }

    combined_score = (fact_result["fact_score"] * 0.6) + (ml_score * 0.4)

    agreement = abs(fact_result["fact_score"] - ml_score) < 0.3

    return {
        "final_score": combined_score,
        "decision": "Verified" if combined_score > 0.6 else "Not Verified",
        "agreement": agreement
    }

