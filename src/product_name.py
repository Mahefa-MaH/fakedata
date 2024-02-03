import random

# Functions to randomly select words from each category
def choose_adjective():
    categories = {
        "benefit": ["sustainable", "comfortable", "durable", "high-performance", "versatile", "luxurious", "affordable", "innovative", "natural", "organic", "eco-friendly"],
        "emotion": ["stylish", "sleek", "chic", "trendy", "cozy", "calming", "empowering", "playful", "nostalgic", "adventurous"],
        "descriptive": ["lightweight", "breathable", "waterproof", "dustproof", "shockproof", "hypoallergenic", "stain-resistant", "energy-efficient", "long-lasting"]
    }
    category = random.choice(list(categories.keys()))
    return random.choice(categories[category])

def choose_noun():
    categories = {
        "product": ["dress", "shirt", "backpack", "headphones", "smartphone", "coffee mug", "candle", "organizer", "tool"],
        "benefit": ["solution", "saver", "booster", "optimizer", "enhancer", "companion", "essential", "protector", "delight"],
        "descriptive": ["breeze", "haven", "shield", "whisper", "spark", "balance", "whisper", "touch", "glow"],
        "figurative": ["haven", "whisper", "oasis", "escape", "spark", "haven", "edge", "peak", "ascent"]
    }
    category = random.choice(list(categories.keys()))
    return random.choice(categories[category])

def choose_verb():
    categories = {
        "action": ["transform", "elevate", "simplify", "connect", "empower", "protect", "maximize", "boost", "refresh"],
        "benefit": ["energize", "soothe", "illuminate", "amplify", "streamline", "elevate", "empower", "transform", "personalize"]
    }
    category = random.choice(list(categories.keys()))
    return random.choice(categories[category])

def choose_other_word():
    options = ["Eco", "Pro", "Lite", "Max", "Luxe", "Mini", "Plus", "Travel", "Smart"]
    return random.choice(options)

def choose_rhyming_word(word):
    rhymes = {
        "care": ["fair"],
        "light": ["bright"],
        "dream": ["team"],
        "fit": ["hit"],
        "cool": ["rule"]
    }
    if word in rhymes:
        return random.choice(rhymes[word])
    else:
        return word

def build_product_name(structure):
    name = ""
    for element in structure:
        if element == "adjective":
            name += choose_adjective() + " "
        elif element == "noun":
            name += choose_noun() + " "
        elif element == "verb":
            name += choose_verb() + " "
        elif element == "other":
            name += choose_other_word() + " "
        elif element == "rhyme":
            rhyming_word = choose_rhyming_word(name.split()[-1])
            name = name[:-len(name.split()[-1])] + rhyming_word + " "
        else:
            name += element + " "
    return name.strip()

# Generate different product name variations
structures = [
    ["adjective", "noun"],
    ["adjective", "verb", "noun"],
    ["noun", "adjective", "other"],
    ["verb", "rhyme", "other", "noun"],
    ["adjective", "noun", "verb", "other"],
    ["noun", "other", "verb", "noun"]
]

for structure in structures:
    print(build_product_name(structure))
