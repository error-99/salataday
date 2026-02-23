import os
from PIL import Image

# Target size range (KB)
TARGET_MIN = 30
TARGET_MAX = 80

# Resize limit (speed + compression)
MAX_WIDTH = 1000

def convert_to_webp(path):
    try:
        img = Image.open(path)

        # Resize if too large
        if img.width > MAX_WIDTH:
            ratio = MAX_WIDTH / img.width
            new_height = int(img.height * ratio)
            img = img.resize((MAX_WIDTH, new_height), Image.LANCZOS)

        # Convert RGBA → RGB
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        webp_path = path.replace(".png", ".webp")

        quality = 80
        img.save(webp_path, "WEBP", quality=quality, method=6)

        # Reduce quality if bigger than TARGET_MAX
        while os.path.getsize(webp_path) / 1024 > TARGET_MAX and quality > 20:
            quality -= 5
            img.save(webp_path, "WEBP", quality=quality, method=6)

        final_size = os.path.getsize(webp_path) / 1024
        print(f"{os.path.basename(webp_path)} → {round(final_size,2)} KB")

        img.close()

        # Delete original PNG
        os.remove(path)

    except Exception as e:
        print(f"Error processing {path}: {e}")

def main():
    folder = os.getcwd()

    for file in os.listdir(folder):
        if file.lower().endswith(".png"):
            full_path = os.path.join(folder, file)
            convert_to_webp(full_path)

    print("\nDone ✔ All images converted to WebP")

if __name__ == "__main__":
    main()