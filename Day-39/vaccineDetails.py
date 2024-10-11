

while True:
    total_people = int(input("Enter the total no of people in the area:"))
    single_dose_count = int(input("Single-dose count:"))
    double_dose_count = int(input("Double-dose count:"))

    if (total_people <=0):
        print('Invalid input')
        break
    elif(single_dose_count < 0 or single_dose_count > total_people):
        print('Invalid input')
        break
    elif(double_dose_count < 0 or double_dose_count > total_people):
        print('Invalid input')
        break
    elif((single_dose_count + double_dose_count)>total_people):
        print('Invalid input')
        break
    else:
        notVaccinated = (total_people - (single_dose_count+double_dose_count))
        total_vaccinated_percentage = (double_dose_count/total_people)*100
        print(f'Not vaccinated people count: {notVaccinated}')
        print(f'Total vaccinated percentage of people: {total_vaccinated_percentage:.2f}%')

    nextArea = int(input("Do you want to continue (1) for yes (0) for no:"))
    if (nextArea == 1):
        continue
    elif(nextArea == 0):
        break
    else:
        print('Invalid input')
        break

    


