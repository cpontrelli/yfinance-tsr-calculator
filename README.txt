If you don't have python installed:
1. Open windows store
2. Search for python
3. Install newest verion of python (ex: 3.9.2)
	a. This will be free. Do not pay for anything
4. Verify installation by opening command prompt (in the windows start menu) and entering: pyhon --version
	a. This should display the version of python you installed

How to run the program:
1. Open the command prompt (in the windows start menu)
2. Navigate to the folder with the python script using the cd command and folder name
	a. Ex: cd Desktop/yfinance-tsr-calc
3. If you are running this for the first time enter command: pip install yfinance --upgrade --no-cache-dir
	a. Move to step 4 if you have run this already
4. Enter company info in input.csv
	a. Replace the company names, tickers, and FYEs you want to calculate
	b. Do not adjust the column header names. They need to be Name, Ticker, FYE
5. Close input.csv and output.csv
6. Enter command: python tsr-calc.py
7. Wait for command prompt to return (this means the program is done running)
8. Open output.csv to see the results

Trouble Shooting
1. yfinance API will occasionally hang for some prices. Will need to add a fix for this
