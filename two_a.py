def presents(dimensions):
    f = open(dimensions,'r')
    dimensions = f.read()
    dimensions = dimensions.splitlines()
    fabric = 0
    for i in range(len(dimensions)):
        package = dimensions[i].split('x')
        package = sorted(map(int,package))
        l = package[0]
        w = package[1]
        h = package[2]
        fabric += (2*l*w) + (2*w*h) + (2*h*l) +  (package[0] * package[1])
    return fabric

