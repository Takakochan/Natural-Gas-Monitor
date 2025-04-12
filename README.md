Natural Gas EIA Forecast vs Actual with Price Overlay

This project visualizes the relationship between natural gas storage levels (reported by the U.S. Energy Information Administration, EIA) and historical futures prices. It processes data from an HTML source and a CSV file, cleans and merges them, and produces a dual-axis line chart showing Actual vs Forecast values alongside market prices.

Features

Parses and processes natural gas supply data from an HTML table

Handles and preserves negative values for accurate financial modeling

Combines EIA supply data with market price data

Visualizes recent records with a dual-axis matplotlib plot

Clean and well-documented Python code suitable for portfolio use

Project Structure

natural-gas-eia-app/
├── data/
│   ├── gas.html                          # EIA HTML table (local copy)
│   └── Natural Gas Futures Historical Data.csv  # Price data from investing.com
├── main.py                              # Main script to run the analysis
└── README.md                            # Project documentation

Requirements

Python 3.7+

pandas

matplotlib

You can install the dependencies using pip:

pip install pandas matplotlib

How to Run

Clone the repository:

git clone https://github.com/yourusername/natural-gas-eia-app.git
cd natural-gas-eia-app

Make sure the data files (gas.html and the CSV) are in the data/ folder.

Run the script:

python main.py

This will display a plot showing:

Actual and Forecast EIA storage values (left axis)

Natural gas futures price (right axis)

Example Output

A plot with two y-axes:

Left Y-axis: Actual vs Forecasted Natural Gas Storage (in Bcf)

Right Y-axis: Natural Gas Futures Prices (USD)

X-axis: Release Date



