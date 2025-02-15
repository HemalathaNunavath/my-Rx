#Time complexity O(n) 
# Example:
# Input: [-12, -8 , -7, -5, 2, 4, 5, 11, 15]
# Output : [4, 16, 25, 25, 49, 56, 121, 144, 225]
def sortedSquares(arr):
    n = len(arr)
    left, right = 0, n - 1
    result = [0] * n
    index = n - 1

    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            result[index] = arr[left] ** 2
            left += 1
        else:
            result[index] = arr[right] ** 2
            right -= 1
        index -= 1

    return result
arr = [-12, -8, -7, -5, 2, 4, 5, 11, 15]
print(sortedSquares(arr))

#Given an array of Red Green Blue balls.You have to sort it.
# Constraint : Time complexity O(n)
# Constraint : Space complexity O(1)
def sortColors(arr):
    left, mid, right = 0, 0, len(arr) - 1

    while mid <= right:
        if arr[mid] == 'B':  # Move Blue to the left
            arr[left], arr[mid] = arr[mid], arr[left]
            left += 1
            mid += 1
        elif arr[mid] == 'G':  # Keep Green in the middle
            mid += 1
        else:  # Move Red to the right
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1

    return arr
arr = ['R', 'G', 'B', 'G', 'G', 'R', 'B', 'B', 'G']
print(sortColors(arr))

# Find Minimum Platforms Required for Trains
def minPlatforms(arrivals, departures):
    arrivals.sort()
    departures.sort()

    platform_needed = 0
    max_platforms = 0
    i, j = 0, 0

    while i < len(arrivals):
        if arrivals[i] < departures[j]:
            platform_needed += 1
            max_platforms = max(max_platforms, platform_needed)
            i += 1
        else:
            platform_needed -= 1
            j += 1

    return max_platforms
arrivals = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]
print(minPlatforms(arrivals, departures))