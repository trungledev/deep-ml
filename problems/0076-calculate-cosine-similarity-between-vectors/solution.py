import numpy as np
from numpy.linalg import norm

def cosine_similarity(A, B):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here

	cosine = np.dot(A, B) / (norm(A) * norm(B))
	return cosine