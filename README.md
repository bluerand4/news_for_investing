# Automated Stock Analysis and Reporting System

This project automates the process of fetching, analyzing, and reporting on stock market data. It includes scripts to update financial data, fetch stock prices, save analyst reports, and generate video summaries of stock news.
Prerequisites

# Replace API keys

Before running the scripts, ensure you have the necessary API keys and dependencies installed.
Required API Keys

    OpenAI API Key
    NSE API Key
    SECGOV API Key
    MongoDB API Key

Replace the placeholders in the scripts with your actual API keys.
Dependencies

# Installation

Install the required Python packages using pip:

    pip install -r requirements.txt


# Running the Scripts

Update Stock Fundamentals

Updates fundamental financial data (income statement, cash flow statement, balance sheet) for ~5000 US public stocks.

    python run_update_analysis_com.py

Fetch Stock Prices

Fetches one-day and one-minute bar chart data for all US public stocks from Polygon and TradingView.

    python run_mini1.py

Save Analyst Reports

Saves analyst reports for selected stocks from SeekingAlpha and updates Google Drive with stocks that have crossed their 200-day maximum high price, aligning them based on healthier financial trajectories (e.g., highest slope for revenue, net income, and cash flow increase).

    python run_pro2.py

Generate and Upload YouTube Videos

Fetches news information for selected stocks from various sources (e.g., WSJ, Google News), summarizes the news using OpenAI API, generates a video with the summary, and uploads it to YouTube.

    python run_youtube.py

Script Descriptions
run_update_analysis_com.py

Updates stocks' fundamental financial data.
Includes income statement, cash flow statement, and balance sheet.

    run_mini1.py

Fetches one-day and one-minute bar chart data.
Sources include Polygon and TradingView.

    run_pro2.py

Saves analyst reports on selected stocks.
Updates Google Drive with stocks based on financial health metrics.

    run_youtube.py

Fetches and summarizes stock news from various sources.
Generates videos and uploads them to YouTube.

# Usage

Ensure all API keys are correctly replaced in the respective scripts.
Install the required dependencies.
Run the scripts in the order mentioned to update data, fetch prices, save reports, and generate videos.

# Example Commands

    python run_update_analysis_com.py
    python run_mini1.py
    python run_pro2.py
    python run_youtube.py

# example website:

    https://www.youtube.com/@user-me9ns6tw2s

# Contributing

Contributions are welcome! Please create a pull request with detailed information on your changes.

# License

This project is licensed under the MIT License.