import sys
number_of_days = int(sys.argv[1])
if number_of_days<4:
    #solution when the number of days N is less than 4
    print("for %s days: %s" % (number_of_days,str(2**(number_of_days-1))+'/'+str(2**number_of_days)))
else:
    consecutive_days = 4 # since he/she is not allowed to miss classes for four or more consecutive days
    probability = 2**3 
    no_of_combo_with_one_day_absent = 2 
    no_of_combo_with_two_day_absent = 1
    no_of_combo_with_three_day_absent = 1
    for iteration in range(4,number_of_days+1):
        i = no_of_combo_with_three_day_absent
        no_of_combo_with_three_day_absent = no_of_combo_with_two_day_absent
        no_of_combo_with_two_day_absent = no_of_combo_with_one_day_absent
        no_of_combo_with_one_day_absent = consecutive_days
        consecutive_days = probability
        probability = (probability - i)*2+i
    print("for %s days: %s" % (number_of_days,str(no_of_combo_with_three_day_absent+no_of_combo_with_two_day_absent+no_of_combo_with_one_day_absent) + '/' + str(probability)))
