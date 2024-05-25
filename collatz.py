
def collatz():
    storeNos = []
    try:
        collatz = int(input("Input a number you want to know its collatz steps : "))

        print("----Starting Collatz sequence---")


        while True:
            if collatz == 1:
                break
            elif collatz % 2 == 1:
                collatz = (collatz*3) +1
                storeNos.append(collatz)
                
            elif collatz % 2 == 0:
                collatz = collatz/2
                storeNos.append(collatz)
                
            else:
                print("Invalid Input")


        for storeNo in storeNos:
            print(f"{storeNo}")

        print('---done---')
        print(f"The number of steps is {len(storeNos)}")
            # i=1
            # if i <= len(storeNos):
            #     print(f"Step {i} : {storeNo}")
            #     i +=1
            
    except ValueError:
        print("Error!!! Invalid Entry Try again")


        


collatz()

