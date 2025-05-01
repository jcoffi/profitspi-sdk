#!/usr/bin/env python3
"""
Script to test all implemented indicators.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta

from profitspi_indicators import ProfitSPIIndicators

def fetch_historical_data(symbol, period="1y", interval="1d"):
    """
    Fetch historical data for a symbol using yfinance.
    
    Args:
        symbol: Stock symbol
        period: Time period to fetch (e.g., "1y", "6mo", "1mo")
        interval: Data interval (e.g., "1d", "1wk", "1mo")
        
    Returns:
        DataFrame with OHLCV data
    """
    print(f"Fetching {period} of {interval} data for {symbol}...")
    
    # Fetch data
    data = yf.download(symbol, period=period, interval=interval)
    
    # Reset index to make date a column
    data = data.reset_index()
    
    # Rename columns to lowercase
    data.columns = [col.lower() if isinstance(col, str) else col[0].lower() if isinstance(col, tuple) else str(col).lower() for col in data.columns]
    
    # Convert date column to string for easier comparison
    data['date_str'] = data['date'].dt.strftime('%Y-%m-%d')
    
    print(f"Fetched {len(data)} periods of data")
    
    return data

def test_all_indicators(symbol="AAPL", period="1y", interval="1d"):
    """
    Test all implemented indicators.
    
    Args:
        symbol: Stock symbol to use for testing
        period: Time period to fetch (e.g., "1y", "6mo", "1mo")
        interval: Data interval (e.g., "1d", "1wk", "1mo")
    """
    # Fetch historical data
    df = fetch_historical_data(symbol, period, interval)
    
    # Fetch market data for beta calculation
    market_df = fetch_historical_data("SPY", period, interval)
    
    # Initialize our indicator calculator
    indicators = ProfitSPIIndicators()
    
    # Create a directory for plots
    os.makedirs("indicator_plots", exist_ok=True)
    
    # List of indicators to test
    indicator_tests = [
        # Moving Averages
        ('SMA', lambda df: indicators._sma(df, 20)),
        ('EMA', lambda df: indicators._ema(df, 20)),
        ('WMA', lambda df: indicators._wma(df, 20)),
        ('TEMA', lambda df: indicators._tema(df, 20)),
        ('TMA', lambda df: indicators._tma(df, 20)),
        
        # Oscillators
        ('RSI', lambda df: indicators._rsi(df, 14)),
        ('Stochastic', lambda df: indicators._stoch(df, 14, 3, 3)),
        ('MACD', lambda df: indicators._macd(df, 12, 26, 9)),
        ('CCI', lambda df: indicators._cci(df, 20)),
        ('Williams %R', lambda df: indicators._williams_r(df, 14)),
        ('Stochastic RSI', lambda df: indicators._stoch_rsi(df, 14, 3, 3, 14)),
        ('Ultimate Oscillator', lambda df: indicators._ultimate_oscillator(df, 7, 14, 28)),
        ('Awesome Oscillator', lambda df: indicators._ao(df, 5, 34)),
        ('Chande Momentum Oscillator', lambda df: indicators._cmo(df, 14)),
        ('PPO', lambda df: indicators._ppo(df, 12, 26, 9)),
        ('DPO', lambda df: indicators._dpo(df, 20)),
        ('TRIX', lambda df: indicators._trix(df, 15)),
        ('Aroon Oscillator', lambda df: indicators._aroon_oscillator(df, 25)),
        ('Fisher Transform', lambda df: indicators._fisher(df, 10)),
        ('SMI', lambda df: indicators._smi(df, 10, 3, 3)),
        ('Fast Stochastic', lambda df: indicators._fast_stochastic(df, 14)),
        ('Slow Stochastic', lambda df: indicators._slow_stochastic(df, 14, 3)),
        ('Full Stochastic', lambda df: indicators._full_stochastic(df, 14, 3, 3)),
        ('Reverse RSI', lambda df: indicators._reverse_rsi(df, 14)),
        ('Cutlers RSI', lambda df: indicators._cutlers_rsi(df, 14)),
        
        # Bands and Channels
        ('Bollinger Bands', lambda df: indicators._bbands(df, 20, 2.0)),
        ('Keltner Channels', lambda df: indicators._keltner(df, 20, 10, 2.0)),
        ('Keltner Channels (Typical)', lambda df: indicators._keltner_typical(df, 20, 1.5)),
        ('Donchian Channels', lambda df: indicators._donchian(df, 20)),
        ('Bollinger Band Width', lambda df: indicators._bbwidth(df, 20, 2.0)),
        ('Bollinger Band %b', lambda df: indicators._bbpercent(df, 20, 2.0)),
        
        # Trend Indicators
        ('ADX', lambda df: indicators._adx(df, 14)),
        ('Aroon', lambda df: indicators._aroon(df, 25)),
        ('Parabolic SAR', lambda df: indicators._parabolic_sar(df, 0.02, 0.02, 0.2)),
        ('Vortex', lambda df: indicators._vortex(df, 14)),
        ('Time Series Forecast', lambda df: indicators._time_series_forecast(df, 14)),
        
        # Volume Indicators
        ('On Balance Volume', lambda df: indicators._obv(df)),
        ('Chaikin Money Flow', lambda df: indicators._cmf(df, 20)),
        ('Chaikin Oscillator', lambda df: indicators._chaikin_oscillator(df, 3, 10)),
        ('Money Flow Index', lambda df: indicators._mfi(df, 14)),
        ('Force Index', lambda df: indicators._force_index(df, 13)),
        ('Ease of Movement', lambda df: indicators._ease_of_movement(df, 14)),
        ('Accumulation Distribution', lambda df: indicators._accumulation_distribution(df)),
        ('Price Volume Trend', lambda df: indicators._price_volume_trend(df)),
        ('Price Volume SMA', lambda df: indicators._price_volume_sma(df, 20)),
        ('Negative Volume Index', lambda df: indicators._negative_volume_index(df)),
        ('Positive Volume Index', lambda df: indicators._positive_volume_index(df)),
        
        # Volatility Indicators
        ('ATR', lambda df: indicators._atr(df, 14)),
        ('Historical Volatility', lambda df: indicators._historical_volatility(df, 20)),
        ('Standard Deviation', lambda df: indicators._standard_deviation(df, 20)),
        ('Chaikin Volatility', lambda df: indicators._chaikin_volatility(df, 10, 10)),
        ('Mass Index', lambda df: indicators._mass_index(df, 25, 9)),
        
        # Price Indicators
        ('Highest High', lambda df: indicators._highest_high(df, 20)),
        ('Lowest Low', lambda df: indicators._lowest_low(df, 20)),
        ('Median Price', lambda df: indicators._median_price(df)),
        ('Typical Price', lambda df: indicators._typical_price(df)),
        ('Weighted Close', lambda df: indicators._weighted_close(df)),
        ('Change', lambda df: indicators._change(df, 1)),
        ('Change %', lambda df: indicators._change_pct(df, 1)),
        ('Percent Difference', lambda df: indicators._percent_difference(df, 1)),
        
        # Statistical Indicators
        ('Beta', lambda df: indicators._beta(df, market_df, 20)),
        ('Correlation', lambda df: indicators._correlation(df, market_df, 20)),
        ('Sharpe Ratio', lambda df: indicators._sharpe_ratio(df, 0.0, 252)),
        ('Sortino Ratio', lambda df: indicators._sortino_ratio(df, 0.0, 252)),
        
        # Other Indicators
        ('ASI', lambda df: indicators._asi(df, 5.0)),
        ('Center of Gravity', lambda df: indicators._center_of_gravity(df, 10)),
        ('Heikin-Ashi', lambda df: indicators._heikin_ashi(df)),
        ('HLC Bars', lambda df: indicators._hlc_bars(df)),
        ('OHLC Bars', lambda df: indicators._ohlc_bars(df))
    ]
    
    # Test each indicator
    results = {}
    for name, func in indicator_tests:
        print(f"Testing {name}...")
        try:
            result = func(df)
            
            # Plot the indicator
            plt.figure(figsize=(12, 6))
            
            # Plot price for reference
            ax1 = plt.gca()
            ax1.plot(df['date'], df['close'], 'k-', alpha=0.3, label='Close Price')
            ax1.set_ylabel('Price')
            
            # Plot the indicator
            if isinstance(result, pd.DataFrame):
                # For indicators that return multiple series
                ax2 = ax1.twinx()
                for col in result.columns:
                    ax2.plot(df['date'], result[col], label=f"{name} - {col}")
                ax2.legend(loc='upper right')
                ax2.set_ylabel('Indicator Value')
            else:
                # For indicators that return a single series
                ax2 = ax1.twinx()
                ax2.plot(df['date'], result, label=name, color='blue')
                ax2.legend(loc='upper right')
                ax2.set_ylabel('Indicator Value')
            
            ax1.legend(loc='upper left')
            plt.title(f"{symbol} - {name}")
            plt.grid(True)
            
            # Save the plot
            plt.savefig(f"indicator_plots/{symbol}_{name.replace(' ', '_').replace('(', '').replace(')', '')}.png")
            plt.close()
            
            # Store the result
            if isinstance(result, pd.DataFrame):
                for col in result.columns:
                    results[f"{name}_{col}"] = result[col]
            else:
                results[name] = result
                
            print(f"  {name} calculated successfully")
        except Exception as e:
            print(f"  Error calculating {name}: {e}")
    
    # Save all results to CSV
    results_df = pd.DataFrame(results)
    results_df['date'] = df['date']
    results_df.to_csv(f"{symbol}_all_indicators.csv", index=False)
    print(f"Saved all indicator values to {symbol}_all_indicators.csv")
    
    return results_df

def main():
    # Test all indicators for multiple symbols
    symbols = ["AAPL", "MSFT", "GOOGL"]
    period = "1y"
    interval = "1d"
    
    for symbol in symbols:
        print(f"\n{'='*50}")
        print(f"Testing all indicators for {symbol}")
        print(f"{'='*50}")
        
        # Test indicators
        test_all_indicators(symbol, period, interval)

if __name__ == "__main__":
    main()