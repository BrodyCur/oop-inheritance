class System:

  galactic_bodies = []

  def __init__(self, name):
    self.name = name
    self.bodies = []

  def add(self, body):
    if body not in self.bodies:
      self.bodies.append(body)
      System.galactic_bodies.append(body)
    else:
      print("Already added!")

  def total_mass(self):
    total = 0
    for body in self.bodies:
      total += body.mass
    return total

  @classmethod
  def galactic_mass(cls):
    galactic_total = 0
    for body in cls.galactic_bodies:
      galactic_total += body.mass
    return galactic_total

  def print_bodies(self):
    for body in self.bodies:
      print(f"{body}")

class Body:

  def __init__(self, name, mass):
    self.name = name
    self.mass = mass


# TODO: make communicate with subclasses to get class type for single method instead of all() in all subclasses.
  # @classmethod
  # def all(cls, system):
  #   results = []
  #   for body in System.bodies:
  #     if isinstance(body, Star):
  #       results.append(body)
  #   print(results)


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
    for planet in system.bodies:
      if isinstance(planet, Planet):
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
    for body in system.bodies:
      if isinstance(star, Star):
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
    for moon in system.bodies:
      if isinstance(moon, Moon):
        moons.append(moon)
    print(moons)
  
  def __repr__(self):
      return f"{self.name}, {self.mass}, {self.month}, {self.planet}"

solar = System("Solar")

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

# print(solar.total_mass())

# Planet.all(solar)
# Star.all(solar)
# Moon.all(solar)

centauri = System("Alpha Centauri")

kentaurus = Star("Rigil Kentaurus", 18390000, "G2-Type")
toliman = Star("Toliman", 18250000, "K1-Type")
proxima = Star("Proxima Centauri", 17490000, "M6-Type")

proxima_b = Planet("Proxima Centauri b", 5438000, 22, 342)

centauri.add(kentaurus)
centauri.add(toliman)
centauri.add(proxima)
centauri.add(proxima_b)

solar.print_bodies()
centauri.print_bodies()

print(System.galactic_mass())
