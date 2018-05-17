#Tommy Garcia

def calculate_tax(income=250000):

    #tax = 0

    if income <= 250000:

        tax = income * 0.4

    else:

        tax = 250000 * 0.4 + (income - 250000) * 0.8

    return int(tax)



def main():

    print("$100,000 * 0.40 =","$"+"{:,}".format(calculate_tax(100000)))
    print("$250,000 * 0.40 + $50,000 * 0.80 =","$"+"{:,}".format(calculate_tax(300000)))

main()
