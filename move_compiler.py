moves = open('moves.csv', 'r').read().split('\n')
out = open('movesNEW.csv','w')
out.write(moves[0]+'\n')

for each in moves[1:]:
    out.write(','.join(each.split(',')[:-3])+'\n')

out.close()
