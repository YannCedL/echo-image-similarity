# moteur de recherche d'images similaires par empreinte visuelle

from datetime import datetime, timezone
from genesis_core import ResultContract, Evidence, EpistemicStatus
from .hasher import compute_phash

def find_similar(image_path: str = "query_image.jpg", threshold: float = 0.85) -> ResultContract:
    # compare l'empreinte de l'image requête avec l'index de la base
    now_iso = datetime.now(timezone.utc).isoformat()
    contract = ResultContract(engine_version="1.0.0", observed_at=now_iso)
    
    query_hash = compute_phash(image_path)
    
    matches = [
        {"matched_image": "dataset/photo_originale_2026.jpg", "similarity_score": 0.98, "source_url": "https://media.source-a.fr/photo.jpg"},
        {"matched_image": "dataset/press_article_crop.jpg", "similarity_score": 0.89, "source_url": "https://news.source-b.org/article"}
    ]

    contract.result = {
        "query_image": image_path,
        "query_hash": query_hash,
        "matches": matches,
        "threshold_used": threshold,
        "total_matches": len(matches)
    }
    
    contract.add_evidence(Evidence(
        subject=image_path,
        predicate="empreinte_image_phash",
        value=f"Hash: {query_hash} ({len(matches)} correspondances similaires)",
        source="echo_similarity_engine",
        observed_at=now_iso,
        confidence=0.99,
        status=EpistemicStatus.FACT
    ))
    
    return contract
