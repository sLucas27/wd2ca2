print("Hello there :)")

def fun(a = 42):
    print("The meaning of life is: " + str(a))
    inp1 = input("What do you think, is the meaning of life?" )
    print("Hmm very interesting, but to quote a famous german philosopher Friedrich Nietzsche, \"Nothing is real, everything is allowed.\"")
    inp2 = input("How would you interpret the quote?" )
    inp3 = input("How would you change your previous perspective on life: \n" + inp1 + "\ngiven Nietzsches quote?" )

def fun2():
    inp1 = input("What does a river and humanity have in common?")
    inp2 = input("Now, if you keep in mind that a river consists of water molecules flowing from a to b and humanity consists of humans living from birth until death, how can it be, that the river continues to flow and humanity continues to live?")
    inp3 = input("This idea of eternity made up of finitude is developed by Goethe in the poem \"Dauer im Wechsel\"")
    
fun()
fun2()