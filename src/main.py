print("Hello there :)")

def fun(a = 42):
    print("The meaning of life is: " + str(a))
    inp1 = input("What do you think, is the meaning of life?" )
    print("Hmm very interesting, but to quote a famous german philosopher Friedrich Nietzsche, \"Nothing is real, everything is allowed.\"")
    inp2 = input("How would you interpret the quote?" )
    inp3 = input("How would you change your previous perspective on life: \n" + inp1 + "\ngiven Nietzsches quote?" )
    
fun()