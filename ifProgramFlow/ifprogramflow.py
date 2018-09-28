_author_ = 'shail'

name = input("Please provide your name :")
age = int(input("Please provide your age, {0} :".format(name)))

if age >= 18:
    print("You are old enough to vote {0}".format(name))
    print("Please put X in the ballot box")
else:
    print("Please come back after {0} years".format(18 - age))

