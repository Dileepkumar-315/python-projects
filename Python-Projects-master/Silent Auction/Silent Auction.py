import os
def find_winner(bidder):
    high=0
    winner=""
    for i in bidder:
        bidding_price=bidder[i]
        if bidding_price>high:
            high=bidding_price
            winner=i
    print(f"the winner is {winner} with a bid of {high}")
print("**** welcome to the silent auction program****")
dict={}
end_of_bidding=False
while not end_of_bidding:
    name=input("what is your name?:")
    bid=int(input("what is your bid?:"))
    n=input("are there any other bidders? type 'yes' or 'no':").lower()
    dict[name]=bid
    if n=='no':
        end_of_bidding=True
        find_winner(dict)
    elif n=='yes':
        os.system('cls')
