price_car=103300
downpayment=price_car*0.1
interest_rate=0.027

user_downpayment=float(input("Please enter your downpayment:"))

#check user downpayment more that 10% or not
# more than 10% user can buy car ,lese than 10% user canot buy car
if (float(user_downpayment)>=float(downpayment)):
    canbuy=True
    print("you can buy")
else:
    print("You are not eligible for the bank loan")
    canbuy=False

#when user can buy require user give how many that want to loan
if canbuy:
    # user max loan cannot more than car price
    loanmax=(float(price_car)-float(user_downpayment))
    print("you maximent can loan:"+str(loanmax))

    #check amount and ensure that the amount will not exceed
    check_loanmax=False
    while check_loanmax==False :

        loan_amount = float(input("loan amount :"))

        if loan_amount>loanmax :
            print("you cannot loan too more")
            check_loanmax=False
        else:
            check_loanmax=True

    loan_period_y = int(input("please enter your loan period in year:"))
    
   #Formula of total interest and monthly intstallment 
    total_interest = interest_rate * loan_amount * loan_period_y

    monthly_installment = (loan_amount + total_interest) / (12)

#receipt
    print("\nYou downpayment     :RM"+str(user_downpayment))
    print("Interest rate       :"+str(interest_rate))
    print("Loan amount         :RM"+str(loan_amount))
    print("Loan period (year)  :"+str(loan_period_y))

    print("Total interest      :RM"+str(total_interest))
    print("You need to pay RM"+str(monthly_installment)+" monthly installment")
    
