class Trip:
	def __init__(self, name):
		self.name = name
		self.participantFactory = PersonFactory()
		self.expensesFactory = ExpensesFactory()