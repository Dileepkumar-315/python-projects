import random
data=[
    {
        'name':'K.L.Rahul',
        'follower_count':200,   #follower_count is in millions
        'description':'crickter',
        'country':'india'
    },
    {
        'name':'cristiano ronaldo',
        'follower_count':600,
        'description':'football player',
        'country':'portugal'
    },
    {
        'name':'narendra modi',
        'follower_count':100,
        'description':'prime minister',
        'country':'india'
    },
    {
        'name':'fit tuber',
        'follower_count':7,
        'description':'youtuber',
        'country':'india'
    },
    {
        'name':'selena gomez',
        'follower_count':420,
        'description':'musician and actress',
        'country':'united states'
    },
    {
        'name':'kylie jenner',
        'follower_count':400,
        'description':'reality tv personality',
        'country':'united states'
    },
    {
        'name':'pankaj tripathi',
        'follower_count':5,
        'description':'actor',
        'country':'india'
    },
    {
        'name':'leo messi',
        'follower_count':480,
        'description':'football player',
        'country':'argentina'
    },
    {
        'name':'beyonce',
        'follower_count':315,
        'description':'musician',
        'country':'united states'
    },
    {
        'name':'t-series',
        'follower_count':245,
        'description':'music studio',
        'country':'india'
    },
    {
        'name':'neeraj chopra',
        'follower_count':6,
        'description':'athlete',
        'country':'india'
    },
    {
        'name':'justin bieber',
        'follower_count':293,
        'description':'musician',
        'country':'canada'
    },
    {
        'name':'taylor swift',
        'follower_count':267,
        'description':'musician',
        'country':'united states'
    },
    {
        'name':'jennifer lopez',
        'follower_count':249,
        'description':'actress',
        'country':'united states'
    },
    {
        'name':'shakira',
        'follower_count':87,
        'description':'musician',
        'country':'colombia'
    },
    {
        'name':'nasa',
        'follower_count':94,
        'description':'space agency',
        'country':'united states'
    },
    {
        'name':'isro',
        'follower_count':1,
        'description':'space agency',
        'country':'india'
    }
]
score=0
d1=random.choice(data)
flag=True
while flag:
    d2=random.choice(data)
    print(f"compare1: {d1['name']},{d1['description']},from{d1['country']}")
    print("VS")
    print(f"compare2: {d2['name']},{d2['description']},from{d2['country']}")
    n=int(input("who has more followers?Type '1' or '2':"))
    if n==1:
        if d1['follower_count']>d2['follower_count']:
            score=score+1
            print(f"you are right,your score is {score}.")
            d1=d1
        else:
            print(f"you are wrong..your final score is {score}.")
            exit()
    else:
        if d1['follower_count'] < d2['follower_count']:
            score=score+1
            print(f"you are right,your score is {score}.")
            d1=d2
        else:
            print(f"you are wrong..your final score is {score}.")
            exit()
