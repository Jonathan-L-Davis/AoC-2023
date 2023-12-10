


class seed_map_entry:
    
    src_start = 0
    dst_start = 0
    range_length = 0
    
    
    def __init__(self,dstart,sstart,rangfjalkg):
        self.src_start = sstart
        self.dst_start = dstart
        self.range_length = rangfjalkg
    
    

def map_seeds( seeds,almanac ):
    
    retMe = []
    for seed in seeds:
        is_in_almanac = False
        for almond in almanac:
            dst_start = int(almond.dst_start)
            src_start = int(almond.src_start)
            range_length = int(almond.range_length)
            map_dist = dst_start-src_start
            if( (seed >= src_start) and (seed < src_start + range_length) ):
                retMe.append( seed + map_dist )
                is_in_almanac = True
        if not is_in_almanac:
            retMe.append(seed)
    
    return retMe
    
seeds = []
s2s = []
s2f = []
f2w = []
w2l = []
l2t = []
t2h = []
h2l = []
total = 0
total2 = 0
state = 0
with open("input.txt") as file:
    first_line = file.readline().split()
    seeds = ( first_line[1:len(first_line)] )
    for idx,seed in enumerate(seeds):
        seeds[idx] = int(seed)
    #print(seeds)
    
    for line in file:
        #print(line)
        
        if (line.find("seed-to-soil map:")!=-1) or (state == 1):
            state = 1
            if line.find("soil-to-fertilizer map:") != -1:
                state = 2
                continue
            if (line.find("seed-to-soil map:")==-1) and (len(line.split())==3) :
                tmp = line.split()
                s2s.append( seed_map_entry( tmp[0], tmp[1], tmp[2] ) )
        
        if line == "soil-to-fertilizer map:" or (state == 2):
            state = 2
            if line.find("fertilizer-to-water map:") != -1:
                state = 3
                continue
            if (line.find("soil-to-fertilizer map:")==-1) and (len(line.split())==3) :
                tmp = line.split()
                s2f.append( seed_map_entry( tmp[0], tmp[1], tmp[2] ) )
            
        if line == "fertilizer-to-water map:" or (state == 3):
            state = 3
            if line.find("water-to-light map:") != -1:
                state = 4
                continue
            if (line.find("fertilizer-to-water map:")==-1) and (len(line.split())==3) :
                tmp = line.split()
                f2w.append( seed_map_entry( tmp[0], tmp[1], tmp[2] ) )
            
        if line == "water-to-light map:" or (state == 4):
            state = 4
            if line.find("light-to-temperature map:") != -1:
                state = 5
                continue
            if (line.find("water-to-light map:")==-1) and (len(line.split())==3) :
                tmp = line.split()
                w2l.append( seed_map_entry( tmp[0], tmp[1], tmp[2] ) )
            
        if line == "light-to-temperature map:" or (state == 5):
            state = 5
            if line.find("temperature-to-humidity map:") != -1:
                state = 6
                continue
            if (line.find("seed-to-soil map:")==-1) and (len(line.split())==3) :
                tmp = line.split()
                l2t.append( seed_map_entry( tmp[0], tmp[1], tmp[2] ) )
            
        if line == "temperature-to-humidity map:" or (state == 6):
            state = 6
            if line.find("humidity-to-location map:") != -1:
                state = 7
                continue
            if (line.find("seed-to-soil map:")==-1) and (len(line.split())==3) :
                tmp = line.split()
                t2h.append( seed_map_entry( tmp[0], tmp[1], tmp[2] ) )
            
        if line == "humidity-to-location map:" or (state == 7):
            state = 7
            if line.strip() == -1:
                state = 0
                continue
            if (line.find("seed-to-soil map:")==-1) and (len(line.split())==3) :
                tmp = line.split()
                h2l.append( seed_map_entry( tmp[0], tmp[1], tmp[2] ) )
            
        


#print( len(s2s) )
#print( len(s2f) )
#print( len(f2w) )
#print( len(w2l) )
#print( len(l2t) )
#print( len(t2h) )
#print( len(h2l) )

soil = map_seeds(seeds,s2s)
fertilizer = map_seeds(soil,s2f)
water = map_seeds(fertilizer,f2w)
light = map_seeds(water,w2l)
temp = map_seeds(light,l2t)
humid = map_seeds(temp,t2h)
loc = map_seeds(humid,h2l)

#print(seeds)
#print(soil)
#print(fertilizer)
#print(water)
#print(light)
#print(temp)
#print(humid)
#print(loc)

total = min(loc)

print(total)
print(total2)
