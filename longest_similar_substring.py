# Driver Code
if __name__ == '__main__':
	A = [3, 6, 7, 4, 2, 7, 9, 1, 0, 3, 5, 6]
	B = [1, 5, 6, 9, 7, 4, 2, 7, 9, 9, 2, 1]

	# Function call to find
	# maximum length of subarray
	n = len(A)
	m = len(B)

        # Auxillary dp[][] array
	dp = [[0 for i in range(n + 1)] for i in range(m + 1)]

        # Updating the dp[][] table
        # in Bottom Up approach
	for i in range(n - 1, -1, -1):
		for j in range(m - 1, -1, -1):

                        # If A[i] is equal to B[i]
                        # then dp[j][i] = dp[j + 1][i + 1] + 1
			if A[i] == B[j]:
				dp[j][i] = dp[j + 1][i + 1] + 1
	maxm = 0
	maxele = 0
        # Find maximum of all the values
        # in dp[][] array to get the
        # maximum length
	idx = 0
	for i in dp:
		for j in i:

                        # Update the length
			maxm = max(maxm, j)
			if maxm > maxele:
				idx = j-1
				maxele = maxm
	ans = [] 
	while maxm > 0:
		ans.append(B[idx])
		idx = idx+1
		maxm = maxm-1
	print(ans)
