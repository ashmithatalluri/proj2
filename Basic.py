import csv
def write_info_csv(info_list):
      with open('student_info.csv','a', newline ='') as csv_file:
            writer=csv.writer(csv_file)

            if csv_file.tell() == 0:
                  writer.writerow(["NAME","AGE","EMAIL_ID"])
            writer.writerow(info_list)
           

if __name__ == '__main__':
      condition= True
      student_num= 1
      
      while (condition):
            student_info=input("enter the student info for student #{}: "
                               . format(student_num))
            student_info_list=student_info.split(" ")

            print("\nthe entered info is -\n Name: {}\n Age: {}\n Email_id: {}"
                  . format(student_info_list[0],student_info_list[1],student_info_list[2]))

            choice_check=input("entered info is correct(Y/N): ")
                  
            if choice_check == "Y":
                  write_info_csv(student_info_list)
            
                  condition_check=input("enter (Y/N) for accepting another students info: " )
                  if condition_check == "Y":
                        condition = True
                        student_num = student_num + 1
                  elif condition_check == "N":
                        condition = False
            
            elif choice_check == "N":
                  print("\n re-enter the inFO!")
