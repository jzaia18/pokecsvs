alldata = open('alldata.csv','w')

pokemain  = open('pokemon.csv','r').read().split('\n')

##print pokemain[0]
##print pokestats[0]
##print poketypes[0]
##
##print poketypes[1:5]
##
##print len(pokemain), len(pokestats), len(poketypes)
##print pokemain[810]

#pokestats = open('pokemon_stats.csv','r').read().split('\n') #has been replaced
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


#poketypes = open('pokemon_types.csv','r').read().split('\n') #has been replaced
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


#pokeevos = open('pokemon_species.csv','r').read().split('\n')
##STEP THREE: evolutions
##out = open('pokemon_speciesNEW.csv','w')
##
##for i in xrange(len(pokeevos)):
##    pokeevos[i] = pokeevos[i].split(',')
##pokeevos.pop()
##
##for each in pokeevos:
##    if not each[3]:
##        each[3]=0
##    out.write('%s,%s,%s\n'%(each[0],each[3],each[4]))
##
##out.close()
pokeevos = open('pokemon_speciesNEW.csv','r').read().split('\n')

learnset  = open('pokemon_moves.csv','r').read().split('\n')
##STEP FOUR: learnset
for i in xrange(len(learnset)):
    learnset[i] = learnset[i].split(',')
learnset.pop()
print learnset.pop(0)

out = open('pokemon_movesNEW.csv', 'w')
out.write('pokemon_id,move_id\n')
i = 0
curr_num = 1
curr_str = ''
god_damn_this = ['']
while i < len(learnset):
    if int(learnset[i][1]) != 18:
        i+=1
        continue
    if int(learnset[i][0]) != curr_num:
        if 0 < int(pokeevos[curr_num].split(',')[1]) < len(god_damn_this):#add prevolution moves
            #print pokeevos[curr_num].split(',')
            #print curr_str
            curr_str = curr_str + god_damn_this[int(pokeevos[curr_num].split(',')[1])]
        #print '%s, "%s"\n'%(curr_num, curr_str[1:])

        ## REMOVE DUPLICATES
        curr_str = list(set(curr_str[1:].split(';')))
        curr_str.sort()
        curr_str = ';'.join(curr_str)
            
        out.write('%s,"%s"\n'%(curr_num, curr_str))
        curr_num+=1
        god_damn_this.append(';'+curr_str)
        curr_str=''
    else:
        if not ';' + learnset[i][2] in curr_str:
            to_add = learnset[i][2]
            while len(to_add) < 3:
                to_add = '0' + to_add
            curr_str += ';' + to_add
    i+=1
    if curr_num > 721:
        break

out.close()
learnset  = open('pokemon_movesNEW.csv','r').read().split('\n')


##STEP FOUR: compile all data
#print len(pokemain), len(pokestats), len(poketypes)
#limit data in pokemain
pokemain = pokemain[0:722]

print 'Main:        ', pokemain[0]
print 'Stats:       ', pokestats[0]
print 'Types:       ', poketypes[0]
print 'Evolutions:  ', pokeevos[0]
print 'Learnsets:   ', learnset[0]


for i in xrange(len(pokemain)):
    pokemain[i] = pokemain[i].split(',')

for i in xrange(len(poketypes)):
    poketypes[i] = poketypes[i].split(',')
poketypes.pop()

for i in xrange(len(pokestats)):
    pokestats[i] = pokestats[i].split(',')
pokestats.pop()

for i in xrange(len(pokeevos)):
    pokeevos[i] = pokeevos[i].split(',')
pokeevos.pop()

for i in xrange(len(learnset)):
    x = learnset[i].split(',')[0]
    learnset[i] = learnset[i][len(x)+1:]
learnset.pop()

for i in xrange(len(pokemain)):
    alldata.write('%s,%s,'%(pokemain[i][0],pokemain[i][1]))
    alldata.write('%s,%s,'%(poketypes[i][1],poketypes[i][2]))
    alldata.write('%s,%s,%s,%s,%s,%s,'%(pokestats[i][1], pokestats[i][2], pokestats[i][3], pokestats[i][4], pokestats[i][5], pokestats[i][6]))
    alldata.write('%s,%s,'%(pokeevos[i][1], pokeevos[i][2]))
    alldata.write('%s\n'%(learnset[i]))

alldata.close()

print "DONE!"
