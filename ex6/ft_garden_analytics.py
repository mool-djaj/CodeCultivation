class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
        self.category = "regular"

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"

    def get_score(self) -> int:
        return self.height


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.category = "flowering"

    def get_info(self) -> str:
        return (f"{super().get_info()}, "
                f"{self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int,
                 color: str, points: int) -> None:
        super().__init__(name, height, color)
        self.points = points
        self.category = "prize flowers"

    def get_info(self) -> str:
        return (f"{super().get_info()}, "
                f"Prize points: {self.points}")

    def get_score(self) -> int:
        return self.height + (self.points * 4)


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        self.plant_count = 0
        self.total_growth = 0

    def add_plant(self, plant: Plant) -> None:
        self.plants += [plant]
        self.plant_count += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1


class GardenManager:
    total_gardens = 0

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> list['Garden']:
        network = []
        for owner in owners:
            network += [Garden(owner)]
            cls.total_gardens += 1
        return network

    class GardenStats:
        @staticmethod
        def validate_height(height: int) -> bool:
            return height > 0

        @staticmethod
        def calculate_score(garden: Garden) -> int:
            score = 0
            for plant in garden.plants:
                score += plant.get_score()
            return score


def ft_garden_analytics() -> None:
    print("=== Garden Management System Demo ===\n")
    owners = ["Alice", "Bob"]
    network = GardenManager.create_garden_network(owners)
    alice_garden = network[0]
    bob_garden = network[1]

    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(
        PrizeFlower("Sunflower", 50, "yellow", 10))

    bob_garden.plants += [Plant("Shrub", 92)]
    bob_garden.plant_count += 1

    alice_garden.help_plants_grow()
    print("\n=== Alice's Garden Report ===")
    print("Plants in garden:")

    reg_count = 0
    flow_count = 0
    prize_count = 0

    for plant in alice_garden.plants:
        print(f"- {plant.get_info()}")
        if plant.category == "regular":
            reg_count += 1
        elif plant.category == "flowering":
            flow_count += 1
        elif plant.category == "prize flowers":
            prize_count += 1

    print(f"Plants added: {alice_garden.plant_count}, "
          f"Total growth: {alice_garden.total_growth}cm")
    print(f"Plant types: {reg_count} regular, "
          f"{flow_count} flowering, "
          f"{prize_count} prize flowers")

    is_valid = GardenManager.GardenStats.validate_height(101)
    print(f"Height validation test: {is_valid}")

    alice_score = GardenManager.GardenStats.calculate_score(
        alice_garden)
    bob_score = GardenManager.GardenStats.calculate_score(
        bob_garden)

    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    ft_garden_analytics()
