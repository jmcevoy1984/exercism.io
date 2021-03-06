class Garden:

	__default_students = (
        'Alice', 'Bob', 'Charlie', 'David',
        'Eve', 'Fred', 'Ginny', 'Harriet',
        'Ileana', 'Joseph', 'Kincaid', 'Larry'
        )
        
	def __init__(self,  garden_str, students = __default_students):

		#Split into a list of two rows with index 0 being the top row and index 1 being the bottom row
		self.garden_list = garden_str.split('\n')

		#Redefines the list so that it has 2 elements (Top row and Bottom row) made up of lists containing 2 characters eg: ['RV']
		self.garden_list = [
		[row_str[letter_index:letter_index+2] for letter_index in range(0, len(row_str)-1, 2)]
		for row_str in self.garden_list
		]
		
		#Sort students alphabetically
		self.students_list = sorted(students)

		self.plants_dict = {
		'G':'Grass',
		'C':'Clover', 
		'R':'Radishes', 
		'V':'Violets'
		}

		#Make a dictionary that links the students name with the letters for top row + bottom row eg: {'Alice':'RVCV'}
		self.student_plants_dict = {self.students_list[i]:self.garden_list[0][i] + self.garden_list[1][i] for i in range(len(self.garden_list[0]))}

	def plants(self, student_str):#Converts the letters linked with the student's name into a list of plant names and return the list
		self.letters = self.student_plants_dict[student_str]
		self.plants_list = [self.plants_dict[letter] for letter in self.letters]
		return self.plants_list
