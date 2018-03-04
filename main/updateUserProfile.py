from datetime import date, timedelta
from numpy import log
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

def updateUserProfile(user, data):
    # Update general goals:
    user.generalGoals = data['generalGoals']

    # Time value of money!
    if 'retirementTargetAmount' in data and 'bigTicketTargetAmount' in data:
        time1 = date.today() + timedelta(days=365*int(data['retirementTime']))
        amount1 = float(data['retirementTargetAmount'])
        time2 = date.today() + timedelta(days=365*int(data['bigTicketTime']))
        amount2 = float(data['bigTicketTargetAmount'])
        interestRate = 0.02
        time, amount = convertToFirstTime(time1, amount1, time2, amount2, i=interestRate)
        # We add in the targetAmount and targetDate!
        user.targetAmount = amount
        user.targetDate = time
    elif 'retirementTargetAmount' in data:
        user.targetAmount = float(data['retirementTargetAmount'])
        user.targetDate = date.today() + timedelta(days=365*int(data['retirementTime']))
    elif 'bigTicketTargetAmount' in data:
        user.targetAmount = float(data['bigTicketTargetAmount'])
        user.targetDate = date.today() + timedelta(days=365*int(data['bigTicketTime']))

    # Update target contributions
    user.targetContributions = float(data['targetContribution'])

    # Calculate riskTolerance
    calculateRiskTolerance(user, data)



def convertToFirstTime(time1, amount1, time2, amount2, i):
    # Make sure that time1 is before time2
    if time1 > time2:
        tmp = time2
        time2 = time1
        time1 = tmp
        tmp = amount2
        amount2 = amount1
        amount1 = tmp
    delta = time2 - time1
    a = (1 + i) ** (delta.days / 365.25)
    amount2AtTime1 = amount2 / a
    finalAmount = amount1 + amount2AtTime1
    finalTime = time1
    return (finalTime, finalAmount)

def calculateRiskTolerance(user, data):
    print('\n')
    total_possible = 0
    earned = 0
    # Add points if they have a lot of savings
    # Max 10
    currentSavings = float(data['currentSavings'])
    lcs = log(currentSavings + 1)
    savingsPoints = min(lcs / 1.1, 10)
    total_possible += 10
    earned += savingsPoints

    # Add points if they have a large takehome pay
    # Max 10
    currentTakehome = float(data['currentTakehome'])
    lct = log(currentTakehome + 1)
    takehomePoints = min(lct / .8, 10)
    total_possible += 10
    earned += takehomePoints

    # Subtract points for debt/income
    # Max |-alot|
    monthsWorthOfDebt = float(data['currentDebt']) / currentTakehome
    earned -= monthsWorthOfDebt
    total_possible += 0

    # Subtract points for children
    # Max |-5|
    currentChildren = float(data['currentChildren'])
    lcc = log(currentChildren + 1)
    childrenPoints = -max(lcc / .4, 5)
    total_possible += 0
    earned += childrenPoints

    # Subtract points for health problems
    # Max |-5|
    try:
        healthProblems = data['healthProblems']
        total_possible += 0
        if healthProblems == "on":
            earned += -5
    except:
        pass

    # Add points for far retirement
    # Max 5
    retirementTime = int(data['retirementTime'])
    lrt = log(retirementTime + 1)
    retirementPoints = min(lrt, 5)
    total_possible += 5
    earned += retirementPoints

    # Add points for far big ticket
    # Max 2
    bigTicketTime = int(data['bigTicketTime'])
    lrt = log(bigTicketTime + 1)
    bigTicketPoints = min(lrt, 2)
    total_possible += 2
    earned += bigTicketPoints
    # Add points from risk questions
    earned += int(data['questionOne'])
    earned += int(data['questionTwo'])
    earned += int(data['questionThree'])
    total_possible += 12

    riskTolerance = 100 * earned / total_possible
    print(riskTolerance)
    return riskTolerance

def requiredRateOfReturn(initial, recurring, time, final):
    # initial * ((1 + i) ** (time))
    requiredRate = lambda r: initial * ((r + 1) ** time) + (recurring * 12) * ((((1 + r) ** time) - 1) / r) - final
    rates = list(range(1,100))
    rates = [r * 0.01 for r in rates]
    diffs = [requiredRate(r) for r in rates]
    plt.plot(rates, diffs)
    plt.show()
    initial_guess = 0.1
    print(fsolve(requiredRate, initial_guess))
