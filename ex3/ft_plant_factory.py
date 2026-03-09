class Plant:
    def __init__(self, name: str, starting_height: int,
                 starting_age: int) -> None:
        self.name = name
        self.starting_height = starting_height
        self.starting_age = starting_age

    def get_info(self) -> None:
        print(f"Created: {self.name} ({self.starting_height}cm,"
              f" {self.starting_age} days)")


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Oak", 200, 365)
    plant3 = Plant("Cactus", 5, 90)
    plant4 = Plant("Sunflower", 80, 45)
    plant5 = Plant("Fern", 15, 120)
    plants = [plant1, plant2, plant3, plant4, plant5]
    i = 0
    for plant in plants:
        plant.get_info()
        i = i + 1
    print(f"Total plants created: {i}")


if __name__ == "__main__":
    ft_plant_factory()
