'''
In this Kata we will play a classic game of Tug-o'-War!

Two teams of 5 members will face off, the strongest of which will prevail. 
Each team member will be assigned a strength rating (1-9), with the most powerful 
members having a rating of 9. Your goal is to determine, based on the cumulative strength of 
the members of each team, which team will win the war.

The teams will be represented by an array of arrays:

Javascript/Python

[[5,0,3,2,1], [1,6,8,2,9]]  // 11 &lt; 26 ; "Team 2 wins!"

If team one is stronger, return the string "Team 1 wins!" If team two is stronger, return the 
string "Team 2 wins!"

If the two teams are of equal strength, the team with the strongest Anchor (the member furthest f
	rom the center of the rope) will win. In the above example, the member with strength 5 
is team one's Anchor and strength 9 is team two's Anchor. If the teams and the Anchors are 
both of equal strength, return the string "It's a tie!"

more examples:

Javascript/Python

[[1,2,3,4,5], [1,2,3,4,5]] // Team 2 has stronger Anchor ; "Team 2 wins!"
[[1,2,3,4,5], [5,4,3,2,1]] // Teams &amp; Anchors are tied; "It's a tie!"
'''
def tug_o_war(teams):
	if sum(teams[0]) > sum(teams[1]):
		return "Team 1 wins!"
	elif sum(teams[0]) < sum(teams[1]):
		return "Team 2 wins!"
	else:
		if teams[0][0] > teams[1][-1]:
			return "Team 1 wins!"
		elif teams[0][-1] < teams[1][-1]:
			return "Team 2 wins!"
		else:
			return "It's a tie!"


print tug_o_war( [[1,2,3,4,5], [1,2,3,4,5]] )
print tug_o_war( [[1,2,3,4,5], [5,4,3,2,1]] )

'''
def tug_o_war(teams):
    (a, b) = (sum(team) for team in teams)
    if a == b:
        a = teams[0][0]
        b = teams[1][-1]
    return "Team 1 wins!" if a > b else "Team 2 wins!" if a < b else "It's a tie!"
'''