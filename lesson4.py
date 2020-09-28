def returnWinner():
    new_file = open("test.txt", "r+")  # 1 Название файла, 2 Метод открытие
    for line in new_file.readlines():
        #print(line[0:5])
        #print(type(new_file.readlines()))
        print(line[-1])
        coomand, score = line.split(" ")
        team, team2 = coomand.split(":")
        goals, goals2 = score.split(":")

        if int(goals) == int(goals2):
            print(f"Draw beetwen : {team} and {team2}.")
        elif int(goals) > int(goals2):
            print(f"Winner is: {team}!")
        else:
            print(f"Winner is: {team2}!")
        print("\n")
        new_file.close()

def add_score():
    newFile = open("test.txt","a")
    score = input("Enter commands and their score")
    newFile.write("\n"+score)
    newFile.close()

def main():
    while True:
        print("Choose options")
        print("1) Add new score")
        print("2) List all scores and their winners")
        print("3) Stop programm")

        choice = int(input("Enter your choice:"))

        if choice == 1:
            add_score()
        elif choice == 2:
            returnWinner()
        elif choice ==3:
            break
        else:
            print("Error no such choice")

main()

#add_score()
#returnWinner()
#new_file.write("\nAbdysh_ata:Dynamo-RF 1000:0")
