import sys

def assign_blood(donors, rec):
    """Calculate how many people can receive blood"""
    will_receive = 0
    for i in range(len(rec)):
        j = i
        # only compare recipients against compatible donors, ie those with larger indexes
        while j < len(donors) and rec[i] > 0:
            # even is Rh+, odd is Rh-. + cannot donate to -, so skip this combination
            if j % 2 == 0 and i % 2 == 1:
                j += 1
                continue
            # A can't donate to B
            if (j == 4 or j == 5) and (i == 2 or i == 3):
                j += 1
                continue
            if donors[j] >= rec[i]:
                will_receive += rec[i]
                donors[j] -= rec[i]
                rec[i] = 0 
            else:
                will_receive += donors[j]
                rec[i] -= donors[j]
                donors[j] = 0
            j += 1

    return will_receive
            
        

fname = sys.argv[1]
with open(fname) as f:
    # read and reverse list to be in increasing order of compatibility
    donors = list(reversed(list(map(int, f.readline().split(" ")))))
    rec = list(reversed(list(map(int, f.readline().split(" ")))))

    print(assign_blood(donors, rec))

