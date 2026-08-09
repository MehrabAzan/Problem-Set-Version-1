def planet_lookup(planet_name):
    if planetary_info.get(planet_name) == None:
        return "Sorry, I have no data on that planet"
    return f"Planet {planet_name} has an orbital period of {planetary_info[planet_name]["Orbital Period"]} Earth days and has {planetary_info[planet_name]["Moons"]} moons."

planetary_info = {
    "Mercury": {
        "Moons": 0,
        "Orbital Period": 88
    },
    "Earth": {
        "Moons": 1,
        "Orbital Period": 365.25
    },
    "Mars": {
        "Moons": 2,
        "Orbital Period": 687
    },
    "Jupiter": {
        "Moons": 79,
        "Orbital Period": 10592
    }
}

print(planet_lookup("Jupiter"))
print(planet_lookup("Pluto"))