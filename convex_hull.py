
def jarvis(zb):
    
    leftmost = zb[0]
    for point in zb:
        if point[0] < leftmost[0] or (point[0] == leftmost[0] and point[1] < leftmost[1]):
            leftmost = point

    
    hull = []
    pidx = zb.index(leftmost)
    p = leftmost
    while True:
        hull.append(p)
        
        q1 = (pidx + 1) % len(zb)
        q = zb[q1]
        
        for r in zb:
            if ((q[1] - p[1]) * (r[0] - q[0]) - (r[1] - q[1]) * (q[0] - p[0]) > 0):
                q = r
                
        p = q

        if p == leftmost:
            break

    return hull
    

def jarvisv2(zb):
    
    leftmost = zb[0]
    for point in zb:
        if point[0] < leftmost[0] or (point[0] == leftmost[0] and point[1] < leftmost[1]):
            leftmost = point

    pidx = zb.index(leftmost)
    
    hull = []
    
    p = leftmost
    while True:
        hull.append(p)
        q1 = (pidx + 1) % len(zb)
        q = zb[q1]
        for r in zb:
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val > 0 or (val == 0 and ((r[0] - p[0])**2 + (r[1] - p[1])**2 > (q[0] - p[0])**2 + (q[1] - p[1])**2)):
                q = r
        
        p = q
        
        if p == leftmost:
            break

    return hull
    
         


def main():
    
    zb = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
    
    print(jarvis(zb))
    print(jarvisv2(zb))
    
    

main()