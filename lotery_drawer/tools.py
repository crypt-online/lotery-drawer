import numpy as np

def compute3DRandomSeed(x, y, z):
	h = np.uint32(z)
	h += np.uint32(x) * np.uint32(374761393) + np.uint32(y) * np.uint32(668265263)
	h = (h ^ (h >> np.uint32(13))) * np.uint32(1274126177)
	h = h ^ (h >> np.uint32(16))
	return h