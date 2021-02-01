#============== Done with procedural ==============

# total_hours = input('PLease Enter Your Total Hours: ')
# rate_per_hour = input('Please Enter The Rate per Hour : ')
# total_pay = (int(total_hours) * float(rate_per_hour) )

# print(total_pay)


#============== Done  with Function ==============

def payroll(total_hours, rate_per_hour):
    
    total_pay = (int(total_hours) * float(rate_per_hour) )
    
    return total_pay

a = input('PLease Enter Your Total Hours: ')
b = input('Please hourly rate : ')

c = payroll(a, b)

print("Total Pay :",c)


# =========== Done with class  =============== 

# class Payroll:

#     total_hours = int(input('PLease Enter Your Total Hours: '))
#     rate_per_hour = float(input('Please Enter The Rate per Hour : '))
    
#     def pay(self):
        
        
#         return self.total_hours * self.rate_per_hour 
    

# obj = Payroll()

# print(obj.pay())