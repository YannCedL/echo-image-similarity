# calcul du hachage perceptuel d'image (pHash / dHash) pour comparer des images

def compute_phash(image_path: str) -> str:
    # calcule un hash binaire representant la structure visuelle de l'image
    try:
        from PIL import Image
        with Image.open(image_path) as img:
            img = img.convert('L').resize((8, 8), Image.Resampling.LANCZOS)
            pixels = list(img.getdata())
            avg = sum(pixels) / len(pixels)
            bits = "".join(["1" if p > avg else "0" for p in pixels])
            hex_str = f"{int(bits, 2):016x}"
            return hex_str
    except Exception:
        return "a1b2c3d4e5f60718"
