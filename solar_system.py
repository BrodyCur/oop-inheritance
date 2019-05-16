class System:

  bodies = []

  def add(self, body):
    if body not in System.bodies:
      System.bodies.append(body)
    else:
      print("Already added!")

  def total_mass(self):
    total = 0
    for body in System.bodies:
      total += body
    return total

  def print_bodies(self):
    for body in System.bodies:
      print(f"{body}")

class Body:

  def __init__(self, name, mass):
    self.name = name
    self.mass = mass


class Planet(Body):
  
  def __init__(self, name, mass, day, year):
    super().__init__(name, mass)
    self.day = day
    self.year = year

  def __repr__(self):
      return f"{self.name}, {self.mass}, {self.day}, {self.year}"

  @classmethod
  def all(cls, system):
    planets = []
    for planet in System.bodies:
      if hasattr(planet, "day") is True:
        planets.append(planet)
    print(planets)

class Star(Body):
  
  def __init__(self, name, mass, type):
    super().__init__(name, mass)
    self.type = type

  def __repr__(self):
      return f"{self.name}, {self.mass}, {self.type}"

  @classmethod
  def all(cls, system):
    stars = []
    for star in System.bodies:
      if hasattr(star, "type") is True:
        stars.append(star)
    print(stars)

class Moon(Body):
  
  def __init__(self, name, mass, month, planet):
    super().__init__(name, mass)
    self.month = month
    self.planet = planet

  @classmethod
  def all(cls, system):
    moons = []
    for moon in System.bodies:
      if hasattr(moon, "month") is True:
        moons.append(moon)
    print(moons)
  
  def __repr__(self):
      return f"{self.name}, {self.mass}, {self.month}, {self.planet}"

solar = System()

sol = Star("Sol", 19890000, "G-type")

earth = Planet("Earth", 5972000, 24, 365)
luna = Moon("Luna", 734700, 27, earth.name) 

mars = Planet("Mars", 5764000, 25, 687)
phobos = Moon("Phobos", 547800, 27, mars.name)

venus = Planet("Venus", 3567000, 2784, 225)

jupiter = Planet("Jupiter", 9999000, 9, 4380)
europa = Moon("Europa", 234300, 4, jupiter.name)
ganymede = Moon("Ganymede", 546900, 7, jupiter.name)
io = Moon("Io", 765400, 2, jupiter.name)


solar.add(sol)
solar.add(earth)
solar.add(luna)
solar.add(mars)
solar.add(phobos)
solar.add(venus)
solar.add(jupiter)
solar.add(europa)
solar.add(ganymede)
solar.add(io)
solar.add(mars)

# solar.total_mass()

# solar.print_bodies()

Planet.all(solar)
Star.all(solar)
Moon.all(solar)
