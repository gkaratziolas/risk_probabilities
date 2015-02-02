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



def p_victory(attackers, defenders, survivors):
    """attackers = number of your men,
       defenders = number of their men,
       survivors = number of your men in 
       their teritory after the fight."""

    p = 0

    #impossible to reach survivor goal
    if attackers < 1 or attackers < survivors:
        return 0

    #survivor goal has been met
    elif defenders <= 0:
        return 1

    elif attackers >= 3 and defenders >= 2:
        p += pv3_2 * p_victory(attackers,   defenders-2, survivors)
        p += pd3_2 * p_victory(attackers-1, defenders-1, survivors)
        p += pl3_2 * p_victory(attackers-2, defenders,   survivors)
    elif attackers >= 3 and defenders == 1:
        p += pv3_1 * p_victory(attackers,   defenders-1, survivors)
        p += pl3_1 * p_victory(attackers-1, defenders,   survivors)
    elif attackers == 2 and defenders >= 2:
        p += pv2_2 * p_victory(attackers,   defenders-2, survivors)
        p += pd2_2 * p_victory(attackers-1, defenders-1, survivors)
        p += pl2_2 * p_victory(attackers-2, defenders,   survivors)
    elif attackers == 2 and defenders == 1:
        p += pv2_1 * p_victory(attackers,   defenders-1, survivors)
        p += pl2_1 * p_victory(attackers-1, defenders,   survivors)
    elif attackers == 1 and defenders == 2:
        p += pv1_2 * p_victory(attackers,   defenders-1, survivors)
        p += pl1_2 * p_victory(attackers-1, defenders,   survivors)
    elif attackers == 1 and defenders == 1:
        p += pv1_1 * p_victory(attackers,   defenders-1, survivors)
        p += pl1_1 * p_victory(attackers-1, defenders,   survivors)


    return p

n = 1000

print(p_victory(n,2,n-7))