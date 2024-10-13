import math
def buy(loan_amount,interest_rate=0.059,years=30):
    period = {
        'WEEKLY':7,
        'FORTNIGHTLY':14,
        'MONTHLY':30.4375
    }
    days=365.25*years
    payment_instance_cnt = days/period['WEEKLY']
    payment_instance_base_amount = loan_amount/payment_instance_cnt
    #print(payment_instance_cnt,payment_instance_base_amount)
    remain_instance_loan_amount = [loan_amount - payment_instance_base_amount * xth_period for xth_period in range(1,math.ceil(payment_instance_cnt)+1)]
    interest_instance_amount = [interest_rate/(365.25/period['WEEKLY']) * x for x in remain_instance_loan_amount]
    return interest_instance_amount
def buy_amortized(loan_amount,interest_rate, years=30,period='WEEKLY'):
    PERIOD = {
        'WEEKLY':7,
        'FORTNIGHTLY':14,
        'MONTHLY':30.4375
    }
    n = years*52
    r = interest_rate/n
    print('info:',interest_rate,r,r*n,n)
    D = ((1+r)**n-1)/(r*(1+r)**n)
    total_payment = L = loan_amount*(r*(1+r)**n)/((1+r)**n-1)
    return total_payment