A = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
Z = "F.R.I.E.N.D.S"

# Separarte the string into comma separated values.
B = A.split('.')
print(B)

# sort string alphabetically
C = sorted(Z)
print(C)

# remove character from string
D = Z.replace('R','')
print(D)

# remove dot from string Z
E = Z.replace('.','')
print(E)

# number of occurrence of O in string
F = A.count('O')
print(F)

# number of occurrence of substring in string A
F = A.count('OO')
print(F)