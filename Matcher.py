import os
from PIL import Image
import imagehash

def compare_images(query_image, directory):
    # Compute the perceptual hash for the query image
    query_hash = imagehash.dhash(Image.open(query_image))

    # Iterate through the directory and compare the hashes
    for filename in os.listdir(directory):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            img_path = os.path.join(directory, filename)
            img_hash = imagehash.dhash(Image.open(img_path))
            
            # Check if the hashes are similar
            if abs(query_hash - img_hash) < 10:
                return filename.split('.')[0]

    return "No matching Pokémon found."

# Example usage
query_image = "D:\Coding\PK2 Data\Test 2.jpg"
directory = "Images"
pokemon_name = compare_images(query_image, directory)
print(pokemon_name)