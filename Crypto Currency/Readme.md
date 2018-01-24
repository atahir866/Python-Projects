### Python Script for sending email notification about introduction to new currency on Binace Cryptovurrency exchange.

* It will check for currencies on Binance exchange using Binance API.
* Every minute, a request will be sent to Binance excahange and results will be stored in an array.
* It will compare cuurencies with the previous list of currencies.
* If the two lists dont match then it will find the new currency in the latest extracted list.
* Upon retrieval, it will send an email notification containing the name of new currencies.
