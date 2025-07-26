animal = input()

switch_animal = {
    "dog": "mammal",
    "snake": "reptile",
    "crocodile": "reptile",
    "tortoise": "reptile",
}

print(switch_animal.get(animal, "unknown"))