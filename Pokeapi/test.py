path = "C:\\Users\\Asus\\Desktop\\XD\\python\\Pokeapi\\requests-api\\Output.txt"

num_pal = 0

with open(path, "r") as text_file:
    for line in text_file:
        palabras = line.split()
        num_pal += len(palabras)

print(palabras)
print(num_pal)