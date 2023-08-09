from itertools import permutations
class Point:
	def __init__(self, straight, left, right):
		self.straight = straight	# this never changes
		self.curved = [left, right]	# this never changes
		self.is_flipflop = False	# this also never changes
		self.left_right = 0	# 0-left, 1-right. initially points to left
	def enter(self, from_pt):
		if from_pt in self.curved:
			if not self.is_flipflop:
				self.left_right = self.curved.index(from_pt)
			return self.straight
		if from_pt == self.straight:
			exit_point = self.curved[self.left_right]
			if self.is_flipflop:
				self.left_right = 1 - self.left_right
			return exit_point
		return None
			# def __str__(self):
	#     return self.char

connections = ['ADEF', 'BCGH', 'CBIJ', "DAKL","EAMN","FANO","GBOP","HBPQ","ICQR","JCRS","KDST","LDTM","MULE","NUEF","OVFG","PVGH","QWHI","RWIJ","SXJK","TXKL","UVMN","VUOP","WXQR","XWST"]

def test(pos1, pos2):
	network = {code[0]: Point(code[1], code[2], code[3]) for code in connections}
	for _ in range(72):
		if pos2[1] == pos1[1]:	# !!!! sensei: check that before calling enter instead of after
			return False
		if set(pos2) == set(pos1):
			return False
		next1 = network[pos1[1]].enter(pos1[0])
		next2 = network[pos2[1]].enter(pos2[0])
		pos1 = pos1[1] + next1
		pos2 = pos2[1] + next2
		# print(pos1, pos2)
	return True

count = 0
all_pos = []
for pt in connections:
	all_pos.append(pt[0] + pt[1])
	all_pos.append(pt[0] + pt[2])
	all_pos.append(pt[0] + pt[3])
print(list(permutations(all_pos, 2)))
exit()
for red, blue in permutations(all_pos, 2):
    print(red,blue)
    if test(red, blue):
        count += 1
print(count)