import os
os.system("clear")

topics = []
times = []
session = {
    "topics":[], "times":[], "done":[], "difficulty":[]}

print("============STUDY TRACKER============")

#name = input("Enter your Name: ")
total_sub=int(input("How many subjects did you studied today? "))
print("-----------------------")

for i in range(total_sub): 
    topic = input(f"Topic No.{i+1}: ").upper()
 
    session["topics"].append(topic)

    time = float(input("Study Time (hrs): "))

    session["times"].append(time)

    done = input("Done? (y/n): ").lower()
    if done == "y":
        session["done"].append(100)
    elif done == "n":
        how_much = float(input("how much left (in %):"))
        session["done"].append(100 - how_much)
    
    diff = input("Difficulty level? (1-5): ").lower()

    if diff == "1":
        diff = "Easy"
    elif diff == "2":
        diff = "Medium"
    elif diff == "3":
        diff = "Hard"
    elif diff == "4":
        diff = "Very Hard"
    elif diff == "5":
        diff = "Extreme" 
    session["difficulty"].append(diff)
     
    
    session["times"].append(time)
   

#
# topic = input("Topic No.2: ")/topics.append(topic)
# time = float(input("Study Time (hrs): "))/times.append(time)
# #
# topic = input("Topic No.3: ")/topics.append(topic)
# time = float(input("Study Time (hrs): "))/times.append(time)


os.system("clear")

print("========SUMMERY========")
#print("Student Name:", name)
print("=======================")
for i in range(total_sub):
    print(
        f"{i + 1}. "
        f"{session['topics'][i]}"
        f" - {session['done'][i]}% Done"
        f" - {session['times'][i]} hrs"
        f" - {session['difficulty'][i]}"
    )
print("=======================")
total_time = 0
for i in range(total_sub):
    total_time += session['times'][i]

print(f"Total Study Time: {(total_time)} hrs")
