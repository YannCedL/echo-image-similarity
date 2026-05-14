# test de similarité et pHash Echo
from echo_image_similarity.search import find_similar

def test_find_similar():
    contract = find_similar("sample.jpg")
    assert contract is not None
    assert contract.result["query_hash"] is not None
    assert len(contract.result["matches"]) >= 1
    assert len(contract.evidence) >= 1
