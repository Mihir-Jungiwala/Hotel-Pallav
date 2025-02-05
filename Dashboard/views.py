from django.shortcuts import render
from django.db.models import Sum
from datetime import date
from django.contrib.auth.decorators import login_required

from Company.models import Company_Profile
from Expense.models import Food_Cash_Miscellaneous_Expenses, Food_Cash_Withdrawal, Hotel_Cash_Miscellaneous_Expenses, Hotel_Cash_Withdrawal, Staff_Advance
from Bill_Master.models import Bill_Master_ADD_Advance, Bill_Master_ADD_Bill
from Revenue.models import Food_Cash_Deposite, Hotel_Cash_Deposite
from Staff_Profile.models import User_Profile
from Shift_Handover.models import Shift_Handover

@login_required(login_url='Login_In')
def Dashboard_Profile(request):
    # Get the current date
    current_date = date.today()

    # Fetch the latest Shift_Handover entry ordered by Date and Time (descending)
    latest_shift_handover = Shift_Handover.objects.order_by('-Shift_Handover_Date', '-Shift_Handover_Time').first()

    # Calculate total staff count
    total_staff = User_Profile.objects.count()

    # Calculate total company count
    total_company = Company_Profile.objects.count()

    # Calculate hotel expenses
    total_withdrawal_hotel_amount = Hotel_Cash_Withdrawal.objects.filter(
        Withdrawal_Hotel_Date=current_date
    ).aggregate(total=Sum('Withdrawal_Hotel_Amount'))['total'] or 0

    total_miscellaneous_expenses_hotel_amount = Hotel_Cash_Miscellaneous_Expenses.objects.filter(
        Miscellaneous_Expenses_Hotel_Date=current_date
    ).aggregate(total=Sum('Miscellaneous_Expenses_Hotel_Amount'))['total'] or 0

    total_hotel_expenses = total_withdrawal_hotel_amount + total_miscellaneous_expenses_hotel_amount

    # Calculate food expenses
    total_withdrawal_food_amount = Food_Cash_Withdrawal.objects.filter(
        Withdrawal_Food_Date=current_date
    ).aggregate(total=Sum('Withdrawal_Food_Amount'))['total'] or 0

    total_miscellaneous_expenses_food_amount = Food_Cash_Miscellaneous_Expenses.objects.filter(
        Miscellaneous_Expenses_Food_Date=current_date
    ).aggregate(total=Sum('Miscellaneous_Expenses_Food_Amount'))['total'] or 0

    total_staff_advance = Staff_Advance.objects.filter(
        Staff_Advance_date=current_date
    ).aggregate(total=Sum('Staff_Advance_amount'))['total'] or 0

    total_food_expenses = total_withdrawal_food_amount + total_miscellaneous_expenses_food_amount + total_staff_advance

    # Calculate hotel income
    total_deposite_hotel_amount = Hotel_Cash_Deposite.objects.filter(
        Deposite_Hotel_Date=current_date
    ).aggregate(total=Sum('Deposite_Hotel_Amount'))['total'] or 0

    total_advance_hotel_amount = Bill_Master_ADD_Advance.objects.filter(
        Advance_Payment_Date=current_date,
        Hotel_Advance_MOD__iexact='cash'
    ).aggregate(total=Sum('Hotel_Advance_Amount'))['total'] or 0

    total_bill_hotel_amount = Bill_Master_ADD_Bill.objects.filter(
        Bill_Master_Bill_Date=current_date,
        Bill_Master_Hotel_Mode_Of_Payment__iexact='cash'
    ).aggregate(total=Sum('Bill_Master_Total_Hotel_Amount'))['total'] or 0

    total_debit_hotel_amount = Bill_Master_ADD_Bill.objects.filter(
        Bill_Master_Debit_Bill_Date=current_date,
        Bill_Master_Debit_Hotel_Mode_Of_Payment__iexact='cash'
    ).aggregate(total=Sum('Bill_Master_Debit_Hotel_Amount'))['total'] or 0

    total_hotel_income = total_deposite_hotel_amount + total_advance_hotel_amount + total_bill_hotel_amount + total_debit_hotel_amount

    hotel_balance = total_hotel_income - total_hotel_expenses

    # Calculate food income
    total_deposite_food_amount = Food_Cash_Deposite.objects.filter(
        Deposite_Food_Date=current_date
    ).aggregate(total=Sum('Deposite_Food_Amount'))['total'] or 0

    total_advance_food_amount = Bill_Master_ADD_Advance.objects.filter(
        Advance_Payment_Date=current_date,
        Food_Advance_MOD__iexact='cash'
    ).aggregate(total=Sum('Food_Advance_Amount'))['total'] or 0

    total_bill_food_amount = Bill_Master_ADD_Bill.objects.filter(
        Bill_Master_Bill_Date=current_date,
        Bill_Master_Food_Mode_Of_Payment__iexact='cash'
    ).aggregate(total=Sum('Bill_Master_Total_Food_Amount'))['total'] or 0

    total_debit_food_amount = Bill_Master_ADD_Bill.objects.filter(
        Bill_Master_Debit_Bill_Date=current_date,
        Bill_Master_Debit_Food_Mode_Of_Payment__iexact='cash'
    ).aggregate(total=Sum('Bill_Master_Debit_Food_Amount'))['total'] or 0

    total_food_income = total_deposite_food_amount + total_advance_food_amount + total_bill_food_amount + total_debit_food_amount

    food_balance = total_food_income - total_food_expenses

    

    # Calculate total debit bills
    debit_hotel_bills = Bill_Master_ADD_Bill.objects.filter(
        Bill_Master_Bill_Date=current_date,
        Bill_Master_Hotel_Mode_Of_Payment__iexact='debit',
        Bill_Master_Balance_Hotel_Amount__gt=0
    )

    debit_food_bills = Bill_Master_ADD_Bill.objects.filter(
        Bill_Master_Bill_Date=current_date,
        Bill_Master_Food_Mode_Of_Payment__iexact='debit',
        Bill_Master_Balance_Food_Amount__gt=0
    )

    total_debit_hotel_bills = debit_hotel_bills.count()
    total_debit_food_bills = debit_food_bills.count()

    # Prepare context for the template
    context = {
        'total_staff': total_staff,
        'total_company': total_company,
        'total_debit_hotel_bills': total_debit_hotel_bills,
        'total_debit_food_bills': total_debit_food_bills,
        'total_hotel_expenses': total_hotel_expenses,
        'total_food_expenses': total_food_expenses,
        'total_deposite_hotel_amount': total_deposite_hotel_amount,
        'total_hotel_income': total_hotel_income,
        'total_food_income': total_food_income,
        'shift_handover': latest_shift_handover,
        'hotel_balance' : hotel_balance,
        'food_balance' : food_balance,
        
    }

    # Render the dashboard template with the context
    return render(request, "dashboard.html", context)

# Function to convert numbers to words (Indian numbering system)
def numberToWords(num):
    if num < 0 or num > 100000000:  # Set the limit to 10 crore (10,00,00,000)
        return "Number out of range"

    belowTwenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                   "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                   "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Lakh", "Crore"]

    if num == 0:
        return "Zero Rupees Only"

    words = ""

    def helper(n):
        if n < 20:
            return belowTwenty[n]
        if n < 100:
            return tens[n // 10] + ("" if n % 10 == 0 else " " + belowTwenty[n % 10])
        if n < 1000:
            return belowTwenty[n // 100] + " Hundred" + ("" if n % 100 == 0 else " " + helper(n % 100))

    # Process the number in segments (Thousand, Lakh, Crore)
    crore = num // 10000000
    lakh = (num % 10000000) // 100000
    thousand = (num % 100000) // 1000
    remainder = num % 1000

    if crore > 0:
        words += helper(crore) + " Crore"
    if lakh > 0:
        words += (" " if words else "") + helper(lakh) + " Lakh"
    if thousand > 0:
        words += (" " if words else "") + helper(thousand) + " Thousand"
    if remainder > 0:
        words += (" " if words else "") + helper(remainder)

    return words.strip() + " Rupees Only"


