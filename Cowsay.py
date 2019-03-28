import time
from random import randint

Messages = ["You can do it!", "Stay positive", "You're aMOOsing",
            "Construct aditional pylons", "Oink... I mean... moo",
            "Keep going!", "I'm a cow!", "Much wow!",
            "I need better messages", "Hi Jason!"]
message = " "

a = " " + ("_" * (len(message) + 1))
b = "< " +  message + " >"
c = " " + ("-" * (len(message) + 1))
d = "     \  ^__^"
e = "      \ (oo)\________"
f = "        (__)\        )\/\ "
g = "         U   ||----w |"
h = "             ||     ||"

while True:
    message = Messages[randint(0, len(Messages)) - 1]
    a = " " + ("_" * (len(message) + 1))
    b = "< " +  message + " >"
    c = " " + ("-" * (len(message) + 1))
    print (a)
    print (b)
    print (c)
    print (d)
    print (e)
    print (f)
    print (g)
    print (h)
    time.sleep(3)
