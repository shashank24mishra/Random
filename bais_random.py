import time

class Random_Number:
	def __init__(self):
		self.start = None
		self.end = None
		self.total = None
		

	def random_no(self, **kwargs):
		self.start = kwargs.get('start',0)
		self.end = kwargs.get('end',0)
		self.total = kwargs.get('total',0)
		self.bais_73 = 0
		self.bais_27 = 0
		while (self.bais_27 + self.bais_73) < self.total :

			time_ = int(time.time())
			clock_ = int(str(time.clock()).split('.')[1])
			
			result = (clock_ * time_)%self.end	
			
			if result >= self.start:
				if self.bais_27<((self.total * 27)//100) and result < (self.end//2):
					self.bais_27+=1
				else:
					self.bais_73+=1
				yield result
		
