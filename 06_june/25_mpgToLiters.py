def mpg2lp100km(n):
    return round((100*3.78541178)/(1.609344*n),2)

print mpg2lp100km(42)

def lp100km2mpg(n):
    return round((100*3.78541178)/(1.609344*n),2)

print lp100km2mpg(9)