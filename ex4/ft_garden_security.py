class SecurePlant:
    def __init__(self, name: str) -> None:
        self.name = name
        self.height = 0
        self.age = 0

    def get_height(self) -> int:
        return self.height

    def set_height(self, height_of: int) -> None:
        if height_of < 0:
            print("Invalid operation attempted:"
                  f" height {height_of}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.height = height_of
            print(f"Height updated: {self.height}cm [OK]")

    def get_age(self) -> int:
        return self.age

    def set_age(self, age_of: int) -> None:
        if age_of < 0:
            print("Invalid operation attempted:"
                  f" age {age_of} days[REJECTED]")
            print("Security: Negative time rejected\n")
        else:
            self.age = age_of
            print(f"Age updated: {self.age} days [OK]")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    plant.set_height(25)
    plant.set_age(51)

    plant.get_height()
    plant.get_age()

    if (plant.height >= 0) and (plant.age >= 0):
        print(f"Current plant: Rose ({plant.height}cm, "
              f"{plant.age} days)")


if __name__ == "__main__":
    ft_garden_security()
