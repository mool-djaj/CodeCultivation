class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    garden = [plant1, plant2, plant3]
    for i in range(3):
        print(f"{garden[i].name}: {garden[i].height}cm, "
              f"{garden[i].age} days old")


if __name__ == "__main__":
    ft_garden_data()
