class A:
    varA = "wlc to class A "
class B:
    varB = "wlc to class B "
class c( A, B):
    varC = "wlc to class C"
c1 = c()
print(c1.varA)
print(c1.varB)
print(c1.varC)

