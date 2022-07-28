import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
elif float(sys.argv[1]) == False:
    sys.exit("Command-line argument not a number")

user_input = float(sys.argv[1])

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    result = (r['bpi']['USD']['rate'])
    result = float(result.replace(",", ""))
    answer = result * user_input
    print(f"${answer:,.4f}")
except requests.RequestException:
    sys.exit('Unable to handle request.')