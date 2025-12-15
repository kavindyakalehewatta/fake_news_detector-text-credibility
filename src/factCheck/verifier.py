# Match claim vs evidence
from .sources import SRI_LANKAN_SOURCES
from .scraper import search_site

def verify_claim(text, keywords):
    evidence = []

    for source in SRI_LANKAN_SOURCES:
        score = search_site(source["url"], keywords)
        if score > 0:
            evidence.append({
                "source": source["name"],
                "matches": score
            })

    if len(evidence) == 0:
        return None  # no verification possible

    fact_score = min(1.0, sum(e["matches"] for e in evidence) / 10)

    return {
        "verified": True,
        "fact_score": fact_score,
        "evidence": evidence
    }
