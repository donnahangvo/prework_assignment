#"""Question 1"""
print("Question 1")
def hello_name(username):
    print("Hello, " + username.title() + "!")

hello_name('donna')

"""Question 2"""
print("Question 2")
def first_odds(start, end):
    numbers = range(start, end)
    for num in numbers:
        if num % 2 !=0:
            print(num)
first_odds(1,100)

"""Question 3"""
print("Question 3")
def max_num_in_list(a_list):
    max_list = max(a_list)
    print(max_list)
max_num_in_list([22, 33, 84, 10, 6])

"""Question 4"""
print("Question 4")
def is_leap_year(a_year):
    year = a_year
    if (year % 4==0 and year%100!=0 or year%400==0):
        print("True")
    else:
        print("False")
is_leap_year(2000)

"""Question 5"""
print("Question 5")
def is_consecutive(a_list):
    con_num = a_list
    if sorted(con_num) == list(range(min(con_num), max(con_num)+1)):
        print("True")
    else:
        print("False")
is_consecutive([2,3,4,5,6,7])
is_consecutive([1,2,4,5])


