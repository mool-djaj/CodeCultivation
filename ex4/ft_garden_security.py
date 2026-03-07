class Plant:
	def __init__(self, name):
		self.name = name
		self.height = 0
		self.age = 0

	def get_height(self,height_of):
		if height_of < 0:
			print(f"Invalid operation attempted: height {height_of}cm [REJECTED]")
			print(f"Security: Negative height rejected\n")
		else:
			self.height = height_of
			print(f"Height updated: {self.height}cm [OK]")

	def get_age(self,age_of):
		if age_of < 0:
			print(f"Invalid operation attempted: age {age_of} days[REJECTED]")
			print(f"Security: Negative time rejected\n")
		else:
			self.age = age_of
			print(f"Age updated: {self.age} days [OK]")

	def set_height(self,height_of):
		self.get_age(height_of)
	
	def set_age(self,age_of):
		self.get_age(age_of)


def ft_garden_security():
	print("=== Garden Security System ===")
	plant = Plant("Rose")
	plant.set_height(25)
	plant.set_age(51)

	if (plant.height >= 0) and (plant. age >= 0):
		print(f"Current plant: Rose ({plant.height}cm, {plant.age} days)")

ft_garden_security()

	