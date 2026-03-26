class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0
            self._shade_calls = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def record_shade(self) -> None:
            self._shade_calls += 1

        def display(self, is_tree: bool) -> None:
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, {self._show_calls} show")
            if is_tree:
                print(f" {self._shade_calls} shade")

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self._stats = Plant.Stats()

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> 'Plant':
        return cls("Unknown plant", 0.0, 0)

    def grow(self) -> None:
        self.height += 1.0
        self._stats.record_grow()

    def age(self) -> None:
        self.age_days += 1
        self._stats.record_age()

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")
        self._stats.record_show()

class Flower(Plant):
    def __init__(self, name: str, height: float, age_days: int, color: str) -> None:
        super().__init__(name, height, age_days)
        self.color = color
        self.has_bloomed = False

    def bloom(self) -> None:
        self.has_bloomed = True
        print(f"{self.name} is blooming beautifully!")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.has_bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

class Seed(Flower):
    def __init__(self, name: str, height: float, age_days: int, color: str) -> None:
        super().__init__(name, height, age_days, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")

class Tree(Plant):
    def __init__(self, name: str, height: float, age_days: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age_days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of {self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide.")
        self._stats.record_shade()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

def display_plant_stats(plant: Plant) -> None:
    print(f"\n[statistics for {plant.name}]")
    is_tree = isinstance(plant, Tree)
    plant._stats.display(is_tree)

def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old ===")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_a_year(400)}")

    rose = Flower("Rose", 15.0, 10, "red")
    print("\n=== Flower ===")
    rose.show()
    display_plant_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_stats(rose)

    oak = Tree("Oak", 200.0, 365, 5.0)
    print("\n=== Tree ===")
    oak.show()
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)

    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    print("\n=== Seed ===")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)

    anon = Plant.create_anonymous()
    print("\n=== Anonymous ===")
    anon.show()
    display_plant_stats(anon)

if __name__ == "__main__":
    ft_garden_analytics()