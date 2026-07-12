base = int(input("Enter the base of parallelogram:"))
height = int(input("Enter the height of parallelogram:"))
print("area of parallelogram:", base*height)

diagonal1 = int(input("Enter the diagonal of rhombus:"))
diagonal2 = int(input("Enter the diagonal of rhombus:"))
print("area of rhombus:", diagonal1*diagonal2)

parallelside1 = int(input("Enter the parallel side of trapeziod:"))
parallelside2 = int(input("Enter the parallel side of trapeziod:"))
height = int(input("Enter the height of trapeziod:"))
print("area of trapeziod:", 0.5 * (parallelside1 + parallelside2) *height)

numberofsides = int(input("Enter the number of sides of pentagon:"))
lengthofeachside = int(input("Enter the length of each side of pentagon:"))
tan = int(input("Enter the tangent of pentagon:"))
print("area of pentagon", (numberofsides*(lengthofeachside*lengthofeachside)/4 *tan*(3.1416/numberofsides)))