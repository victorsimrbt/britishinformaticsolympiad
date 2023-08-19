'''
achievable: {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}


'''
achievable = set()
ans = 0
for jug1 in range(1,20):
    for jug2 in range(jug1+1,20):
        # print(jug1,jug2)
        achievable = set()
        for i in range(1,21):
            j,n = 3,i
            # print(j,n)
            root = [[20,0],[jug1,0],[jug2,0]]

            def twodcopy(lst):
                return [sublst[:] for sublst in lst]

            def serialize(state):
                string = ''
                for jug in state:
                    string += str(jug[0]) + str(jug[1]) + ' '
                return string
                
            def pour(jugs,idx1,idx2):
                # ! pour from jug1 to jug2
                jugs = twodcopy(jugs)
                capacity1,volume1 = jugs[idx1]
                capacity2,volume2 = jugs[idx2]
                
                # ! move all water from jug1 to jug2
                # if volume1 > (capacity2-volume2):
                    
                pour_volume = min(capacity2-volume2,volume1)
                
                jugs[idx1][1] -= pour_volume
                jugs[idx2][1] += pour_volume
                return jugs

            def empty(jugs,idx):
                jugs = twodcopy(jugs)
                jugs[idx][1] = 0
                # capacity,volume = jug
                return jugs

            def fill(jugs,idx):
                jugs = twodcopy(jugs)
                jugs[idx][1] = jugs[idx][0]
                return jugs

            dist = {}
            def generate_neighbors(jugs,distance):
                states = []
                jugs = twodcopy(jugs)
                for i in range(len(jugs)):
                    states.append(empty(jugs,i))
                    states.append(fill(jugs,i))
                
                for jug1 in range(len(jugs)):
                    for jug2 in range(len(jugs)):
                        if jug1 != jug2 and jugs[jug1] != 0:
                            # print(pour(jugs,jug1,jug2),jug1,jug2)
                            states.append(pour(jugs,jug1,jug2))
                
                neighbors = []
                for state in states:
                    # print(serialize(state))
                    for jug in state:
                        if jug[1] == n:
                            achievable.add(n)
                            # print(distance + 1)
                            # exit()
                    if serialize(state) in dist:
                        pass
                    else:
                        dist[serialize(state)] = distance + 1
                        neighbors.append(state)
                return neighbors

            queue = []
            queue = [root]

            # print(root)
            head = 0 
            dist[serialize(root)] = 0

            while head < len(queue):
                last = queue[head]
                queue += generate_neighbors(last,dist[serialize(last)])
                head += 1
            
        # print(achievable)
        if achievable == set({2, 4, 6, 8, 10, 12, 14, 16, 18, 20}):
            # print(achievable)
            print(20,jug1,jug2)
            ans += 1


            # print(generate_neighbors([[3,0],[3,1]]))
print(achievable)
print(ans)
            
                
            
        