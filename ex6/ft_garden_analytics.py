class Plant:
    def __init__(self, name: str, hight: int) -> None:
        self.name = name
        self.hight = hight
        self.category = "regular"

    def grow(self) -> None:
        self.hight += 1

    def get_info(self) -> str:
        return f"- {self.name}: {self.hight}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, hight: int, color: str) -> None:
        super().__init__(name, hight)
        self.color = color
        self.blooming = False
        self.category = "flowering"

    def bloom(self) -> str:
        self.blooming = True
        return f"{self.get_info()}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        hight: int,
        color: str,
        prize_points: int,
    ) -> None:
        super().__init__(name, hight, color)
        self.prize_points = prize_points
        self.category = "prize"

    def prize(self) -> str:
        return f"{self.bloom()}, prize point: {self.prize_points}"


class GardenManager:
    total_gardens = 0

    class GardenStats:
        def __init__(self) -> None:
            self.total_plants = 0
            self.total_growth = 0
            self.regular_count = 0
            self.flowering_count = 0
            self.prize_count = 0
            self.total_grow = 0
            self.prize = 0

        def calculate(self, plants: list[Plant]) -> None:
            for plant in plants:
                if plant.category == "prize":
                    self.prize_count += 1
                    self.total_plants += 1
                    self.prize = plant.prize_points
                elif plant.category == "flowering":
                    self.flowering_count += 1
                    self.total_plants += 1
                else:
                    self.regular_count += 1
                    self.total_plants += 1

                self.total_growth += plant.hight

    def __init__(self, name: str) -> None:
        self.name = name
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all(self) -> None:
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.total_grow += 1
            print(f"{plant.name} grew 1cm")

    def get_all_info(self) -> None:
        for plant in self.plants:
            if plant.category == "prize":
                print(plant.prize())
            elif plant.category == "flowering":
                print(plant.bloom())
            else:
                print(plant.get_info())

    @classmethod
    def create_garden_network(cls) -> None:
        print(f"Total gardens managed: {GardenManager.total_gardens}")

    @staticmethod
    def is_valid_height(height: int) -> bool:
        if height > 0:
            return True
        return False

    def get_report(self) -> None:
        self.stats.calculate(self.plants)
        print(f"=== {self.name}'s Garden Report ===")
        self.get_all_info()
        print(
            f"Plants added: {self.stats.total_plants}, "
            f"Total growth: {self.stats.total_grow}cm"
        )
        print(
            f"Plant types: {self.stats.regular_count} regular, "
            f"{self.stats.flowering_count} flowering, "
            f"{self.stats.prize_count} prize flowers"
        )
        print("")


def ft_garden_analytics() -> None:
    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    print("=== Garden Management System Demo ===\n")

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    print("")
    alice.grow_all()
    print("")
    alice.get_report()

    alice_score = (
        alice.stats.total_growth
        + alice.stats.prize
        + (alice.stats.prize * alice.stats.total_grow)
    )
    bob_score = (
        bob.stats.total_growth
        + bob.stats.prize
        + (bob.stats.prize * bob.stats.total_grow)
    )
    print(
        "Garden scores - "
        f"Alice: {alice_score}, "
        f"Bob: {bob_score}"
    )

    print(f"Height validation test: {GardenManager.is_valid_height(25)}")
    GardenManager.create_garden_network()


if __name__ == "__main__":
    ft_garden_analytics()
