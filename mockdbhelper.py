class MockDBHelper:
	def connect(self, database="crimemap"):
		pass

	def get_all_inputs(self):
		return []

	def add_input(self, data):
		pass

	def clear_all(self):
		pass

	def add_crimes(self, category, date, latitude, longitude, description):
		pass

	def get_all_crimes():
		return [{ 'latitude': 41.257851, 
    		'longitude': -95.986908, 
    		'date': "2000-01-01", 
    		'category': "mugging", 
    		'description': "mock description" }] 


		