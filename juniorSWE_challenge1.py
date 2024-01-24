"""

Author: Cole Emerine

Challenge #1 for Junior Software Engineer
TAMID Group Application


"""

#sortArrays is a function that joins two arrays together and sorts them up until k elements long
def sortArrays(arr1, arr2, k):

    #the space/time complexity of this methdod is dependent upon the sort() function
    #the sort function has a 'big O notation' of O(nlogn)
    sorted = arr1+arr2
    sorted.sort()

    return sorted[0:k]




#main function to incorporate the test cases through user input and execute the code
def main():
    condition = True;

    #this while loop allows the user to continue to test different combinations of arrays and lengths
    while(condition):
        arr1 = input("Enter the numbers for the first array separated by a space: ")
        arr2 = input("Enter the numbers for the second array separated by a space: ")
        k = int(input("Enter the size of the final array: "))

        #this separates the users entered numbers into arrays
        arr1 = arr1.split(" ")
        arr2 = arr2.split(" ")

        #this converts the user inputted arrays from strings to integers
        #this try/exception block aims to catch any errors that may be introduced into the arrays from the user
        try:
            for i in range(0, len(arr1)):
                if len(arr1) != 1:
                    arr1[i] = int(arr1[i])
                else:
                    arr1 = []

            for j in range(0, len(arr2)):
                if len(arr2) != 1:
                    arr2[j] = int(arr2[j])
                else:
                    arr2 = []
        except:
            print("Please only input numbers and separate with a singular space (i.e. 1 1 2 21 3 7)\n")
            continue


        sorted = sortArrays(arr1, arr2, k)
        print("Your sorted array is: ", end="")
        print(sorted)
        print()

        choice = input("Would you like to combine and sort two more arrays? (Yes/No) ")
        print()
        if choice == ("No"):
            condition = False


    print("Thanks for using sortArrays, goodbye!")


#command line check to ensure this file is the main file being run
if __name__=="__main__":
    main()