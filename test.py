import argparse
import math
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()


if len(sys.argv) < 5:
    print('Incorrect parameters')
elif args.type == 'annuity':
    # annuity
    if args.payment == None:
        i = (float(args.interest) / 100) / 12
        annuity = math.ceil(float(args.principal) * (i * pow(i + 1, float(args.periods))) / (pow(1 + i, float(args.periods)) - 1))
        print(f'Your annuity payment = {annuity}!')
        overpayment = annuity * int(args.periods) - int(args.principal)
        print(f'Overpayment = {overpayment}')
    # credit principal
    elif args.principal == None:
        i = (float(args.interest) / 100) / 12
        credit_principal = math.floor(float(args.payment) / (i * pow(1 + i, float(args.periods)) /
                                                             (pow(1 + i, float(args.periods)) - 1)))
        print(f'Your credit principal = {credit_principal}!')
        overpayment = int(args.payment) * int(args.periods) - credit_principal
    # periods
    elif args.periods == None:
        i = (float(args.interest) / 100) / 12
        n = math.ceil(math.log(float(args.payment) / (float(args.payment) - i * float(args.principal)), 1 + i))
        years = n // 12
        months = n % 12
        if years == 0:
            if months == 1:
                print(f'You need {months} month to repay this credit!')
            else:
                print(f'You need {months} months to repay this credit!')
        elif months == 0:
            if years == 1:
                print(f'You need {years} year to repay this credit!')
            else:
                print(f'You need {years} years to repay this credit!')
        else:
            print(f'You need {years} years and {months} to repay this credit!')
        overpayment = (years * 12 + months) * int(args.payment) - int(args.principal)
        print(f'Overpayment = {overpayment}')
elif args.type == 'diff':
    if args.payment != None:
        print('Incorrect parameters')
    else:
        i = (float(args.interest) / 100) / 12
        counter = 0
        for m in range(1, int(args.periods) + 1):
            d = math.ceil(float(args.principal) / float(args.periods) + i * (float(args.principal) - float(args.principal) * (m - 1)
                                                                   / float(args.periods)))
            print(f'Month {m}: paid out {d}')
            counter += d
        overpayment = counter - int(args.principal)
        print(f'Overpayment = {overpayment}')
else:
    print('Incorrect parameters')

