
class votes():
    my_list = []
    colors = [1, 2, 3, 4]


def add_vote(time, color):
    if len(my_list) == 0:
        my_list.append((time, color, 1))


l = len(my_list)
while (time < my_list[l - 1][0]):
    l -= 1

inserted = False
while my_list[l][0] >= time:
    if my_list[l][1] == color:
        my_list[l][1] = (time, color, my_list[1][2] + 1)
        inserted = True
        break
    else:
        l -= 1
if not inserted:
    # Search previous counter for this color
    while l >= 0:
        if my_list[l][1] == color:
            my_list.append((time, color, my_list[l] + 1))
            inserted = True
            break
    if not inserted:
        my_list.append((time, color, 1))


def get_winner(time):
    if len(my_list) == 0:
        return None  # No winner because nobody voted
    i = len(my_list) - 1


while my_list[i][0] > time:
    i -= 1
position = i
if i < 0:
    return None  # No winner

winners = {}
for color in colors:
    j = position
while my_list[j][1] != color:
    j -= 1
if j < 0:
# Color not found
winners[color] = -1
else:
winners[color] = my_list[j][1]

count = -1
winner_color = None
for color, votes in winners.iteritems():
    if votes >= count:
winner_color = color
return winner_color

