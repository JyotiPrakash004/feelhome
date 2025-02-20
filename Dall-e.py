import os
import random
import google.generativeai as genai
import requests
import shutil

# Replace with your Gemini API key
GEMINI_API_KEY = "MY_API_KEY"

# Configure API key
genai.configure(api_key=GEMINI_API_KEY)

# Function to generate and save Gemini image
def generate_and_save_image(prompt, save_folder="assets"):
    # Ensure the save directory exists
    os.makedirs(save_folder, exist_ok=True)

    # Generate image using Gemini
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt])

    if response and response.parts:
        for idx, part in enumerate(response.parts):
            if hasattr(part, 'image'):
                image_data = part.image.data  # Get image data
                image_path = os.path.join(save_folder, f"image{idx + 1}.png")

                # Save the image
                with open(image_path, "wb") as img_file:
                    img_file.write(image_data)

                print(f"✅ Image saved at: {image_path}")
    else:
        print("❌ No image generated.")

def move_image(source_folder, target_folder_1, target_folder_2,  image_name):
    source_path = os.path.join(source_folder, image_name)
    target_path_1 = os.path.join(target_folder_1, image_name)
    target_path_2 = os.path.join(target_folder_2, image_name)

    condition = True #change it to false if he dislikes the image

    if os.path.exists(source_path):
        if condition:
            shutil.move(source_path, target_path_1)
            print(f"Moved {image_name} from {source_folder} to {target_folder_1}")
        else:
            shutil.move(source_path, target_path_2)
            print(f"Moved {image_name} from {source_folder} to {target_folder_2}")
    else:
        print(f"Error: {image_name} not found in {source_folder}")

# Example Usage
style=["Minimalist",
    "Scandinavian",
    "Industrial",
    "Bohemian",
    "Modern Farmhouse",
    "Coastal",
    "Traditional",
    "Mid-Century Modern",
    "Art Deco",
    "Contemporary"]
room_types = [
    "Kitchen",
    "Bedroom",
    "Bathroom",
    "Living Room/Hall",
    "Balcony/Patio",
    "Study Room",
    "Attic/Basement"]

extras= [["Kitchen Island", "Walk-in Pantry", "Double Oven/Convection Oven", "Commercial Appliances", "Breakfast Nook", "Wet Bar"],
        ["Projector/Home Theater System", "Built-in Speakers/Sound System", "Smart Home Integration", "Lighting", "Gaming Setup/Area", "Dedicated Workspace/Home Office Tech", "Wine Fridge/Beverage Center"],
        ["Soaking Tub", "Steam Shower", "Double Vanity", "Heated Floors", "Bidet", "Makeup Vanity", "Yoga/Meditation Space"],
        ["Built-in Entertainment Center", "Fireplace", "Wet Bar","Standing Desk", "Soundproofing","Built-in Storage"],
        ["Planters & Vertical Gardens", "String Lights or Lanterns", "Decorative Screens or Privacy Panels", "Storage Bench or Cabinets", "Projector", "Mini Bar Cart"],
        ["Whiteboard", "Bookshelves", "Floating Shelve", "Smart Speaker", "Monitor & Laptop Stand", "Soundproofing Panels"],
        ["Workout Equipments", "Insulation & Heating", "Bright LED Ceiling Lights", "Ergonomic Chair & Desk", "LED Strip Lights & Smart Lighting", "Mirrors"]]

i = 0
while i<3:
    i11 = random.randint(0,9)
    i12 = random.randint(0,9)
    while i12==i11:
        i12 = random.randint(0,9)
    i2 = random.randint(0,2)
    i3 = random.randint(0,5)

    st1 = style[i11]
    st2 = style[i12]
    rt = room_types[i2]
    ex = extras[i2][i3]
    generate_and_save_image(f"Interior design, heavily emphasizing {st1}, with secondary influences of {st2}.  The room should be {rt}, and feature {ex}.  High quality, photorealistic rendering")
    i=i+1
    move_image("assets", "liked", "disliked", f"image{i}")
