from echo_image_similarity import compute_phash, find_similar

def test_compute_phash():
    h = compute_phash("test.jpg")
    assert len(h) == 16

def test_find_similar():
    c = find_similar("test.jpg")
    assert "query_hash" in c.result
