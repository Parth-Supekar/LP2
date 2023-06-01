# Python3 program for the above approach

# DFS memoization
adjMatrix=[]
mp=dict()

# Function to implement DFS Traversal
def DFSUtility(node, stops, dst, cities):
	# Base Case
	if (node == dst):
		return 0

	if (stops < 0) :
		return 1e9

	key=(node, stops)

	# Find value with key in a map
	if key in mp:
		return mp[key]

	ans = 1e9

	# Traverse adjacency matrix of
	# source node
	for neighbour in range(cities):
		weight = adjMatrix[node][neighbour]

		if (weight > 0) :

			# Recursive DFS call for
			# child node
			minVal = DFSUtility(neighbour, stops - 1, dst, cities)

			if (minVal + weight > 0):
				ans = min(ans, minVal + weight)
		
	

	mp[key] = ans

	# Return ans
	return ans


# Function to find the cheapest price
# from given source to destination
def findCheapestPrice(cities, flights, src, dst, stops):
	global adjMatrix
	# Resize Adjacency Matrix
	adjMatrix=[[0]*(cities + 1) for _ in range(cities + 1)]

	# Traverse flight[][]
	for item in flights:
		# Create Adjacency Matrix
		adjMatrix[item[0]][item[1]] = item[2]
	

	# DFS Call to find shortest path
	ans = DFSUtility(src, stops, dst, cities)

	# Return the cost
	return -1 if ans >= 1e9 else int(ans)
	


# Driver Code
if __name__ == '__main__':
	# Input flight : :Source,
	# Destination, Cost
	flights = [[ 4, 1, 1 ],[ 1, 2, 3] , [ 0, 3, 2] , [ 0, 4, 10] , [ 3, 1, 1] , [ 1, 4, 3]]

	# vec, n, stops, src, dst
	stops = 2
	totalCities = 5
	sourceCity = 0
	destCity = 4

	# Function Call
	ans = findCheapestPrice(
		totalCities, flights,
		sourceCity, destCity,
		stops)

	print(ans)
