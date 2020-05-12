import sys
import json

from lotery_drawer import Drawer

if __name__ == '__main__':
	fileUrl = sys.argv[1]

	with open(fileUrl, 'r') as file:
		dataLotery = json.load(file)
		drawer = Drawer()
		winners = drawer.draw(dataLotery)
		print(winners)