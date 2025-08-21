import random
uc=int(input("enter your choice:"))
cc=random.randint(0,2)
print(f"computer choice is {cc}")
if uc==cc:
    print("draw")
elif uc==0 and cc==2:
    print("you won")
elif uc==2 and cc==0:
    print("you loss")
elif cc==1:
    if uc<cc:
        print("you loss")
    else:
        print("you won")
elif uc==1:
    if uc>cc:
        print("you won")
    else:
        print("you loss")
else:
    print("invalid")
