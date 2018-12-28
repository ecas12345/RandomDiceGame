def multi_roll(rolls, sides):
	import random
	a = 0
	total = 0
	working = 0

	while a < rolls:
		a += 1
		working = random.randint(1, sides)
		total += working
		print("Roll #", a, ": ", working)
	print("Total is: ", total)

def main():
        answer = 'y'
        rolls = int(input("How many rolls?"))
        sides = int(input("Enter the dice that you want to roll: "))
        multi_roll(rolls, sides)
        while answer == 'y':
            answer = input("Roll again? (y/n):")
            if answer == 'y':
                print("y")
                main()
            elif answer == 'n': 
                print("Goodbye")
                break
            else:
                answer = 'y'
                print("You need to enter either a N or a Y")
                
if __name__ == '__main__':
    main()