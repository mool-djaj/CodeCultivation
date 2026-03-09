class Plant:
    def __init__(self, name: str, height_of: int, age_of: int) -> None:
        self.name = name
        self.height_of = height_of
        self.age_of = age_of

    def age(self) -> None:
        self.age_of = self.age_of + 1

    def grow(self) -> None:
        self.height_of = self.height_of + 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height_of}cm, {self.age_of} days old")


def ft_plant_growth() -> None:
    plant = Plant("Rose", 25, 30)
    days = 7
    starting_height = plant.height_of
    print("=== Day 1 ===")
    plant.get_info()
    for i in range(days - 1):
        plant.grow()
        plant.age()
    print(f"=== Day {days} ===")
    plant.get_info()
    total_growth = plant.height_of - starting_height
    print(f"Growth this week: +{total_growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
