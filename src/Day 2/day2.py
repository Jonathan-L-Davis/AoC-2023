total = 0

line_num = 0
possible = True
red = 0
green = 0
blue = 0
max_red = 12
max_green = 13
max_blue = 14
colors = ["red","green","blue"]

with open("input.txt") as file:
    for line in file:
        red = 0
        green = 0
        blue = 0
        line = line.strip("Game ")
        line_num, line = line.split(":")
        line = line.strip()
        game = line.split(";")
        possible = True
        for rounds in game:
            cubes = rounds.strip().split(", ")
            print (cubes)
            for cube in cubes:
                if ( cube.find("red" )!= -1 ):
                    red = max(int(cube.split(" ")[0]),red)
                if ( cube.find("green" )!= -1 ):
                    green = max(int(cube.split(" ")[0]),green)
                    print(green)
                if ( cube.find("blue" )!= -1 ):
                    blue = max(int(cube.split(" ")[0]),blue)
        print( str(red) + " " + str(green) + " " + str(blue) )
            #if( int(red) > max_red or int(green) > max_green or int(blue) > max_blue ):
            #    possible = False
        
        #if possible:
        total += int(red*green*blue)
        
print(total)
