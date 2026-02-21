#!/usr/bin/env python3
"""
Supprime le fond blanc de toutes les images spécifiées et génère des PNG transparents.
Utilise un floodfill depuis les coins + seuil de tolérance pour un résultat propre.
"""

from PIL import Image
import os
import glob

def remove_white_background(input_path: str, output_path: str, tolerance: int = 30) -> None:
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    pixels = list(img.getdata())

    def is_near_white(pixel, tol):
        r, g, b, _ = pixel
        return r >= (255 - tol) and g >= (255 - tol) and b >= (255 - tol)

    visited = [[False] * height for _ in range(width)]
    background_coords = set()

    def floodfill(start_x, start_y):
        stack = [(start_x, start_y)]
        while stack:
            x, y = stack.pop()
            if x < 0 or x >= width or y < 0 or y >= height:
                continue
            if visited[x][y]:
                continue
            visited[x][y] = True
            idx = y * width + x
            if is_near_white(pixels[idx], tolerance):
                background_coords.add(idx)
                stack.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])

    for cx, cy in [(0, 0), (width-1, 0), (0, height-1), (width-1, height-1)]:
        floodfill(cx, cy)

    new_pixels = [
        (255, 255, 255, 0) if i in background_coords else pixel
        for i, pixel in enumerate(pixels)
    ]

    img.putdata(new_pixels)
    img.save(output_path, "PNG")
    print(f"  ✅ {os.path.basename(input_path)} → {os.path.basename(output_path)}")


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    images_dir = os.path.join(base_dir, "public", "images")

    patterns = ["lulu*.jpg", "pose*.png"]
    sources = []
    for pattern in patterns:
        sources.extend(sorted(glob.glob(os.path.join(images_dir, pattern))))

    print(f"🖼  {len(sources)} image(s) trouvée(s)...\n")

    for src in sources:
        name = os.path.splitext(os.path.basename(src))[0]
        # Pour les lulu*.jpg → lulu*-nobg.png
        # Pour les pose*.png → pose*-nobg.png
        dst = os.path.join(images_dir, f"{name}-nobg.png")
        remove_white_background(src, dst, tolerance=30)

    print(f"\n✨ Terminé ! {len(sources)} fichier(s) PNG transparents générés.")


if __name__ == "__main__":
    main()
