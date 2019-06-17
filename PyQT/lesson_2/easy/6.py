class AnyClass():
    pass

ac = AnyClass()
print(ac)

# type - стандартный метакласс в Python
AnyClass1 = type('AnyClass1', (), {})
amc = AnyClass1()

#print(amc)
#print(amc.__class__)
#print(amc.__class__.__class__)

