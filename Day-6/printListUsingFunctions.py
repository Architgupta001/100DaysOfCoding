# Write a script to create and print a list where the values are square of numbers between 1 and 30 

def demo(num):
    demo_list = []
    for i in range(1,num+1):
        demo_list.append(i**2)
    print(demo_list)

demo(10)
