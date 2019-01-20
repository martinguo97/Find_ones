class number_of_digit_one:
	def __init__(self):
		self.iter_memo={}

	def countDigitOne(self,n):
		number=str(n)
		start=0
		answer=0
		if number.endswith('0'):
			while start<n:
				answer+=self.iter_memo[start]
				start+=10
			return answer
		else:
			last=str(n)[-1]
			end_index=n-int(last)
			print(end_index)
			while start<end_index:
				answer+=self.iter_memo[start]
				start+=10
			for i in range(end_index,n+1):
				num=str(i)
				for element in num:
					if element=='1':
						answer+=1
			return answer

		

	def memo(self):
		self.iter_memo={0:2,10:10,20:1,30:1,40:1,50:1,60:1,70:1,80:1,90:2}
		number=100
		while number<=10000000:
			counter=0
			if str(number).startswith('1'):
				counter+=10
			rest=str(number)[1:]
			rest=rest.lstrip('0')
			if len(rest)==0:
				self.iter_memo[number]=counter+self.iter_memo[0]
				number+=10
				continue
			self.iter_memo[number]=counter+self.iter_memo[int(rest)]
			number+=10
		# print(self.iter_memo)
		return self.iter_memo




	def ones(self,n):
		counter=0
		for i in range(0,n+1):
			num=str(i)
			for element in num:
				if element=='1':
					counter+=1
		print(counter)
		return counter
