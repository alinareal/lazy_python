#money_on_borsch = 100
#borsch_portion_price = 2.75
#borsh_portion_number = money_on_borsch // borsch_portion_price
#borsch_fee = money_on_borsch % borsch_portion_price
#print borsh_portion_number

#money_on_dumplings = 100
#dumplings_portion_price = 2.19
#dumplings_portion_number = money_on_dumplings // dumplings_portion_price
#dumplings_fee = money_on_dumplings % dumplings_portion_price
#print dumplings_portion_number

#money_on_compote = 50
#compote_portion_price = 1.24
#compote_portion_number = money_on_compote // compote_portion_price
#compote_fee = money_on_compote % compote_portion_price
#print compote_portion_number

#total_fee = borsch_fee + dumplings_fee + compote_fee
#print total_fee

borsh_portion_number = 100 // 2.75
borsch_tips = 100 % 2.75
borsch_tips = round(borsch_tips, 2)
print borsch_tips, borsh_portion_number
