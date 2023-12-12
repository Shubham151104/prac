'''

Assignment :Group B -14
Write a python program to store first year percentage of students in array.
Write function for sorting array of floating point numbers in ascending order
using 
a) Selection Sort 
b) Bubble sort and display top five scores.

'''


def accept_percentage(A):
    n = int(input("Enter number of students in First year "))
    for i in range(n):
        per = float(input(" Enter Percentage of student : "))
        A.append(per)


def display(A):
    if len(A) == 0:
        print(" No recors found ")
    else:
        print(" Percentage of students :", end = " " )
        for i in range(len(A)):
            print( A[i], end= "   ")
        print("\n")


def bubble_sort(A):
    n=len(A)
    for i in range(n):
        for j in range(n-i-1):
            if A[j] < A[j+1]:
                temp = A[j+1]
                A[j+1] = A[j]
                A[j] = temp      #swap a,b = b,a
                

def selection_sort(A):
    n=len(A)
    for i in range(n-1):        
        min_ind = i
        for j in range(i+1, n):     #finding min element in array     
            if A[j] < A[min_ind]:
                min_ind = j

        A[i], A[min_ind] = A[min_ind], A[i]     

        
    


def main():
    while True:
       print("\n\n")
       print("\t1: Accept percentage of First Year Students ")
       print("\t2: Display percentage of students  ")
       print("\t3: Selection Sort ")
       print("\t4: Bubble sort")
       print("\t5: Display top five scores")
       print("\t6: Exit")
       ch=int(input("\t Enter Your Choice : "))
       if ( ch==6 ):
           print("\t End of Program!")
           quit()
       elif(ch==1):
           marks=[]
           accept_percentage(marks)

       elif(ch==2):
           display(marks)

       elif(ch==3):
           selection_sort(marks)
           print(" Percentage of students after sorting in ascending order : ")
           display(marks)

       elif(ch==4):
           bubble_sort(marks)
           print(" Percentage of students after sorting in decending order : ")
           display(marks)
              
       elif(ch==5):
           bubble_sort(marks)
           if len(marks) < 5:
               print("Top %d students : "%(len(marks)))
               for i in range(len(marks)):
                   print(marks[i], end="   ")
           else:    
               print("Top 5 Students : ")
               for i in range(5):
                   print(marks[i], end="   ")
              
       else:
           print("INVALID CHOICE")

main()
