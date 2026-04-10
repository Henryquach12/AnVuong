import math
class Planet:
    def __init__(self, name, mass, diameter, density, gravity, distance_from_sun, mean_temperature, moon_count, ring_system, global_magnetic_field):
        self.name = name
        self.weight = weight
        self.diameter = diameter
        self.density = density
        self.gravity = gravity
        self.distance_from_sun = distance_from_sun
        self.mean_temperature = mean_temperature
        self.moon_count = moon_count
        self.ring_system = ring_system
        self.global_magnetic_field = global_magnetic_field
    def radius(self):
        radius = self.diameter / 2
        return radius
    def surface_area(self):
        surface_area = 4 * math.pi * (self.radius())**2 
        return surface_area
    def mass(self):
        mass = self.weight * self.gravity
        return mass
    def planet_weight(self):
        weight = weight * (gravity/9.8)
        
    def __str__(self):
        description = f"Planet: {self.name}\n"
        description += f"Mass: {self.mass}\n"
        description += f"Diameter: {self.diameter}\n"
        description += f"Density: {self.density}\n"
        description += f"Gravity: {self.gravity}\n"
        description += f"Distance from Sun: {self.distance_from_sun}\n"
        description += f"Mean Temperature: {self.mean_temperature}\n"
        
        if self.moon_count == 0:
            description += "This planet has no moons.\n"
        else:
            description += f"This planet has {self.moon_count} moons.\n"

        if self.ring_system:
            description += "This planet has a ring system.\n"
        else:
            description += "This planet does not have a ring system.\n"

        if self.global_magnetic_field:
            description += "This planet has a global magnetic field.\n"
        else:
            description += "This planet does not have a global magnetic field.\n"

        return description