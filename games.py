guess_count = 1 
guess_limit = 3
secret_number = 9

while guess_count <= guess_limit : 
     guess = int(input("guess: "))
     guess_count = guess_count + 1
     if guess == secret_number:
        print("you won")
        break
else:
    print("sorry, you failed")        