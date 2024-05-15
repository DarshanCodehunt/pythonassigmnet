# ----------------------------------------

# def checklastfirst(arr):
#     last_index = len(arr) - 1;
#     if arr[0] == arr[last_index]:
#         return True
#     else:
#         return False
    
    
# print(checklastfirst([10, 20, 30, 40, 10]))
# print(checklastfirst([75, 65, 35, 75, 30]))
    
# ---------------------------------------------

# list = [10, 20, 33, 46, 55]
# for x in list:
#     if x%5 == 0:
#         print(x)
        
# --------------------------------------------------

# name = "Emma is good developer. Emma is a writer"
# print("Emma appeared " + str(name.count("Emma")) + " times")


# --------------------------------------------------


# def checkPalindrome(number):
#     if str(number) == str(number)[::-1]:
#         print("Yes. given number is palindrome number")
#     else:
#         print("No. given number is not palindrome number")
        
# checkPalindrome(121)

# -----------------------------------------------------------

# def reverseInt(number):
#     reverseNum = str(number)[::-1]
#     test = ' '.join(reverseNum)
#     print(test)
    
    
# reverseInt(7536)

# --------------------------------------------

# def sortLowerUpper(word="PyThOnIndIA"):
#     lower = ''
#     upper =''
#     for x in word:
#         if x.islower() == True:
#             lower = lower + x
#         elif x.isupper() == True:
#             upper = upper + x

#     print(lower+upper)
            
    
    
# sortLowerUpper("PyThOnIndIA")

#---------------------------------------------
    

# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# result = []

# for x in str_list:
#     if x:
#         result.append(x)


# print(result)  
