def get_corners(n): # every odd number is a layer
    return [n**2+1 + n, n**2+1 + n + n+1, n**2+1 + n + 2*(n+1), n**2+1 + n + 3*(n+1)]

corners = [1]
for n in range(0,500):# this prints all the layers up until 7x7. For 1001 I need to put the upper limit to 500
    corners.extend(get_corners(2*n+1))

print(sum(corners))