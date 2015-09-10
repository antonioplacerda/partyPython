class factory:
	items = []
	counter = 0
	idCounter = 0
	
	def create():
		counter += 1
	
	def destroy(ID):
		counter -= 1
		
	def getFromDB:
		print("To be done")