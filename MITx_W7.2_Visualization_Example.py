"""
Want to explore how the ability to visualize results can help guide computation

Planning for retirement example:
    - intend to save an amount m each month
    - intend to earn a percentage r of income on investments each month
    - want to explore how big a retirement fund will be compounded by time ready to retire

Use visualization to guide the computation

Interaction with plotting routines and computations allows us to explore data:
    - change display range to zero in on particular areas of interest
    - change sets of values and visualize effect - then guides new choice of values to explore
    - change display parameters to highlight clustering of plots by parameter

"""
from pylab import plt

def retire(monthly, rate, terms):
    """
    :param monthly: amount to put aside each month
    :param rate: rate at which going to earn interest
    :param terms: amount of months
    :return: list of months, list of savings for each month
    """
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += [i]     # adds label for the next month
        savings += [savings[-1]*(1 + mRate) + monthly]  # savings with accrued interest + new monthly contribution
    return base, savings

# now, displaying the results
def displayRetireWMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)     # using base and savings list as x and y values
        plt.plot(xvals, yvals, label='retire with monthly inst of '+str(monthly))
        plt.legend()

displayRetireWMonthlies([500,600,700,800,900,1000, 1100], .05, 40*12)
plt.show()

def displayRetireWRate(month, rates, terms):
    plt.figure('retireRate')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals, label='monthly: '+ str(month)+ ' rate of:     ' + str(int(rate*100)))
        plt.legend(loc = 'upper left')

displayRetireWRate(800, [.03, .05, 0.07], 40*12)
plt.show()


def displayRetireWMonthsandRates(monthlies, rates, terms):
    plt.figure('retire both')
    plt.clf()
    plt.xlim(30*12, 40*12)      # focusing only on the last 10 years of investment
    for monthly in monthlies:
        for rate in rates:
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, label='retire with '+ str(monthly) + ":" + str(int(rate*100)))
            plt.legend(loc = 'upper left')

displayRetireWMonthsandRates([500,700, 900, 1100], [.03, .05, .07], 40*12)
plt.show()

# its hard to distinguish because of the overlap
# more clear way of doing
def displayRetireWMonthsandRates2(monthlies, rates, terms):
    plt.figure('retire better')
    plt.clf()
    plt.xlim(30*12, 40*12)
    monthLabels = ['r', 'b', 'g', 'k']
    rateLabels = ['-', 'o', '^']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i % len(monthLabels)]      # using remainder to pick new label for each new month choice
        for j in range(len(rates)):
            rate = rates[j]
            rateLable = rateLabels[j % len(rateLabels)]     # if more months, cycles back to the beginning
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, monthLabel+rateLable, label = 'retire: ' + str(monthly) + " : " +
                     str(int(rate*100)))
            plt.legend(loc="upper left")

displayRetireWMonthsandRates2([500,700,900,1100], [.03, .05, .07], 40*12)
plt.show()