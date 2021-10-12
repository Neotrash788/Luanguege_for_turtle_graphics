import turtle

#Declare nessecary vars
functions = []
t = turtle.Turtle()
codePos = 0

# read code and split into lines
with open('shape.shape', 'r') as f:
    code = []
    for i in f.readlines():
        code.append(i.strip('\n'))


def updateSr(sr):
    if sr == '0':
        turtle.tracer(0,0)

def updatePen(pen):
    if pen == 'U':
        t.penup()
    elif pen == 'D':
        t.pendown()

def setSpeed(speed):
    t.speed(int(speed))

def setSize(Size):
    global size
    size = int(Size)

def up():
    t.left(90)
    t.forward(size)
    t.right(90)

def down():
    t.right(90)
    t.forward(size)
    t.left(90)

def left():
    t.right(180)
    t.forward(size)
    t.left(180)

def right():
    t.forward(size)

def move(line):
    #intepret move > 1 commands (M R3)
    movement = []
    for i in range(1,len(line)):
        if len(line[i])>1:
            movement.append(line[i][0]*int(line[i][1:])) 
        else:
            movement.append(line[i])
    movement = list(''.join(movement))

    #Move based on movement arr
    for i in movement:
        if i == 'U':
            up()
        if i == 'D':
            down()
        if i == 'L':
            left()
        if i == 'R':
            right()

def find_in_list_of_list(mylist, char):
    for sub_list in mylist:
        if char in sub_list:
            return (mylist.index(sub_list), sub_list.index(char))
    raise ValueError("'{char}' is not in list".format(char = char))

def readFunc(func):
    #Look up function and data
    print(func)
    print(func[1])
    currentFunction = functions[find_in_list_of_list(functions, func[1])[0]]
    print(f'-----------')
    print(currentFunction)
    print(f'-----------')
    #Run commands in function
    for command in currentFunction:
        print(command)
        readLine(command.split(' '))

def createFunc(i):
    newFunc = []
    fName = ' '.join(line[1:line.index('[')])
    newFunc.append(fName)
    i += 1
    while code[i] != ']':
        newFunc.append(code[i])
        i +=1
    functions.append(newFunc)
    print(f'CURRENT FUNCTIONS ->{functions}')
    return i

def goto(line):
    x = int(line[1])
    y = int(line[2])
    t.goto(x,y)

def readLine(line):
    global codePos
    if line[0] == 'GOTO':
        goto(line)

    if line[0] == 'SR': #
        updateSr(line[1])
        print(line)

    if line[0] == 'P':
        updatePen(line[1])

    if line[0] == 'M':
        move(line)

    if line[0] == 'CF':
        codePos = createFunc(codePos)

    if line[0] == 'SS':
        setSize(int(line[1]))
    
    if line[0] == 'SSP':
        setSpeed(line[1])
    
    if line[0] == 'F':
        try:
            readFunc(line.split(' '))
        except Exception:
            readFunc(line)
    
    turtle.update()

#Main Loop
while codePos < len(code):
    line = code[codePos].split(' ')
    readLine(line)
    print(f'Current Line is {line}')
    codePos += 1

input('END ->')
