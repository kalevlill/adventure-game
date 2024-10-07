
def greeting():
    print("Welcome to the lost treasure hunt")
    print("The rules are simple - solve the riddle, to advance into the next room")


def main():
    greeting()
    rooms = [
    {
                "name":"Entrance hall",
                "description":"You enter the entrance hall",
                "description":"A dark room with old paintings on the walls. ",
                "riddle":{
                    "Question":"It has keys, but no locks. It has space, but no room. You can enter, but can’t go inside. What is it?",
                    "Answer":"A keyboard"
                }
    },
    {
                "name":"Library",
                "description":"",
                "riddle":{
                    "Question":"What can you hold in your right hand, but never in your left hand?",
                    "Answer":"Your left hand"
                } 
    },
    {
                "name":"Dining room",
                "description":"",
                "riddle":{
                    "Question":"Ask this question all day long, but always get completely different answers, and yet all the answers will be correct. What is the question?",
                    "Answer":"What time is it?"
                }
    }
  ]

    currentroom = 0
    print(rooms)
    print(rooms[0])
    print(rooms[0]['riddle'])

main()