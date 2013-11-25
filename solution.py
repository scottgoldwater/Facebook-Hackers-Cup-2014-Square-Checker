__author__ = 'Scott Goldwater'
def checkSquare(rowCount, file):
    plain = 0
    preplain = -1
    hash = 0
    hashrow = 0
    ishash = False
    started = False
    finished = False
    answer = None
    hashdone = False

    for x in range(0, rowCount):
        line = file.readline()
        preplain = plain
        plain = 0
        ishash = False
        hashdone = False
        if not started:
            preplain = -1
        for y in range(0, rowCount):
            if line[y] == '#':
                if hashdone:
                    answer = False
                ishash = True
                if not started:
                    started = True
                if finished:
                    answer = False
                hash += 1
                continue
            if not ishash:
                plain += 1
            else:
                hashdone = True
            if (plain == rowCount) & started:
                finished = True
        if started:
            if ishash:
                hashrow += 1
            if not finished:
                if plain != preplain | preplain != -1:
                    answer= False
    if(answer != None):
        return answer
    if hashrow == 0:
        return False
    if hash/hashrow == hashrow:
        return True
    return False

input = open("sampleinput.txt")
output = open("output.txt", 'w')
number = input.readline()
number = int(number)

for i in range(0,number):
    print "Case #{}:".format(i+1),
    case = input.readline()
    case = int(case)
    boolean =  checkSquare(case,input)
    if(boolean):
        print "YES"
    else:
        print "NO"




