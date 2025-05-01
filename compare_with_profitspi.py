#!/usr/bin/env python3
"""
Script to compare our indicator implementations with ProfitSPI's calculations.
This script will:
1. Run a backtest in ProfitSPI that uses specific indicators
2. Extract the indicator values at specific points in time from ProfitSPI
3. Calculate the same indicators with our implementation using the same data
4. Compare the results to ensure they match
"""

import os
import sys
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import yfinance as yf
from pprint import pprint

# Add the SDK to the path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import our indicator implementation
from profitspi_indicators import ProfitSPIIndicators

# Import the ProfitSPI SDK
import profitspi_sdk
from profitspi_sdk.api.backtesting_api import BacktestingApi
from profitspi_sdk.api.instruments_api import InstrumentsApi
from profitspi_sdk.api_client import ApiClient
from profitspi_sdk.configuration import Configuration

# User credentials
API_KEY = '-$UBRks}sVHX'
USER_ID = 'jcoffi@gmail.com'

def run_profitspi_backtest(strategy_id=None, test_id=None):
    """
    Run a backtest using ProfitSPI SDK or get an existing test.
    
    Args:
        strategy_id: Optional strategy ID to use
        test_id: Optional test ID to use
        
    Returns:
        Dictionary with backtest results
    """
    print("Running backtest using ProfitSPI SDK...")
    
    # Configure API client
    config = Configuration()
    api_client = ApiClient(config)
    
    # Initialize API instances
    backtesting_api = BacktestingApi(api_client)
    
    try:
        # If strategy_id is not provided, get a default strategy
        if strategy_id is None:
            # Get default strategies
            default_strategies = backtesting_api.backtesting_get_default_strategies(API_KEY, USER_ID)
            
            if not default_strategies:
                print("No default strategies found.")
                return None
            
            print(f"Found {len(default_strategies)} default strategies.")
            
            # Use the first strategy
            if default_strategies:
                strategy = default_strategies[0]
                strategy_id = strategy.strategy_id
                strategy_name = strategy.name if hasattr(strategy, 'name') else "Unknown"
                print(f"Using strategy: {strategy_name} (ID: {strategy_id})")
            else:
                print("No strategies found.")
                return None
        
        # Since we can't access strategy details directly, we'll use some common indicators
        indicators = [
            ('SMA', [20]),
            ('SMA', [50]),
            ('EMA', [20]),
            ('RSI', [14]),
            ('BBANDS', [20, 2]),
            ('MACD', [12, 26, 9])
        ]
        
        print(f"Found {len(indicators)} indicators in the strategy:")
        for indicator, params in indicators:
            param_str = ", ".join(str(p) for p in params)
            print(f"  - {indicator}({param_str})")
        
        # If test_id is not provided, get or create a test
        if test_id is None:
            # Get tests for this strategy
            tests = backtesting_api.backtesting_get_user_strategy_test(strategy_id, API_KEY, USER_ID)
            
            if isinstance(tests, list) and tests:
                # Use the first test
                test = tests[0]
                test_id = test.test_num
                print(f"Using existing test: Test #{test_id}")
            else:
                # Create a new test
                print("No existing tests found. Creating a new test...")
                
                # Get available instruments
                instruments_api = InstrumentsApi(api_client)
                instrument_groups = instruments_api.instruments_get_instrument_groups(API_KEY, USER_ID)
                
                # Use a common stock like AAPL
                symbol = "AAPL"
                
                # Create test parameters
                test_params = {
                    "strategy_id": strategy_id,
                    "api_key": API_KEY,
                    "user_id": USER_ID,
                    "instruments": symbol,
                    "begin_date": (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d'),
                    "end_date": datetime.now().strftime('%Y-%m-%d')
                }
                
                # Create the test
                test_result = backtesting_api.backtesting_post_user_strategy_test(**test_params)
                
                if not test_result or not hasattr(test_result, 'test_num'):
                    print("Failed to create a new test.")
                    return None
                
                test_id = test_result.test_num
                print(f"Created new test: Test #{test_id}")
        
        # Get test details
        test_details = backtesting_api.backtesting_get_user_strategy_test_0(
            id=strategy_id, test=test_id, api_key=API_KEY, user_id=USER_ID
        )
        
        if not test_details:
            print("Failed to get test details.")
            return None
        
        # Get test trades
        test_trades = backtesting_api.backtesting_get_user_strategy_test_trades(
            id=strategy_id, test=test_id, api_key=API_KEY, user_id=USER_ID
        )
        
        # Get test instruments
        instruments = []
        if hasattr(test_details, 'instruments') and test_details.instruments:
            instruments = [instr.strip() for instr in test_details.instruments.split(',')]
        
        # If no instruments found, use a default
        if not instruments:
            instruments = ['AAPL']
        
        # Get date range
        start_date = None
        end_date = None
        if hasattr(test_details, 'begin_date'):
            start_date = test_details.begin_date
        if hasattr(test_details, 'end_date'):
            end_date = test_details.end_date
            
        # If no dates found, use default range
        if not start_date:
            start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
        if not end_date:
            end_date = datetime.now().strftime('%Y-%m-%d')
        
        # Return the results
        return {
            'strategy_id': strategy_id,
            'test_id': test_id,
            'test': test_details,
            'trades': test_trades,
            'indicators': indicators,
            'instruments': instruments,
            'start_date': start_date,
            'end_date': end_date
        }
    
    except Exception as e:
        print(f"Error running ProfitSPI backtest: {e}")
        return None

def fetch_historical_data(symbol, start_date, end_date):
    """
    Fetch historical data for a symbol using yfinance.
    
    Args:
        symbol: Stock symbol
        start_date: Start date
        end_date: End date
        
    Returns:
        DataFrame with OHLCV data
    """
    print(f"Fetching historical data for {symbol} from {start_date} to {end_date}...")
    
    try:
        # Fetch data
        data = yf.download(symbol, start=start_date, end=end_date)
        
        # Reset index to make date a column
        data = data.reset_index()
        
        # Rename columns to lowercase
        data.columns = [col.lower() if isinstance(col, str) else col[0].lower() if isinstance(col, tuple) else str(col).lower() for col in data.columns]
        
        # Convert date column to string for easier comparison
        data['date_str'] = data['date'].dt.strftime('%Y-%m-%d')
        
        print(f"Fetched {len(data)} periods of data")
        print(f"Sample dates: {data['date_str'].iloc[:3].tolist()}")
        
        return data
    except Exception as e:
        print(f"Error fetching historical data: {e}")
        return None

def calculate_indicators(df, indicators):
    """
    Calculate indicators using our implementation.
    
    Args:
        df: DataFrame with OHLCV data
        indicators: List of (indicator_name, parameters) tuples
        
    Returns:
        Dictionary with calculated indicator values
    """
    print("Calculating indicators using our implementation...")
    
    # Initialize our indicator calculator
    indicator_calculator = ProfitSPIIndicators()
    
    # Make sure we have a date_str column
    if 'date_str' not in df.columns:
        print("Error: date_str column not found in DataFrame")
        return None
    
    # Calculate each indicator
    results = {}
    for indicator_name, params in indicators:
        try:
            # Convert indicator name to method name
            method_name = f"_{indicator_name.lower()}"
            
            # Check if we have a method for this indicator
            if hasattr(indicator_calculator, method_name):
                # Call the method with parameters
                result = getattr(indicator_calculator, method_name)(df, *params)
                
                # Add to results
                if isinstance(result, pd.DataFrame):
                    # For indicators that return multiple series
                    for col in result.columns:
                        # Create a DataFrame with date_str column
                        result_df = pd.DataFrame({
                            'value': result[col],
                            'date_str': df['date_str']
                        })
                        results[f"{indicator_name}_{col}"] = result_df
                else:
                    # Create a DataFrame with date_str column
                    result_df = pd.DataFrame({
                        'value': result,
                        'date_str': df['date_str']
                    })
                    results[indicator_name] = result_df
                
                print(f"Calculated {indicator_name} with parameters {params}")
            else:
                print(f"Indicator {indicator_name} not implemented")
        except Exception as e:
            print(f"Error calculating {indicator_name}: {e}")
    
    return results

def extract_profitspi_indicator_values(backtest_results):
    """
    Extract indicator values from ProfitSPI backtest results.
    
    Args:
        backtest_results: Dictionary with backtest results
        
    Returns:
        Dictionary with indicator values at trade entry points
    """
    print("Extracting indicator values from ProfitSPI backtest results...")
    
    # Check if we have trades
    if not backtest_results or 'trades' not in backtest_results or not backtest_results['trades']:
        print("No trades found in backtest results.")
        return None
    
    # Get trades
    trades = backtest_results['trades']
    
    # Check if trades has a 'test_trades' attribute
    if hasattr(trades, 'test_trades'):
        trade_list = trades.test_trades
    elif isinstance(trades, list):
        trade_list = trades
    else:
        print("Unexpected trades format.")
        return None
    
    # Extract indicator values at trade entry points
    indicator_values = []
    
    for trade in trade_list:
        # Get trade details
        if hasattr(trade, 'entry_date'):
            entry_date = trade.entry_date
        elif isinstance(trade, dict) and 'entry_date' in trade:
            entry_date = trade['entry_date']
        else:
            print("Trade has no entry_date attribute.")
            continue
        
        # Add to indicator values
        indicator_values.append({
            'entry_date': entry_date,
            'symbol': trade.instrument if hasattr(trade, 'instrument') else trade.get('instrument', 'Unknown'),
            'entry_price': trade.entry_price if hasattr(trade, 'entry_price') else trade.get('entry_price', 0),
            'exit_price': trade.exit_price if hasattr(trade, 'exit_price') else trade.get('exit_price', 0),
            'profit': trade.trade_profit if hasattr(trade, 'trade_profit') else trade.get('trade_profit', 0)
        })
    
    return indicator_values

def compare_indicators(profitspi_values, our_values, indicators):
    """
    Compare indicator values from ProfitSPI with our calculations.
    
    Args:
        profitspi_values: Dictionary with indicator values from ProfitSPI
        our_values: Dictionary with indicator values from our implementation
        indicators: List of (indicator_name, parameters) tuples
        
    Returns:
        DataFrame with comparison results
    """
    print("Comparing indicator values...")
    
    # Check if we have values to compare
    if not profitspi_values or not our_values:
        print("No values to compare.")
        return None
    
    # Create a comparison DataFrame
    comparison = []
    
    # Get the DataFrame with our values
    first_key = list(our_values.keys())[0]
    df_with_dates = our_values[first_key].reset_index()
    
    # Make sure we have a date_str column
    if 'date_str' not in df_with_dates.columns:
        print("Error: date_str column not found in DataFrame")
        return None
        
    # Get the dates as strings
    our_date_strs = df_with_dates['date_str'].tolist()
    
    for entry in profitspi_values:
        entry_date = entry['entry_date']
        symbol = entry['symbol']
        
        # Convert entry_date to string
        if isinstance(entry_date, datetime):
            entry_date_str = entry_date.strftime('%Y-%m-%d')
        else:
            entry_date_str = str(entry_date)
        
        # Convert entry_date to string in YYYY-MM-DD format
        try:
            if isinstance(entry_date, datetime):
                entry_date_str = entry_date.strftime('%Y-%m-%d')
            else:
                entry_date_str = str(entry_date).split(' ')[0]  # Get just the date part
                
            # Print all our dates for debugging
            print(f"Looking for date: {entry_date_str}")
            print(f"Available dates: {our_date_strs[:5]}...{our_date_strs[-5:]}")
            
            # Check if the date is in our data
            if entry_date_str in our_date_strs:
                print(f"Found exact match for {entry_date_str}")
                
                # Compare indicator values
                for indicator_name, _ in indicators:
                    # Get our value
                    our_value = None
                    if indicator_name in our_values:
                        # Find the row with matching date_str
                        matching_rows = our_values[indicator_name][our_values[indicator_name]['date_str'] == entry_date_str]
                        if not matching_rows.empty:
                            our_value = matching_rows['value'].iloc[0]
                            print(f"Found value for {indicator_name} on {entry_date_str}: {our_value}")
                    
                    # Add to comparison
                    comparison.append({
                        'date': entry_date,
                        'date_str': entry_date_str,
                        'symbol': symbol,
                        'indicator': indicator_name,
                        'our_value': our_value,
                        'entry_price': entry['entry_price'],
                        'exit_price': entry['exit_price'],
                        'profit': entry['profit']
                    })
            else:
                print(f"No match found for {entry_date_str}")
                continue
        except Exception as e:
            print(f"Error matching date {entry_date}: {e}")
            continue
    
    # Convert to DataFrame
    if comparison:
        return pd.DataFrame(comparison)
    else:
        return None

def main():
    # Run a backtest in ProfitSPI
    backtest_results = run_profitspi_backtest()
    
    if not backtest_results:
        print("Failed to run backtest.")
        return
    
    # Save backtest results
    try:
        with open('profitspi_backtest_comparison.json', 'w') as f:
            # Create a custom JSON encoder to handle datetime objects
            class DateTimeEncoder(json.JSONEncoder):
                def default(self, obj):
                    if isinstance(obj, datetime):
                        return obj.isoformat()
                    return super().default(obj)
            
            # Convert objects to dictionaries
            results_dict = {}
            for key, value in backtest_results.items():
                if hasattr(value, 'to_dict'):
                    results_dict[key] = value.to_dict()
                elif isinstance(value, list) and all(hasattr(item, 'to_dict') for item in value if hasattr(item, 'to_dict')):
                    results_dict[key] = [item.to_dict() if hasattr(item, 'to_dict') else item for item in value]
                else:
                    results_dict[key] = value
            
            json.dump(results_dict, f, indent=2, cls=DateTimeEncoder)
        
        print("Saved backtest results to profitspi_backtest_comparison.json")
    except Exception as e:
        print(f"Error saving backtest results: {e}")
    
    # Extract indicator values from ProfitSPI
    profitspi_values = extract_profitspi_indicator_values(backtest_results)
    
    if not profitspi_values:
        print("Failed to extract indicator values from ProfitSPI.")
        return
    
    # Get instruments from trades
    instruments = []
    if 'trades' in backtest_results and backtest_results['trades']:
        trades = backtest_results['trades']
        
        # Check if trades has a 'test_trades' attribute
        if hasattr(trades, 'test_trades'):
            trade_list = trades.test_trades
        elif isinstance(trades, list):
            trade_list = trades
        else:
            trade_list = []
        
        # Extract unique instruments
        for trade in trade_list:
            if hasattr(trade, 'instrument'):
                instruments.append(trade.instrument)
            elif isinstance(trade, dict) and 'instrument' in trade:
                instruments.append(trade['instrument'])
        
        # Remove duplicates
        instruments = list(set(instruments))
    
    # If no instruments found, use the ones from backtest_results
    if not instruments:
        instruments = backtest_results.get('instruments', [])
    
    # Check if we have test results with dates
    if ('test' in backtest_results and 
        hasattr(backtest_results['test'], 'test_results') and 
        hasattr(backtest_results['test'].test_results, 'first_test_date') and 
        hasattr(backtest_results['test'].test_results, 'last_test_date')):
        start_date = backtest_results['test'].test_results.first_test_date
        end_date = backtest_results['test'].test_results.last_test_date
    else:
        start_date = backtest_results['start_date']
        end_date = backtest_results['end_date']
    
    if not instruments:
        print("No instruments found in backtest results.")
        return
    
    # Process each instrument
    all_comparisons = []
    
    for symbol in instruments:
        print(f"\nProcessing instrument: {symbol}")
        
        # Fetch historical data
        df = fetch_historical_data(symbol, start_date, end_date)
        
        if df is None or df.empty:
            print(f"Failed to fetch historical data for {symbol}.")
            continue
        
        # Calculate indicators using our implementation
        our_values = calculate_indicators(df, backtest_results['indicators'])
        
        if not our_values:
            print(f"Failed to calculate indicators for {symbol}.")
            continue
        
        # Filter profitspi_values for this symbol
        symbol_values = [v for v in profitspi_values if v['symbol'] == symbol]
        
        if not symbol_values:
            print(f"No ProfitSPI values found for {symbol}.")
            continue
        
        # Compare indicator values
        comparison = compare_indicators(symbol_values, our_values, backtest_results['indicators'])
        
        if comparison is not None:
            all_comparisons.append(comparison)
    
    # Combine all comparisons
    if all_comparisons:
        comparison = pd.concat(all_comparisons, ignore_index=True)
    else:
        comparison = None
    
    if comparison is not None:
        # Save comparison results
        comparison.to_csv('indicator_comparison.csv', index=False)
        print("Saved comparison results to indicator_comparison.csv")
        
        # Print comparison summary
        print("\nComparison Summary:")
        print(comparison.to_string())
    else:
        print("Failed to compare indicator values.")

if __name__ == "__main__":
    main()