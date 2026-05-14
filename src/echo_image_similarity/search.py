from datetime import datetime, timezone
from genesis_core import ResultContract, Evidence, EpistemicStatus
from .hasher import compute_phash

def find_similar(image_path: str, threshold: float = 0.9) -> ResultContract:
    now = datetime.now(timezone.utc).isoformat()
    contract = ResultContract(engine_version="1.0.0", observed_at=now)
    phash = compute_phash(image_path)
    contract.result = {"query_hash": phash, "matches": [], "threshold": threshold}
    contract.add_evidence(Evidence(subject=image_path, predicate="image_hash",
        value=phash, source="echo_engine", observed_at=now,
        confidence=1.0, status=EpistemicStatus.FACT))
    return contract
