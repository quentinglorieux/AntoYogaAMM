#!/usr/bin/env python3
"""
Supprime le fond blanc des images lulu*.jpg et génère des PNG transparents.

Stratégie en deux passes :
1. Floodfill depuis les 4 coins pour le fond extérieur.
2. Suppression globale de TOUS les pixels quasi-blancs (zones internes comme
   entre les bras ou les jambes des illustrations).

On utilise pour la passe 2 un filtre : si un pixel est quasi-blanc ET que ses
voisins immédiats sont soit transparents, soit également quasi-blancs, on le
rend transparent. On répète jusqu'à convergence.
"""

from PIL import Image
import os
import glob


def is_near_white(r, g, b, tol):
    return r >= (255 - tol) and g >= (255 - tol) and b >= (255 - tol)


def remove_white_background(input_path: str, output_path: str, tolerance: int = 30, erode: bool = True) -> None:
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    pixels = list(img.getdata())

    # ------------------------------------------------------------------
    # Passe 1 : floodfill depuis les 4 coins (fond extérieur)
    # ------------------------------------------------------------------
    visited = [[False] * height for _ in range(width)]
    bg = set()

    def floodfill(sx, sy):
        stack = [(sx, sy)]
        while stack:
            x, y = stack.pop()
            if x < 0 or x >= width or y < 0 or y >= height:
                continue
            if visited[x][y]:
                continue
            visited[x][y] = True
            r, g, b, _ = pixels[y * width + x]
            if is_near_white(r, g, b, tolerance):
                bg.add(y * width + x)
                stack.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])

    for cx, cy in [(0, 0), (width-1, 0), (0, height-1), (width-1, height-1)]:
        floodfill(cx, cy)

    # Appliquer passe 1
    data = list(pixels)
    for idx in bg:
        data[idx] = (255, 255, 255, 0)

    # ------------------------------------------------------------------
    # Passe 2 : zones blanches internes (optionnelle)
    # ------------------------------------------------------------------
    if erode:
        changed = True
        while changed:
            changed = False
            new_data = list(data)
            for y in range(height):
                for x in range(width):
                    idx = y * width + x
                    r, g, b, a = data[idx]
                    if a == 0:
                        continue
                    if not is_near_white(r, g, b, tolerance):
                        continue
                    neighbors = []
                    if x > 0:         neighbors.append(data[y * width + (x-1)])
                    if x < width-1:   neighbors.append(data[y * width + (x+1)])
                    if y > 0:         neighbors.append(data[(y-1) * width + x])
                    if y < height-1:  neighbors.append(data[(y+1) * width + x])
                    if any(n[3] == 0 for n in neighbors):
                        new_data[idx] = (255, 255, 255, 0)
                        changed = True
            data = new_data

    img.putdata(data)
    img.save(output_path, "PNG")
    print(f"  ✅ {os.path.basename(input_path)} → {os.path.basename(output_path)}")


def main():
    # On cible uniquement lulu-om pour commencer
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    images_dir = os.path.join(base_dir, "public", "images")

    targets = sys.argv[1:] if len(sys.argv) > 1 else None

    if targets:
        sources = [os.path.join(images_dir, t) for t in targets]
    else:
        sources = sorted(glob.glob(os.path.join(images_dir, "lulu*.jpg")))

    # Images dont le corps blanc ne doit PAS être érodé
    NO_ERODE = {"lulu-equilibre.jpg", "lulu-amm.jpg", "lulu-chaise.jpg"}

    print(f"🖼  {len(sources)} image(s) — suppression fond + zones internes...\n")
    for src in sources:
        basename = os.path.basename(src)
        name = os.path.splitext(basename)[0]
        dst = os.path.join(images_dir, f"{name}-nobg.png")
        erode = basename not in NO_ERODE
        remove_white_background(src, dst, tolerance=30, erode=erode)
    print(f"\n✨ Terminé !")


if __name__ == "__main__":
    import sys
    main()
