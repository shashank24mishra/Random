import time

class Random_Number:
	def random_no(self, **kwargs):
		self.start = kwargs.get('start',0)	#Intializing start range for random number
		self.end = kwargs.get('end',0)		#Intializing end range for random number
		self.total = kwargs.get('total',0)	#Intializing total number for total number of random number required
		self.bais_73 = 0			#Intializing counter for 73% biased to the higher number
		self.bais_27 = 0			#Intializing counter for 27% biased to the lower number
		
		while (self.bais_27 + self.bais_73) < self.total :     #loop running till total count reach
			
			time_ = int(time.time())			# generating long int value
			clock_ = int(str(time.clock()).split('.')[1])	# generating int value

			result = (clock_ * time_)%self.end	        # For result less than end range 

			if result >= self.start:			# Condition to check result should be greater than or equal start range
				if self.bais_27<((self.total * 27)//100) and result < (self.end//2):	# Condition for 27% biased
					self.bais_27+=1
				else:									# Otherwise 73% biased
					self.bais_73+=1
				yield result

