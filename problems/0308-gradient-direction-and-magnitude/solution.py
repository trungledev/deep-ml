import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	
	magnitude = np.sqrt(sum([x ** 2 for x in gradient]))
	direction = [x / magnitude for x in gradient]
	descent_direction = [ - x / magnitude for x in gradient]
	if magnitude == 0:
		direction = [0.0 for x in gradient]

	return {"magnitude": magnitude,"direction": direction,"descent_direction":descent_direction}