import random
from .tools import compute3DRandomSeed
class Drawer:
	def __init__(self):
		self.endTimestamp = 0
		self.prizes = []
		self.tickets = []
		self.winners = []

		self.nbUsers = 0

	def draw(self, loteryData):
		self.endTimestamp = loteryData['endTimestamp']

		for prize in loteryData['prizes']:
			for i in range(prize['nb']):
				self.prizes.append(prize['name'])

		self.nbUsers = len(loteryData['tickets'])

		self.tickets = []
		for user in loteryData['tickets']:
			for i in range(loteryData['tickets'][user]):
				self.tickets.append(user)

		random.seed(compute3DRandomSeed(-1, self.nbUsers * len(self.tickets), self.endTimestamp))
		random.shuffle(self.tickets)

		for i in range(len(self.prizes)):
			random.seed(compute3DRandomSeed(i, self.nbUsers * len(self.tickets), self.endTimestamp))
			idx = random.randint(0, len(self.tickets)-1)
			self.winners.append({
				'prizeName': self.prizes[i],
				'username': self.tickets.pop(idx)
			})

		return self.winners