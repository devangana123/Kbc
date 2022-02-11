question_list=[
    ["which is the capital of India ?"],
    ["who is prime minister of India ?"],
    ["which course teach in Navgurukul ?"],
    ["when was Maharashtra established ?"],
    ["which is the cleanest city of India ?"]
]
option=[
    ["Goa","Karnatak","Kerla","New Delhi"],
    ["Ramnath Kovind","Jawaharlal Nehru","Narendra Modi","Atalbihari Vajpei"],
    ["Software Engineering","Agriculture","Science and Technologi","Medical Course"],
    ["1947","1960","1950","1989"],
    ["Indore","jaipur","mumbai","lackhnau"]
]
op50_50=[
    ["1)Goa","4)New Delhi"],
    ["2)Jawaharlal Nehru","3) Narendra Modi"],
    ["1)Softwaere Engineering","3)Science and Technology"],
    ["1947","1960"],
    ["1)lakhnau","2)Indore"]
]
ans_list=[4,3,1,2,1]
print("kon banega karodpati,kbc")
print("lets start the game")
i=0
c=0
s=10000
while i<len(question_list):
    print(question_list[i])
    a=0
    while a<len(option[i]):
        k=option[i][a]
        print(a+1,k)
        a=a+1
    if c==0:
        life_line=input("do you want to use life line")
        if life_line=="yes":
            print(op50_50[i])
            c+=1
            s+=10000
    Ans=int(input("enter your option"))
    if ans_list[i]==Ans:
        print("your answer is correct,you won",s,"rupees")
        s+=10000
    else:
        print("your answer is wrong")
        break
    i=i+1
    

