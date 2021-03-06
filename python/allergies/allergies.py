class Allergies:

	def __init__(self, score=0):
		
		self.score = score
		self.allergies_list = ['cats', 'pollen', 'chocolate', 'tomatoes', 'strawberries', 'shellfish', 'peanuts', 'eggs']
		self.lst = []
		self.temp_list = []
		if score > 0:
			self.binary_score = bin(self.score)
			self.binary_score = self.binary_score[2:] # Remove the leading '0b' from the converted string
			
			for i in range(len(self.binary_score)-1, -1, -1):
				if self.binary_score[i] == '1':
					self.temp_list = self.allergies_list[(len(self.allergies_list)-1) - (len(self.binary_score)-1):]
					self.lst.append(self.temp_list[i])

	def is_allergic_to(self, allergen):
			return allergen in self.lst
				
