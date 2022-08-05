def lr():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    lr()
    move()
    lr()   
    move()
    turn_left()
for step in range(6):
    jump()
