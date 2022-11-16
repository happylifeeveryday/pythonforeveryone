import random
class rock():
    def __init__(self):
        self.position_x=random.random()
        self.position_y=random.random()
    def eaten():
        #when rock touches paper,rock will be changed to paper.
        return(self.position_x,self.position_y)

class paper():
    def __init__(self):
        self.position_x=random.random()
        self.position_y=random.random()
    def eaten():
        #when paper touches scissors,paper will be changed to scissors.
        return(self.position_x,self.position_y)

class scissors():
    def __init__(self):
        self.position_x=random.random()
        self.position_y=random.random()
    def eaten():
        #when scissors touches rock,scissors will be changed to rock.
        return(self.position_x,self.position_y)
