name = ""
score = 0
count = 0
Que_list = [{
    "Question": "1) 2+3",
    "A": 5,
    "B": 2,
    "C": 4,
    "D": 40,
    "ans": "A"
},
    {
        "Question": "2) 2+9",
        "A": 5,
        "B": 2,
        "C": 11,
        "D": 40,
        "ans": "C"
    }
]


def getData():
    print("Welcome To KBC")
    global name
    name = input("enter name: ")


def display(lst):
    global score
    global count
    for i in lst:
        print("\n", i["Question"])
        print("(A)", i["A"], "\t",
              "(B)", i["B"], "\t",
              "(C)", i["C"], "\t",
              "(D)", i["D"])
        ans = input("Enter yr ans: ")
        if ans.upper() == i["ans"]:
            score = score + 1
        print("Now yr score is: ", score)
        count = count + 1
        if (count == len(Que_list)):
            print("Now yr game is over...")

        print("-----------------------------------------------")


def main():
    global Que_list
    getData()
    display(Que_list)


main()

