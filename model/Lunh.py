class Lunh:

	def __init__(self):
		pass

	def checksum(self, number):
		if int(number) <= 0: return False
		number_str = str(number)[::-1]
		digits = []
		total = 0

		for i in range(len(number_str)):
			if not (i % 2): digits.append(int(number_str[i]) * 2)
			else: digits.append(int(number_str[i]))

			if digits[i] > 9: digits[i] = digits[i] - 9

			total += digits[i]

		return ((total * 9) % 10) == 0
