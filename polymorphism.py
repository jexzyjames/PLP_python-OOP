# Activity 2: Polymorphism Challenge!

class Vehicle:
    """Base class for all vehicles, defining a common 'move' interface."""
    def __init__(self, name):
        self.name = name

    def move(self):
        """
        Abstract method to be overridden by subclasses.
        Represents the action of movement unique to each vehicle type.
        """
        raise NotImplementedError("Subclasses must implement the 'move' method.")

class Car(Vehicle):
    """Represents a car, moving by driving."""
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model

    def move(self):
        """Car moves by driving."""
        print(f"{self.name} ({self.model}): Driving on the road 🚗")

class Plane(Vehicle):
    """Represents a plane, moving by flying."""
    def __init__(self, name, airline):
        super().__init__(name)
        self.airline = airline

    def move(self):
        """Plane moves by flying."""
        print(f"{self.name} ({self.airline}): Flying through the sky ✈️")

class Boat(Vehicle):
    """Represents a boat, moving by sailing/motoring."""
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type # e.g., "Sailboat", "Speedboat"

    def move(self):
        """Boat moves by sailing or motoring on water."""
        print(f"{self.name} ({self.type}): Cruising on the water 🚤")

class Bicycle(Vehicle):
    """Represents a bicycle, moving by pedaling."""
    def __init__(self, name, gears):
        super().__init__(name)
        self.gears = gears

    def move(self):
        """Bicycle moves by pedaling."""
        print(f"{self.name} (Bicycle with {self.gears} gears): Pedaling along the path 🚴")

# --- Demonstration for Activity 2 ---
print("\n--- Activity 2: Polymorphism Challenge Demonstration ---")

# Create instances of different vehicle types
my_car = Car("My Sedan", "Honda Civic")
dream_plane = Plane("Airbus A380", "Emirates")
fishing_boat = Boat("Sea Queen", "Fishing Boat")
mountain_bike = Bicycle("Trail Blazer", 21)

# Put them all in a list
vehicles = [my_car, dream_plane, fishing_boat, mountain_bike]

# Iterate through the list and call the 'move' method on each object
# This demonstrates polymorphism: same method call, different behavior
for vehicle in vehicles:
    vehicle.move()
