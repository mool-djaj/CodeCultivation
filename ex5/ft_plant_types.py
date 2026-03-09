class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_common_info(self, plant_type: str) -> str:
        return (f"{self.name} ({plant_type}): "
                f"{self.height}cm, {self.age} days")


class Flower(Plant):
    def __init__(self, name: str, height: int,
                 age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def display_info(self) -> None:
        print(f"{self.get_common_info('Flower')},"
              f" {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        area = int(3.14159 * ((self.height / 100) ** 2))
        print(f"{self.name} provides {area}"
              f" square meters of shade")

    def display_info(self) -> None:
        print(f"{self.get_common_info('Tree')},"
              f" {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def provide_nutrition(self) -> None:
        print(f"{self.name} is rich in"
              f" {self.nutritional_value}")

    def display_info(self) -> None:
        print(f"{self.get_common_info('Vegetable')},"
              f" {self.harvest_season} harvest")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 15, 14, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 800, 3000, 40)

    tomato = Vegetable("Tomato", 80, 90, "summer",
                       "vitamin C")
    carrot = Vegetable("Carrot", 20, 60, "fall",
                       "vitamin A")

    rose.display_info()
    rose.bloom()

    oak.display_info()
    oak.produce_shade()

    tomato.display_info()
    tomato.provide_nutrition()

    tulip.display_info()
    tulip.bloom()

    pine.display_info()
    pine.produce_shade()

    carrot.display_info()
    carrot.provide_nutrition()


if __name__ == "__main__":
    ft_plant_types()
