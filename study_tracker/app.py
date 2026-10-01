import os


print("============STUDY TRACKER============")
name = input("Enter your Name: ")
print("-----------------------")

topic_01 = input("Topic No.1: ")
time_01 = float(input("Study Time (hrs): "))
print("-----------------------")

topic_02 = input("Topic No.2: ")
time_02 = float(input("Study Time (hrs): "))
print("-----------------------")

topic_03 = input("Topic No.3: ")
time_03 = float(input("Study Time (hrs): "))

topic = [topic_01, topic_02, topic_03]
time = [time_01, time_02, time_03]

os.system("clear")

print("========SUMMERY========")
print("Student Name:", name)
print("=======================")
for i in range(3):
    print(f"{i+1}. ",f"{topic[i]} ","-",time[i]," hrs")
print("=======================")


