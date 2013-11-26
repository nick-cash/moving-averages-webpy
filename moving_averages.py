# Simple Moving Average
#   series - list of numbers
#   period - time period used to slice the list
def simple_moving_average(series, period):
    period_list = series[len(series)-period:]
    return sum(period_list)/len(period_list)

# Cumulative Moving Average
#   Note: This function works with successive values and assumes series[-1] is
#         our newest number to average.
#   series - list of numbers
#   last_cma - our last computed moving average
def cumulative_moving_average(series, last_cma):
    if len(series) > 1:
        return ((last_cma*(len(series)-1))+series[-1])/len(series)
    else:
        return series[-1]

# Weighted Moving Average
#   Note: Weights decrease in arithmetical progression starting at period and
#         ending at 1.
#   series - list of numbers
#   period - time period we are using for calculations
def weighted_moving_average(series, period):
    period_list = series[len(series)-period:]
    return sum([(i+1)*num for i,num in enumerate(period_list)])/((period*(period+1))/2)


# Exponential Moving Average
#   Note: This function works over successive values and assumes series[-1] is
#         our newest number to average.
#   series - list of numbers
#   period - time period we are interested in, used only to calculate smoothing
#   last_ema - our last exponential moving average value
def exponential_moving_average(series, period, last_ema, smoothing=None):
    # Must be between 0 and 1. Higher values discount old data faster.
    if not smoothing or smoothing > 1.0 or smoothing < 0.0:
        smoothing = 2.0/(period+1.0)

    if len(series) > 1:
        return last_ema+(smoothing*(series[-1]-last_ema))
    else:
        return series[-1]
