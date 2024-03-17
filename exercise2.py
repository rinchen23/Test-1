from queue import Queue
patient = Queue
current_patient = None
while True:
    print(""" Desk manager: Select the option below:
          1.Register patent
          2.Remove patient
          3.Display patient queue
          4.Exit """)
userinput = input(">>>")
print()
if userinput == "1":
    patient_name = input("Enter patient name:")
    patient.put(Patient_name)
    current_patient = patient_name
    print(f"patient {patient_name} successfully registered")
elif userinput == "2":
    patient.get()
    print(f"patient {current_patient} removed after meeting the doctor")
elif userinput == "3":
    print("curret patient queue")
    for i in patient.queue:
        print(i)
elif userinput == "4":
    print("Exited")
    