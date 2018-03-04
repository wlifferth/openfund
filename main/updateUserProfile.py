from datetime import date, timedelta

def updateUserProfile(user, data):
    # Update general goals:
    user.generalGoals = data['generalGoals']

    # Time value of money!
    if 'retirementTargetAmount' in data and 'bigTicketTargetAmount' in data:
        time1 = date.today() + timedelta(years=data['retirementTime'])
        amount1 = data['retirementTargeAmount']
        time2 = date.today() + timedelta(years=data['bigTicketTime'])
        amount2 = data['bigTicketTargetAmount']
        interestRate = 0.02
        time, amount = convertToFirstTime(time1, amount1, time2, amount2, i=interestRate)
        user.targetAmount = amount
        user.targetDate = time
        user.targetDate = date.now() + timedelta(years=data['retirementTime'])

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
