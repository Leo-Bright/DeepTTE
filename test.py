import numpy as np

a2 = [4, 5, 1, 3, 6, 3, 2]

a2 = np.asarray(a2)

mask = np.arange(np.asarray([5])) < a2[:, None]
# padded = np.zeros(mask.shape, dtype = np.float32)
# padded[mask] = seqs
# print padded
print mask