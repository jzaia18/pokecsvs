alldata = open('alldata.csv','w')

pokemain  = open('pokemon.csv','r').read().split('\n')
pokestats = open('pokemon_stats.csv','r')#.read().split('\n') #has been replaced
poketypes = open('pokemon_types.csv','r')#.read().split('\n') #has been replaced
learnset  = open('pokemon_moves.csv','r').read().split('\n')

##print pokemain[0]
##print pokestats[0]
##print poketypes[0]
##
##print poketypes[1:5]
##
##print len(pokemain), len(pokestats), len(poketypes)
##print pokemain[810]

#### STEP ONE: fix types
##for i in xrange(len(poketypes)):
##    poketypes[i] = poketypes[i].split(',')
##poketypes.pop()
##poketypes.pop(0)
##
##out = open('pokemon_typesNEW.csv','w')
##out.write('pokemon_id, type1_id, type2_id\n')
##
##j = 1
##i = 0
##while i < len(poketypes):
##    #print poketypes[i], poketypes[i+1]
##    if int(poketypes[i+1][0])==j:
##        out.write('%s, %s, %s\n'%(j, poketypes[i][1], poketypes[i+1][1]))
##        i+=1
##    else:
##        out.write('%s, %s, %s\n'%(j, poketypes[i][1], 0))
##    if j==721:
##        break
##    j+=1
##    i+=1
##
##out.close()
poketypes = open('pokemon_typesNEW.csv','r').read().split('\n')

## STEP TWO: fix stats
##out = open('pokemon_statsNEW.csv','w')
##out.write('pokemon_id, hp, attack, defense, spatk, spdef, speed\n')
##
##for i in xrange(len(pokestats)):
##    pokestats[i] = pokestats[i].split(',')
##pokestats.pop()
##pokestats.pop(0)
##
##ps = pokestats
##i = 0
##while i < len(ps):
####    for j in range(5):
####        print ps[i+j]
##    #print ps[i:i+6]
##    out.write('%s, %s, %s, %s, %s, %s, %s\n'%(ps[i][0], ps[i][2], ps[i+1][2], ps[i+2][2], ps[i+3][2], ps[i+4][2], ps[i+5][2]))
##    i+=6
##    if i/6 >= 721:
##        break
##
##out.close()
pokestats = open('pokemon_statsNEW.csv','r').read().split('\n')

##STEP THREE: learnset
for i in xrange(len(learnset)):
    learnset[i] = learnset[i].split(',')
learnset.pop()
print learnset.pop(0)

out = open('pokemon_movesNEW.csv', 'w')
out.write('pokemon_id, move_id\n')
i = 0
curr_num = 1
curr_str = ''
while i < len(learnset):
    if int(learnset[i][1]) != 18:
        i+=1
        continue
    if int(learnset[i][0]) != curr_num:
        #print '%s, "%s"\n'%(curr_num, curr_str[1:])
        out.write('%s, "%s"\n'%(curr_num, curr_str[1:]))
        curr_num+=1
        curr_str=''
    else:
        curr_str += ',' + learnset[i][2]
    i+=1
    if curr_num > 721:
        break

out.close()


##STEP FOUR: compile all data
#print len(pokemain), len(pokestats), len(poketypes)
#limit data in pokemain
pokemain = pokemain[0:722]

print pokemain[0]
print pokestats[0]
print poketypes[0]


for i in xrange(len(pokemain)):
    pokemain[i] = pokemain[i].split(',')

for i in xrange(len(poketypes)):
    poketypes[i] = poketypes[i].split(',')
poketypes.pop()

for i in xrange(len(pokestats)):
    pokestats[i] = pokestats[i].split(',')
pokestats.pop()

for i in xrange(len(pokemain)):
    alldata.write('%s, %s, '%(pokemain[i][0],pokemain[i][1]))
    alldata.write('%s, %s, '%(poketypes[i][1],poketypes[i][2]))
    alldata.write('%s, %s, %s, %s, %s, %s\n'%(pokestats[i][1], pokestats[i][2], pokestats[i][3], pokestats[i][4], pokestats[i][5], pokestats[i][6]))

alldata.close()
