name = input("Enter plant name: ")
plant_type = input("Enter plant type (herb/shrub/tree/climber/creeper): ")

print("\n--- Plant Information---")
print("Name:", name)

if plant_type == "herb":
    print("Type: Herb ")
    print("Characteristics: Small, soft stem, short lifespan")
    print("Uses: Medicine, food, spices")
    print("Examples: Tulsi, Mint, Grass")

elif plant_type == "shrub":
    print("Type: Shrub ")
    print("Characteristics: Medium size, woody stems, bushy")
    print("Uses: Decoration, fencing, fruits")
    print("Examples: Rose, Hibiscus, Lemon plant")

elif plant_type == "tree":
    print("Type: Tree ")
    print("Characteristics: Tall, strong trunk, long lifespan")
    print("Uses: Timber, fruits, shade, oxygen")
    print("Examples: Mango,Pine")

elif plant_type == "climber":
    print("Type: Climber ")
    print("Characteristics: Weak stem, needs support to grow up")
    print("Uses: Vegetables, decoration")
    print("Examples:Money plant, Pea")

elif plant_type == "creeper":
    print("Type: Creeper ")
    print("Characteristics: Weak stem, spreads on ground")
    print("Uses: Food crops, decoration")
    print("Examples: Pumpkin, Watermelon, Sweet potato")

else:
    print(" Invalid plant type!")