import sympy

x1,x2,x3,x4,y1,y2,y3,y4,z1,z2,z3,z4,d1,d2,d3,d4,xs,ys,zs = sympy.symbols("x1,x2,x3,x4,y1,y2,y3,y4,z1,z2,z3,z4,d1,d2,d3,d4,xs,ys,zs")

eq1 = sympy.Eq(d1,sympy.sqrt((xs-x1)**2+(ys-y1)**2+(zs-z1)**2))
eq2 = sympy.Eq(d2,sympy.sqrt((xs-x2)**2+(ys-y2)**2+(zs-z2)**2))
eq3 = sympy.Eq(d3,sympy.sqrt((xs-x3)**2+(ys-y3)**2+(zs-z3)**2))
eq4 = sympy.Eq(d4,sympy.sqrt((xs-x4)**2+(ys-y4)**2+(zs-z4)**2))

result = sympy.solve([eq1,eq2,eq3,eq4],(xs,ys,zs))

pickle.dump(result, open( "save.p", "wb" ))
print(result)
