def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	m = len(matrix)
	n = len(matrix[0])
	match mode:
		case "column":
			return [sum([matrix[j][i] for j in range(m)]) / m for i in range(n)]
		case "row":
			return [sum([matrix[i][j] for j in range(n)]) / n for i in range(m)]
	return []