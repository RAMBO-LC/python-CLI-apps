import os
import termgraph
from colorama import Fore, Style
import subprocess
from datetime import date
import json

today = str(date.today())



sessions = [
    {
        "topic": "PYTHON",
        "time": 2.0,
        "done": 100,
        "difficulty": "Hard"
    }
]

def load_DB():
    try:
        with open("DB.json", "r") as f:
            data = json.load(f)
    except Exception as e:
        print(e) 
def save_DB(data):
    try:
        with open("DB.json", "w") as f:
            json.dump(data,f, intent=4)
    except Exception as e:
        print(e) 

    



def add_Session():
    total_sub=int(input("How many subjects did you studied today?: "))
    
    print("-----------------------") 
    
    for i in range(total_sub): 
        topic = input(f"Topic No.{i+1}: ").upper()
        while True:
            try: 
                time = float(input("Study Time(hrs): "))
                break
            except ValueError:
                print("Please enter a valid number for hours")
        done=input("Done?(y/n): ").lower()
        if done == "y":
            done=100
        if done=="n":
            how_much=int(input("How much completed (%) ?: "))    
            done = 100 - how_much   

        diff = input("Difficulty level? (1-5): ").lower().strip()

        diff_level={"1":"easy", "2":"medium", "3":"hard", "4":"very hard", "5":"Extreme"}

        diff = diff_level.get(diff,"Unknown")
        sessions.append({"topic":topic, "time":time, "done":done, "difficulty":diff})
        print("\nSession added!")
        
        continue


def view_sessions():
    if not sessions:
        print("No study sessions found.")
        return
    print("======== STUDY SESSIONS ========")
    for i, session in enumerate(sessions, start=1):
        print(f"{i}. {session['topic']}")
        print(f"   Time: {session['time']} hrs")
        print(f"   Done: {session['done']}%")
        print(f"   Difficulty: {session['difficulty']}")
        print()    



def view_stats():
    if not sessions:
        print(Fore.RED + "No study sessions found.")
        return

    topics = []
    completion = []
    study_times = []

    for session in sessions:
        topics.append(session["topic"])
        completion.append(session["done"])
        study_times.append(session["time"])
#stats
    total_time = sum(study_times)
    average_time = total_time / len(sessions)

    total_done = sum(completion)
    average_done = total_done / len(sessions)

    #print stats
    print(Fore.CYAN + "\n======== STUDY STATISTICS ========")
    print(Fore.GREEN + f"Total Sessions: {len(sessions)}")
    print(Fore.GREEN + f"Total Study Time: {total_time:.2f} hrs")
    print(Fore.YELLOW + f"Average Study Time: {average_time:.2f} hrs")
    print(Fore.YELLOW + f"Average Completion: {average_done:.2f}%")

# graph
    print(Fore.CYAN + "\n====== COMPLETION BY TOPIC ======\n")

    graph_input = "\n".join(
        f"{topic} {done}"
        for topic, done in zip(topics, completion)
    )

    subprocess.run(
        ["termgraph"],
        input=graph_input,
        text=True
    )

    print(Fore.CYAN + "\n======= STUDY TIME BY TOPIC =======\n")


    subprocess.run(
        ["termgraph"],
        input=graph_input,
        text=True
    )
    
def view_summery():
    print("========SUMMERY========")
    print()
    total_sub = len(sessions)
    for i in range(total_sub):
        print(
            f"{i + 1}. "
            f"{sessions[i]['topic']}"
            f" - {sessions[i]['done']}% Done"
            f" - {sessions[i]['time']} hrs"
            f" - {sessions[i]['difficulty']}"
        )
        print()

    total_time = 0
    for i in range(total_sub):
        total_time += sessions[i]['time']

    print(f"TOTAL STUDY TIME {(total_time)} HRS")


print("============STUDY TRACKER============")
print("1. Add Session  2.View Session 3.View Stats 4.View Summary 5.Exit")
choice = input("Enter your choice: ")

if choice == "1":
    add_Session()
    os.system("clear")
    view_sessions()
elif choice == "2":
    os.system("clear")
    view_sessions()
elif choice == "3":
    os.system("clear")    
    view_stats()
elif choice == "4":
    view_summery()    
elif choice == "5":
    print("Exit")
else:
    print("Invalid choice")

