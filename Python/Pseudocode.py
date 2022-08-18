from functools import total_ordering


Total= 0

R10= int(input("Number of R10 notes"))
R20= int(input("Number of R20 notes"))
R50=int(input("Number of R50 notes"))
R100=int(input("Number of R100 notes"))
R200=int(input("Number of R200 notes"))

Total= R10 + R20 + R50 + R100 + R200
print("")
print("Total : " + str(Total))
print("")