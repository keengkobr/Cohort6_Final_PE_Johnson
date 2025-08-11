import math

def mach1():
    return 2 * math.pi * ((15/2) ** 2)

def mach2():
    return (3/4) * (20 ** 2)

def mach3():
    return 18 ** 2

def auto_compare():
    mach1Area = mach1()
    mach2Area = mach2()
    mach3Area = mach3()
    mach1Eff = mach1Area / 20
    mach2Eff = mach2Area / 20 
    mach3Eff = mach3Area / 18
    print(f"A1 eff: {mach1Eff}\nA2 eff: {mach2Eff}\nA3 eff: {mach3Eff}")
    if(mach1Eff > mach2Eff):
        if(mach2Eff > mach3Eff):
            print("The first Automatron is most efficient!")
        elif(mach3Eff > mach1Eff):
            print("The third Automatron is most efficient!")
    elif mach2Eff > mach1Eff:
        if(mach1Eff > mach3Eff):
            print("The second Automatron is most efficient!")
        elif(mach3Eff > mach2Eff):
            print("The third Automatron is most efficient!")

auto_compare()