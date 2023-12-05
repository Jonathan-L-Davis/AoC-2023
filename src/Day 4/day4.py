
def inc_score():
    global round_score
    if round_score == 0:
        round_score = 1
    else:
        round_score *= 2

#45372 - too high
total = 0
total_tickets = 0
initial_tickets = []
ticket_queue = []
round_score = 0
line_no = 1
with open("input.txt") as file:
    for line in file:
        round_score = 0
        game = line.strip().split(":")[1].replace("  "," ")
        score_card , plays = game.split("|")
        game_num = int(  line.strip().split(":")[0][5:8].strip()  )
        
        plays = plays.split(" ")
        score_card = score_card.split(" ")
        initial_tickets.append( list( (game_num,score_card,plays,line_no,1) ) )
        for play in plays:
            if play in score_card and play != '':
                inc_score()
        total += round_score
        line_no += 1
    
    #total_tickets = len(initial_tickets)
    ticket_queue = initial_tickets
    #while len(ticket_queue) > 0:
    for ticket in ticket_queue:
        game_num = ticket[0]
        score_card = ticket[1]
        plays = ticket[2]
        line = ticket[3]
        num = ticket[4]
        score = 0
        for play in plays:
            if play in score_card and play != '':
                score += 1
        print(num)
        
        length = len(initial_tickets)
        if( line < length ):
            for ticket in ticket_queue[line:min(length,line+score)]:
                ticket[4] += 1*num
        
        line_no += 1

for ticket in ticket_queue:
    total_tickets += ticket[4]

print(total)
print(total_tickets)
length = len(initial_tickets)
#print( int((length **2 + length)/2))
