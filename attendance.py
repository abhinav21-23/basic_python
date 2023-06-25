classes_held=int(input("Enter the number of classes held\n"))
classes_attended=int(input("Enter the number of classes attended\n"))
percent_class_attended=(classes_attended/classes_held)*100
if(percent_class_attended<75):
    print("You have attended", percent_class_attended, "% classes. You are not allowed to sit in the exam.")
else:
    print("You have attended", percent_class_attended, "% classes. You are allowed to sit in the exam.")