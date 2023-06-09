# def exchange_money(budget, exchange_rate):
    # """
    # :param budget: float - amount of money you are planning to exchange.
    # :param exchange_rate: float - unit value of the foreign currency.
    # :return: float - exchanged value of the foreign currency you can receive.
    # """
    # exchanged_value = (budget/exchange_rate)
    # return(exchanged_value)

# def get_change(budget, exchanging_value):
    # """
    # :param budget: float - amount of money you own.
    # :param exchanging_value: float - amount of your money you want to exchange now.
    # :return: float - amount left of your starting currency after exchanging.
    # """
    # remaining_amount = budget - exchanging_value
    # return remaining_amount

# def get_value_of_bills(denomination, number_of_bills):
    # """
    # :param denomination: int - the value of a bill.
    # :param number_of_bills: int - amount of bills you received.
    # :return: int - total value of bills you now have.
    # """
    # total_bills = denomination * number_of_bills
    # return total_bills

# def get_number_of_bills(budget, denomination):
    # """
    # :param budget: float - the amount of money you are planning to exchange.
    # :param denomination: int - the value of a single bill.
    # :return: int - number of bills after exchanging all your money.
    # """
    # number_of_bills = budget//denomination
    # return number_of_bills

# def get_leftover_of_bills(budget, denomination):
    # """
    # :param budget: float - the amount of money you are planning to exchange.
    # :param denomination: int - the value of a single bill.
    # :return: float - the leftover amount that cannot be exchanged given the current denomination.
    # """
    # leftover_bills = budget%denomination
    # return leftover_bills

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    percentage_calculus = spread/100
    actual_exchange_rate = exchange_rate + percentage_calculus
    exchange_total = budget * actual_exchange_rate
    # currency_denomination = int(exchange_total) / denomination
    return exchange_total

    # percentage_calculus = exchange_rate * spread
    # actual_exchange_rate = exchange_rate + percentage_calculus
    # exchange_total = budget/actual_exchange_rate
    # currency_denomination = exchange_total * denomination
    # return currency_denomination

test = exchangeable_value(100000, 10.61, 10, 1)
print(test)






