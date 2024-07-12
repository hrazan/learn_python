import colorgram as cg

colors_ = cg.extract("image.jpg", 100)
colors_rgb = []

for color in colors_:
    colors_rgb.append((color.rgb.r, color.rgb.g, color.rgb.b))

print(colors_rgb)
