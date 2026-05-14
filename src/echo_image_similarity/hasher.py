import hashlib

def compute_phash(image_path: str) -> str:
    return hashlib.md5(image_path.encode()).hexdigest()[:16]
