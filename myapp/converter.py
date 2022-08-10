
from forex_python.converter import CurrencyRates
import myapp.views as views
from tabulate import tabulate
import myapp.models as models

# Function to convert the currency from source to destination
def convert():
    file_content = views.read_file()
    transfer_details = []
    # handling multiple dataentry on the csv file
    for i in range(0,len(file_content)):
        list_trans = []
        transactions = file_content[i]
        transaction_details = transactions.split(',' or '|')
        transaction_id = transaction_details[0]
        source = transaction_details[1]
        destination = transaction_details[2]
        amount = float(transaction_details[3])
        cr = CurrencyRates()
        output = cr.convert(source, destination, amount)
        list_trans.append(transaction_id)
        list_trans.append(source)
        list_trans.append(destination)
        list_trans.append(amount)
        list_trans.append(output)
        transfer_details.append(list_trans)

    return(transfer_details)


