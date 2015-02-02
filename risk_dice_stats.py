from __future__ import print_function

pv3_2 = float(0)
pd3_2 = float(0)
pl3_2 = float(0)

pv3_1 = float(0)
pl3_1 = float(0)

pv2_2 = float(0)
pd2_2 = float(0)
pl2_2 = float(0)

pv2_1 = float(0)
pl2_1 = float(0)

pv1_2 = float(0)
pl1_2 = float(0)

pv1_1 = float(0)
pl1_1 = float(0)

def calculate_battle_probabilities():
    for a in range(1,7):
        for b in range(1,7):
            for c in range(1,7):
                for d in range(1,7):
                    for e in range(1,7):
                        if max(a,b,c) > max(d,e):
                            if sorted([a,b,c])[1] > min(d,e):
                                pv3_2 += 1
                            else:
                                pd3_2 += 1
                        else:
                            if sorted([a,b,c])[1] > min(d,e):
                                pd3_2 += 1
    pv3_2 = pv3_2/(6**5)
    pd3_2 = pd3_2/(6**5)
    pl3_2 = 1 - (pv3_2+pd3_2)


    for a in range(1,7):
        for b in range(1,7):
            for c in range(1,7):
                for d in range(1,7):
                    if max(a,b,c) > d:
                        pv3_1 += 1
                    if max(a,b) > max(c,d):
                        if min(a,b) > min(c,d):
                            pv2_2 += 1
                    elif min(a,b) > min(c,d):
                        pd2_2 += 1                
    pv3_1 = pv3_1/(6**4)
    pl3_1 = 1 - pv3_1
    pv2_2 = pv2_2/(6**4)
    pd2_2 = pd2_2/(6**4)
    pl2_2 = 1 - (pv2_2 + pd2_2)


    for a in range(1,7):
        for b in range(1,7):
            for c in range(1,7):
                if a > max(b,c):
                    pv1_2 += 1
                if max(a,b) > c:
                    pv2_1 += 1
    pv2_1 = pv2_1/(6**3)
    pl2_1 = 1 - pv2_1
    pv1_2 = pv1_2/(6**3)
    pl1_2 = 1 - pv1_2


    for a in range(1,7):
        for b in range(1,7):
            if a > b:
                pv1_1 += 1
    pv1_1 = pv1_1/(6**2)
    pl1_1 = 1 - pv1_1

def print_battle_probabilities():
    calculate_battle_probabilities()
    print("pv3_2 =", pv3_2)
    print("pd3_2 =", pd3_2)
    print("pl3_2 =", pl3_2)

    print("pv3_1 =", pv3_1)
    print("pl3_1 =", pl3_1)

    print("pv2_2 =", pv2_2)
    print("pd2_2 =", pd2_2)
    print("pl2_2 =", pl2_2)

    print("pv2_1 =", pv2_1)
    print("pl2_1 =", pl2_1)

    print("pv1_2 =", pv1_2)
    print("pl1_2 =", pl1_2)

    print("pv1_1 =", pv1_1)
    print("pl1_1 =", pl1_1)

print_battle_probabilities()