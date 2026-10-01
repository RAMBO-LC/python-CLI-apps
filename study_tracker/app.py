import os
os.system("clear")

topics = []
times = []

print("============STUDY TRACKER============")
#name = input("Enter your Name: ")
print("-----------------------")

topic = input("Topic No.1: ")/topics.append(topic)
time = float(input("Study Time (hrs): "))/times.append(time)
#
topic = input("Topic No.2: ")/topics.append(topic)
time = float(input("Study Time (hrs): "))/times.append(time)
#
topic = input("Topic No.3: ")/topics.append(topic)
time = float(input("Study Time (hrs): "))/times.append(time)


os.system("clear")

print("========SUMMERY========")
#print("Student Name:", name)
print("=======================")
for i in range(3):
    print(f"{i+1}. {topics[i]} - {times[i]} hrs")
print("=======================")


