import sys

def generate_report(dead_count,injured_count,safe_count):
    print("TSUNAMI REPORT OF JAPAN")
    print("The number of people")
    print(f"Dead:{dead_count}")
    print(f"Injured:{injured_count}")
    print(f"Safe:{safe_count}")
    print("Please help the people who are suffering !!")

def check_negative(count):
    if count<0:
        print("Invalid input.")
        sys.exit()


dead_count = int(input("Dead Count:"))
check_negative(dead_count)
injured_count = int(input("Injured Count:"))
check_negative(injured_count)
safe_count = int(input("Safe Count:"))
check_negative(safe_count)

generate_report(dead_count,injured_count,safe_count)




