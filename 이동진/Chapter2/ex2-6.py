colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirts in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirts)
