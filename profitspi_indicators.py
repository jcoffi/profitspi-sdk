#!/usr/bin/env python3
"""
Implementation of ProfitSPI indicators based on the API documentation.
This module provides implementations of the technical indicators used by ProfitSPI.
"""

import json
import os
import numpy as np
import pandas as pd
from typing import List, Dict, Union, Optional, Tuple, Any

class ProfitSPIIndicators:
    """
    Class to calculate technical indicators similar to ProfitSPI.
    """
    
    def __init__(self, indicators_file: str = 'indicators.json'):
        """
        Initialize the indicators class.
        
        Args:
            indicators_file: Path to the JSON file containing indicator definitions
        """
        self.indicators = {}
        
        # Load indicator definitions if file exists
        if os.path.exists(indicators_file):
            with open(indicators_file, 'r') as f:
                indicators_data = json.load(f)
                
            # Create a dictionary of indicators by alias
            for indicator in indicators_data:
                self.indicators[indicator['indicator_alias']] = indicator
        
    def calculate(self, df: pd.DataFrame, indicator: str, *args, **kwargs) -> pd.Series:
        """
        Calculate the specified indicator.
        
        Args:
            df: DataFrame with OHLCV data
            indicator: Indicator alias (e.g., 'SMA', 'RSI')
            *args: Positional arguments for the indicator
            **kwargs: Keyword arguments for the indicator
            
        Returns:
            Series with the calculated indicator values
        """
        # Convert indicator to uppercase
        indicator = indicator.upper()
        
        # Check if we have a method for this indicator
        method_name = f"_{indicator.lower()}"
        if hasattr(self, method_name):
            # Call the method
            return getattr(self, method_name)(df, *args, **kwargs)
        else:
            raise ValueError(f"Indicator '{indicator}' not implemented")
    
    def parse_indicator_string(self, indicator_str: str) -> Tuple[str, List[Any]]:
        """
        Parse an indicator string like 'SMA(20)' into name and parameters.
        
        Args:
            indicator_str: String representation of the indicator
            
        Returns:
            Tuple of (indicator_name, parameters)
        """
        # Check if there are parameters
        if '(' in indicator_str and ')' in indicator_str:
            # Split into name and parameters
            name = indicator_str.split('(')[0].strip().upper()
            params_str = indicator_str.split('(')[1].split(')')[0].strip()
            
            # Parse parameters
            if params_str:
                params = [p.strip() for p in params_str.split()]
                # Convert numeric parameters
                params = [float(p) if p.replace('.', '', 1).isdigit() else p for p in params]
                # Convert integers
                params = [int(p) if isinstance(p, float) and p.is_integer() else p for p in params]
            else:
                params = []
                
            return name, params
        else:
            # No parameters
            return indicator_str.strip().upper(), []
    
    def calculate_from_string(self, df: pd.DataFrame, indicator_str: str) -> pd.Series:
        """
        Calculate an indicator from a string representation.
        
        Args:
            df: DataFrame with OHLCV data
            indicator_str: String representation of the indicator (e.g., 'SMA(20)')
            
        Returns:
            Series with the calculated indicator values
        """
        name, params = self.parse_indicator_string(indicator_str)
        return self.calculate(df, name, *params)
    
    # Basic price and volume indicators
    def _open(self, df: pd.DataFrame) -> pd.Series:
        """Open price"""
        return df['open']
    
    def _high(self, df: pd.DataFrame) -> pd.Series:
        """High price"""
        return df['high']
    
    def _low(self, df: pd.DataFrame) -> pd.Series:
        """Low price"""
        return df['low']
    
    def _close(self, df: pd.DataFrame) -> pd.Series:
        """Close price"""
        return df['close']
    
    def _volume(self, df: pd.DataFrame) -> pd.Series:
        """Volume"""
        return df['volume']
    
    # Moving Averages
    def _sma(self, df: pd.DataFrame, period: int = 50, input_column: str = 'close') -> pd.Series:
        """
        Simple Moving Average
        
        Args:
            df: DataFrame with OHLCV data
            period: Number of periods for the moving average
            input_column: Column to use for calculation
            
        Returns:
            Series with SMA values
        """
        return df[input_column].rolling(window=period).mean()
    
    def _ema(self, df: pd.DataFrame, period: int = 20, input_column: str = 'close') -> pd.Series:
        """
        Exponential Moving Average
        
        Args:
            df: DataFrame with OHLCV data
            period: Number of periods for the moving average
            input_column: Column to use for calculation
            
        Returns:
            Series with EMA values
        """
        return df[input_column].ewm(span=period, adjust=False).mean()
    
    def _wma(self, df: pd.DataFrame, period: int = 20, input_column: str = 'close') -> pd.Series:
        """
        Weighted Moving Average
        
        Args:
            df: DataFrame with OHLCV data
            period: Number of periods for the moving average
            input_column: Column to use for calculation
            
        Returns:
            Series with WMA values
        """
        weights = np.arange(1, period + 1)
        return df[input_column].rolling(period).apply(
            lambda x: np.sum(weights * x) / weights.sum(), raw=True)
    
    # Oscillators
    def _rsi(self, df: pd.DataFrame, period: int = 14, input_column: str = 'close') -> pd.Series:
        """
        Relative Strength Index
        
        Args:
            df: DataFrame with OHLCV data
            period: Number of periods for RSI calculation
            input_column: Column to use for calculation
            
        Returns:
            Series with RSI values
        """
        delta = df[input_column].diff()
        
        # Make two series: one for gains, one for losses
        up = delta.clip(lower=0)
        down = -1 * delta.clip(upper=0)
        
        # Calculate the EWMA (Exponential Weighted Moving Average)
        roll_up = up.ewm(com=period-1, adjust=False).mean()
        roll_down = down.ewm(com=period-1, adjust=False).mean()
        
        # Calculate the RSI based on EWMA
        rs = roll_up / roll_down
        rsi = 100.0 - (100.0 / (1.0 + rs))
        
        return rsi
    
    def _macd(self, df: pd.DataFrame, fast_period: int = 12, slow_period: int = 26, 
              signal_period: int = 9, input_column: str = 'close') -> pd.DataFrame:
        """
        Moving Average Convergence Divergence
        
        Args:
            df: DataFrame with OHLCV data
            fast_period: Fast EMA period
            slow_period: Slow EMA period
            signal_period: Signal line period
            input_column: Column to use for calculation
            
        Returns:
            DataFrame with MACD line, signal line, and histogram
        """
        # Calculate the fast and slow EMAs
        fast_ema = df[input_column].ewm(span=fast_period, adjust=False).mean()
        slow_ema = df[input_column].ewm(span=slow_period, adjust=False).mean()
        
        # Calculate the MACD line
        macd_line = fast_ema - slow_ema
        
        # Calculate the signal line
        signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
        
        # Calculate the histogram
        histogram = macd_line - signal_line
        
        # Return all three components
        return pd.DataFrame({
            'macd': macd_line,
            'signal': signal_line,
            'histogram': histogram
        })
    
    def _stoch(self, df: pd.DataFrame, k_period: int = 14, d_period: int = 3, 
               slowing: int = 3) -> pd.DataFrame:
        """
        Stochastic Oscillator
        
        Args:
            df: DataFrame with OHLCV data
            k_period: K period
            d_period: D period
            slowing: Slowing period
            
        Returns:
            DataFrame with %K and %D values
        """
        # Calculate %K
        low_min = df['low'].rolling(window=k_period).min()
        high_max = df['high'].rolling(window=k_period).max()
        
        # Fast %K
        k_fast = 100 * ((df['close'] - low_min) / (high_max - low_min))
        
        # Slow %K (with slowing)
        k = k_fast.rolling(window=slowing).mean()
        
        # %D
        d = k.rolling(window=d_period).mean()
        
        return pd.DataFrame({
            'k': k,
            'd': d
        })
    
    # Volatility Indicators
    def _bbands(self, df: pd.DataFrame, period: int = 20, std_dev: float = 2.0, 
                input_column: str = 'close') -> pd.DataFrame:
        """
        Bollinger Bands
        
        Args:
            df: DataFrame with OHLCV data
            period: Number of periods for the moving average
            std_dev: Number of standard deviations for the bands
            input_column: Column to use for calculation
            
        Returns:
            DataFrame with upper, middle, and lower bands
        """
        # Calculate the middle band (SMA)
        middle_band = df[input_column].rolling(window=period).mean()
        
        # Calculate the standard deviation
        std = df[input_column].rolling(window=period).std()
        
        # Calculate the upper and lower bands
        upper_band = middle_band + (std * std_dev)
        lower_band = middle_band - (std * std_dev)
        
        return pd.DataFrame({
            'upper': upper_band,
            'middle': middle_band,
            'lower': lower_band
        })
    
    def _atr(self, df: pd.DataFrame, period: int = 14) -> pd.Series:
        """
        Average True Range
        
        Args:
            df: DataFrame with OHLCV data
            period: Number of periods for ATR calculation
            
        Returns:
            Series with ATR values
        """
        # Calculate True Range
        high_low = df['high'] - df['low']
        high_close = np.abs(df['high'] - df['close'].shift())
        low_close = np.abs(df['low'] - df['close'].shift())
        
        ranges = pd.concat([high_low, high_close, low_close], axis=1)
        true_range = ranges.max(axis=1)
        
        # Calculate ATR
        atr = true_range.ewm(span=period, adjust=False).mean()
        
        return atr
    
    # Trend Indicators
    def _adx(self, df: pd.DataFrame, period: int = 14) -> pd.DataFrame:
        """
        Average Directional Index
        
        Args:
            df: DataFrame with OHLCV data
            period: Number of periods for ADX calculation
            
        Returns:
            DataFrame with ADX, +DI, and -DI values
        """
        # Calculate True Range
        high_low = df['high'] - df['low']
        high_close = np.abs(df['high'] - df['close'].shift())
        low_close = np.abs(df['low'] - df['close'].shift())
        
        ranges = pd.concat([high_low, high_close, low_close], axis=1)
        true_range = ranges.max(axis=1)
        
        # Calculate Directional Movement
        up_move = df['high'].diff()
        down_move = df['low'].diff().multiply(-1)
        
        # Positive Directional Movement (+DM)
        pos_dm = np.where((up_move > down_move) & (up_move > 0), up_move, 0)
        pos_dm = pd.Series(pos_dm, index=df.index)
        
        # Negative Directional Movement (-DM)
        neg_dm = np.where((down_move > up_move) & (down_move > 0), down_move, 0)
        neg_dm = pd.Series(neg_dm, index=df.index)
        
        # Smooth the True Range and Directional Movement
        atr = true_range.ewm(span=period, adjust=False).mean()
        pos_di = 100 * (pos_dm.ewm(span=period, adjust=False).mean() / atr)
        neg_di = 100 * (neg_dm.ewm(span=period, adjust=False).mean() / atr)
        
        # Calculate the Directional Index
        dx = 100 * np.abs(pos_di - neg_di) / (pos_di + neg_di)
        
        # Calculate the Average Directional Index
        adx = dx.ewm(span=period, adjust=False).mean()
        
        return pd.DataFrame({
            'adx': adx,
            'pos_di': pos_di,
            'neg_di': neg_di
        })
    
    # Volume Indicators
    def _obv(self, df: pd.DataFrame) -> pd.Series:
        """
        On-Balance Volume
        
        Args:
            df: DataFrame with OHLCV data
            
        Returns:
            Series with OBV values
        """
        # Calculate price change direction
        price_change = df['close'].diff()
        
        # Create a Series with the volume values
        obv = pd.Series(index=df.index, dtype=float)
        obv.iloc[0] = 0  # Initialize the first value
        
        # Calculate OBV
        for i in range(1, len(df)):
            if price_change.iloc[i] > 0:
                obv.iloc[i] = obv.iloc[i-1] + df['volume'].iloc[i]
            elif price_change.iloc[i] < 0:
                obv.iloc[i] = obv.iloc[i-1] - df['volume'].iloc[i]
            else:
                obv.iloc[i] = obv.iloc[i-1]
                
        return obv
    
    def _mfi(self, df: pd.DataFrame, period: int = 14) -> pd.Series:
        """
        Money Flow Index
        
        Args:
            df: DataFrame with OHLCV data
            period: Number of periods for MFI calculation
            
        Returns:
            Series with MFI values
        """
        # Calculate typical price
        typical_price = (df['high'] + df['low'] + df['close']) / 3
        
        # Calculate raw money flow
        raw_money_flow = typical_price * df['volume']
        
        # Get the direction of the money flow
        money_flow_direction = np.where(typical_price > typical_price.shift(1), 1, -1)
        money_flow_direction[0] = 0  # Set the first value to neutral
        
        # Calculate positive and negative money flows
        positive_flow = np.where(money_flow_direction > 0, raw_money_flow, 0)
        negative_flow = np.where(money_flow_direction < 0, raw_money_flow, 0)
        
        # Calculate the money flow ratio
        positive_mf = pd.Series(positive_flow).rolling(window=period).sum()
        negative_mf = pd.Series(negative_flow).rolling(window=period).sum()
        
        money_flow_ratio = positive_mf / negative_mf
        
        # Calculate MFI
        mfi = 100 - (100 / (1 + money_flow_ratio))
        
        return mfi
    
    # Custom indicators
    def _bbupper(self, df: pd.DataFrame, period: int = 20, std_dev: float = 2.0, 
                input_column: str = 'close') -> pd.Series:
        """
        Bollinger Band Upper
        
        Args:
            df: DataFrame with OHLCV data
            period: Number of periods for the moving average
            std_dev: Number of standard deviations for the bands
            input_column: Column to use for calculation
            
        Returns:
            Series with upper band values
        """
        bbands = self._bbands(df, period, std_dev, input_column)
        return bbands['upper']
    
    def _bblower(self, df: pd.DataFrame, period: int = 20, std_dev: float = 2.0, 
                input_column: str = 'close') -> pd.Series:
        """
        Bollinger Band Lower
        
        Args:
            df: DataFrame with OHLCV data
            period: Number of periods for the moving average
            std_dev: Number of standard deviations for the bands
            input_column: Column to use for calculation
            
        Returns:
            Series with lower band values
        """
        bbands = self._bbands(df, period, std_dev, input_column)
        return bbands['lower']
    
    def _bbmiddle(self, df: pd.DataFrame, period: int = 20, 
                 input_column: str = 'close') -> pd.Series:
        """
        Bollinger Band Middle (SMA)
        
        Args:
            df: DataFrame with OHLCV data
            period: Number of periods for the moving average
            input_column: Column to use for calculation
            
        Returns:
            Series with middle band values
        """
        return self._sma(df, period, input_column)
    
    def _macdline(self, df: pd.DataFrame, fast_period: int = 12, slow_period: int = 26,
                 input_column: str = 'close') -> pd.Series:
        """
        MACD Line
        
        Args:
            df: DataFrame with OHLCV data
            fast_period: Fast EMA period
            slow_period: Slow EMA period
            input_column: Column to use for calculation
            
        Returns:
            Series with MACD line values
        """
        macd = self._macd(df, fast_period, slow_period, 9, input_column)
        return macd['macd']
    
    def _macdsignal(self, df: pd.DataFrame, fast_period: int = 12, slow_period: int = 26,
                   signal_period: int = 9, input_column: str = 'close') -> pd.Series:
        """
        MACD Signal Line
        
        Args:
            df: DataFrame with OHLCV data
            fast_period: Fast EMA period
            slow_period: Slow EMA period
            signal_period: Signal line period
            input_column: Column to use for calculation
            
        Returns:
            Series with MACD signal line values
        """
        macd = self._macd(df, fast_period, slow_period, signal_period, input_column)
        return macd['signal']
    
    def _macdhist(self, df: pd.DataFrame, fast_period: int = 12, slow_period: int = 26,
                 signal_period: int = 9, input_column: str = 'close') -> pd.Series:
        """
        MACD Histogram
        
        Args:
            df: DataFrame with OHLCV data
            fast_period: Fast EMA period
            slow_period: Slow EMA period
            signal_period: Signal line period
            input_column: Column to use for calculation
            
        Returns:
            Series with MACD histogram values
        """
        macd = self._macd(df, fast_period, slow_period, signal_period, input_column)
        return macd['histogram']
    
    def _stochk(self, df: pd.DataFrame, k_period: int = 14, d_period: int = 3,
               slowing: int = 3) -> pd.Series:
        """
        Stochastic %K
        
        Args:
            df: DataFrame with OHLCV data
            k_period: K period
            d_period: D period
            slowing: Slowing period
            
        Returns:
            Series with %K values
        """
        stoch = self._stoch(df, k_period, d_period, slowing)
        return stoch['k']
    
    def _stochd(self, df: pd.DataFrame, k_period: int = 14, d_period: int = 3,
               slowing: int = 3) -> pd.Series:
        """
        Stochastic %D
        
        Args:
            df: DataFrame with OHLCV data
            k_period: K period
            d_period: D period
            slowing: Slowing period
            
        Returns:
            Series with %D values
        """
        stoch = self._stoch(df, k_period, d_period, slowing)
        return stoch['d']
    
    # Complex indicators
    def _keltner(self, df: pd.DataFrame, ema_period: int = 20, atr_period: int = 10, 
                multiplier: float = 2.0) -> pd.DataFrame:
        """
        Keltner Channels using EMA and ATR
        
        Args:
            df: DataFrame with OHLCV data
            ema_period: Period for the EMA calculation
            atr_period: Period for the ATR calculation
            multiplier: Multiplier for the ATR
            
        Returns:
            DataFrame with upper, middle, and lower bands
        """
        # Calculate the middle band (EMA)
        middle_band = self._ema(df, ema_period)
        
        # Calculate the ATR
        atr = self._atr(df, atr_period)
        
        # Calculate the upper and lower bands
        upper_band = middle_band + (atr * multiplier)
        lower_band = middle_band - (atr * multiplier)
        
        return pd.DataFrame({
            'upper': upper_band,
            'middle': middle_band,
            'lower': lower_band
        })
    
    def _keltner_typical(self, df: pd.DataFrame, period: int = 20, multiplier: float = 1.5) -> pd.DataFrame:
        """
        Keltner Channels using Typical Price and High/Low
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the SMA calculation
            multiplier: Multiplier for the range
            
        Returns:
            DataFrame with upper, middle, and lower bands
        """
        # Calculate typical price
        typical_price = (df['high'] + df['low'] + df['close']) / 3
        
        # Calculate the middle band (SMA of typical price)
        middle_band = typical_price.rolling(window=period).mean()
        
        # Calculate the range
        price_range = df['high'].rolling(window=period).mean() - df['low'].rolling(window=period).mean()
        
        # Calculate the upper and lower bands
        upper_band = middle_band + (price_range * multiplier)
        lower_band = middle_band - (price_range * multiplier)
        
        return pd.DataFrame({
            'upper': upper_band,
            'middle': middle_band,
            'lower': lower_band
        })
    
    def _donchian(self, df: pd.DataFrame, period: int = 20) -> pd.DataFrame:
        """
        Donchian Channels
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the channel calculation
            
        Returns:
            DataFrame with upper, middle, and lower bands
        """
        # Calculate the upper band (highest high)
        upper_band = df['high'].rolling(window=period).max()
        
        # Calculate the lower band (lowest low)
        lower_band = df['low'].rolling(window=period).min()
        
        # Calculate the middle band
        middle_band = (upper_band + lower_band) / 2
        
        return pd.DataFrame({
            'upper': upper_band,
            'middle': middle_band,
            'lower': lower_band
        })
    
    def _stoch_rsi(self, df: pd.DataFrame, period: int = 14, smooth_k: int = 3, 
                  smooth_d: int = 3, rsi_period: int = 14) -> pd.DataFrame:
        """
        Stochastic RSI
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the Stochastic calculation
            smooth_k: Smoothing for %K
            smooth_d: Smoothing for %D
            rsi_period: Period for the RSI calculation
            
        Returns:
            DataFrame with %K and %D values
        """
        # Calculate RSI
        rsi = self._rsi(df, rsi_period)
        
        # Calculate Stochastic RSI
        stoch_rsi = pd.Series(index=df.index, dtype=float)
        
        # Calculate %K
        for i in range(period, len(rsi)):
            rsi_window = rsi.iloc[i-period+1:i+1]
            if rsi_window.max() - rsi_window.min() != 0:
                stoch_rsi.iloc[i] = (rsi.iloc[i] - rsi_window.min()) / (rsi_window.max() - rsi_window.min())
            else:
                stoch_rsi.iloc[i] = 0
        
        # Smooth %K
        k = stoch_rsi.rolling(window=smooth_k).mean() * 100
        
        # Calculate %D
        d = k.rolling(window=smooth_d).mean()
        
        return pd.DataFrame({
            'k': k,
            'k_raw': stoch_rsi * 100,
            'd': d
        })
    
    def _williams_r(self, df: pd.DataFrame, period: int = 14) -> pd.Series:
        """
        Williams %R
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the Williams %R calculation
            
        Returns:
            Series with Williams %R values
        """
        # Calculate highest high and lowest low
        highest_high = df['high'].rolling(window=period).max()
        lowest_low = df['low'].rolling(window=period).min()
        
        # Calculate Williams %R
        williams_r = -100 * ((highest_high - df['close']) / (highest_high - lowest_low))
        
        return williams_r
    
    def _cci(self, df: pd.DataFrame, period: int = 20, constant: float = 0.015) -> pd.Series:
        """
        Commodity Channel Index
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the CCI calculation
            constant: Constant multiplier
            
        Returns:
            Series with CCI values
        """
        # Calculate typical price
        typical_price = (df['high'] + df['low'] + df['close']) / 3
        
        # Calculate the SMA of typical price
        tp_sma = typical_price.rolling(window=period).mean()
        
        # Calculate the mean deviation
        mean_deviation = pd.Series(index=df.index, dtype=float)
        for i in range(period-1, len(typical_price)):
            mean_deviation.iloc[i] = np.mean(np.abs(typical_price.iloc[i-period+1:i+1] - tp_sma.iloc[i]))
        
        # Calculate CCI
        cci = (typical_price - tp_sma) / (constant * mean_deviation)
        
        return cci
    
    def _aroon(self, df: pd.DataFrame, period: int = 25) -> pd.DataFrame:
        """
        Aroon Indicator
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the Aroon calculation
            
        Returns:
            DataFrame with Aroon Up and Aroon Down values
        """
        # Initialize Aroon Up and Aroon Down series
        aroon_up = pd.Series(index=df.index, dtype=float)
        aroon_down = pd.Series(index=df.index, dtype=float)
        
        # Calculate Aroon Up and Aroon Down
        for i in range(period, len(df)):
            # Get the window
            high_window = df['high'].iloc[i-period+1:i+1]
            low_window = df['low'].iloc[i-period+1:i+1]
            
            # Find the indices of the highest high and lowest low
            high_idx = high_window.idxmax()
            low_idx = low_window.idxmin()
            
            # Calculate the number of periods since the highest high and lowest low
            periods_since_high = period - (high_window.index.get_loc(high_idx) + 1)
            periods_since_low = period - (low_window.index.get_loc(low_idx) + 1)
            
            # Calculate Aroon Up and Aroon Down
            aroon_up.iloc[i] = 100 * (period - periods_since_high) / period
            aroon_down.iloc[i] = 100 * (period - periods_since_low) / period
        
        return pd.DataFrame({
            'up': aroon_up,
            'down': aroon_down
        })
    
    def _aroon_oscillator(self, df: pd.DataFrame, period: int = 25) -> pd.Series:
        """
        Aroon Oscillator
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the Aroon calculation
            
        Returns:
            Series with Aroon Oscillator values
        """
        # Calculate Aroon Up and Aroon Down
        aroon = self._aroon(df, period)
        
        # Calculate Aroon Oscillator
        aroon_osc = aroon['up'] - aroon['down']
        
        return aroon_osc
    
    def _parabolic_sar(self, df: pd.DataFrame, af_start: float = 0.02, af_increment: float = 0.02, 
                      af_max: float = 0.2) -> pd.Series:
        """
        Parabolic SAR
        
        Args:
            df: DataFrame with OHLCV data
            af_start: Starting acceleration factor
            af_increment: Acceleration factor increment
            af_max: Maximum acceleration factor
            
        Returns:
            Series with Parabolic SAR values
        """
        # Initialize variables
        sar = pd.Series(index=df.index, dtype=float)
        trend = pd.Series(index=df.index, dtype=int)  # 1 for uptrend, -1 for downtrend
        ep = pd.Series(index=df.index, dtype=float)  # Extreme point
        af = pd.Series(index=df.index, dtype=float)  # Acceleration factor
        
        # Initialize the first two periods
        if df['close'].iloc[0] < df['close'].iloc[1]:
            # Initial uptrend
            trend.iloc[0] = 1
            trend.iloc[1] = 1
            sar.iloc[0] = df['low'].iloc[0]
            sar.iloc[1] = min(df['low'].iloc[0], df['low'].iloc[1])
            ep.iloc[1] = df['high'].iloc[1]
            af.iloc[1] = af_start
        else:
            # Initial downtrend
            trend.iloc[0] = -1
            trend.iloc[1] = -1
            sar.iloc[0] = df['high'].iloc[0]
            sar.iloc[1] = max(df['high'].iloc[0], df['high'].iloc[1])
            ep.iloc[1] = df['low'].iloc[1]
            af.iloc[1] = af_start
        
        # Calculate SAR for the rest of the periods
        for i in range(2, len(df)):
            # Previous trend
            prev_trend = trend.iloc[i-1]
            
            # Calculate SAR
            sar.iloc[i] = sar.iloc[i-1] + af.iloc[i-1] * (ep.iloc[i-1] - sar.iloc[i-1])
            
            # Check for trend reversal
            if prev_trend == 1:  # Previous uptrend
                # Check if current price is below SAR
                if df['low'].iloc[i] < sar.iloc[i]:
                    # Trend reversal to downtrend
                    trend.iloc[i] = -1
                    sar.iloc[i] = max(ep.iloc[i-1], df['high'].iloc[i])
                    ep.iloc[i] = df['low'].iloc[i]
                    af.iloc[i] = af_start
                else:
                    # Continue uptrend
                    trend.iloc[i] = 1
                    # Ensure SAR is below the previous two lows
                    sar.iloc[i] = min(sar.iloc[i], df['low'].iloc[i-1], df['low'].iloc[i-2])
                    # Update extreme point if needed
                    if df['high'].iloc[i] > ep.iloc[i-1]:
                        ep.iloc[i] = df['high'].iloc[i]
                        af.iloc[i] = min(af.iloc[i-1] + af_increment, af_max)
                    else:
                        ep.iloc[i] = ep.iloc[i-1]
                        af.iloc[i] = af.iloc[i-1]
            else:  # Previous downtrend
                # Check if current price is above SAR
                if df['high'].iloc[i] > sar.iloc[i]:
                    # Trend reversal to uptrend
                    trend.iloc[i] = 1
                    sar.iloc[i] = min(ep.iloc[i-1], df['low'].iloc[i])
                    ep.iloc[i] = df['high'].iloc[i]
                    af.iloc[i] = af_start
                else:
                    # Continue downtrend
                    trend.iloc[i] = -1
                    # Ensure SAR is above the previous two highs
                    sar.iloc[i] = max(sar.iloc[i], df['high'].iloc[i-1], df['high'].iloc[i-2])
                    # Update extreme point if needed
                    if df['low'].iloc[i] < ep.iloc[i-1]:
                        ep.iloc[i] = df['low'].iloc[i]
                        af.iloc[i] = min(af.iloc[i-1] + af_increment, af_max)
                    else:
                        ep.iloc[i] = ep.iloc[i-1]
                        af.iloc[i] = af.iloc[i-1]
        
        return sar
    
    def _cmf(self, df: pd.DataFrame, period: int = 20) -> pd.Series:
        """
        Chaikin Money Flow
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the CMF calculation
            
        Returns:
            Series with CMF values
        """
        # Calculate Money Flow Multiplier
        high_low_range = df['high'] - df['low']
        money_flow_multiplier = ((df['close'] - df['low']) - (df['high'] - df['close'])) / high_low_range
        money_flow_multiplier = money_flow_multiplier.replace([np.inf, -np.inf], 0)
        
        # Calculate Money Flow Volume
        money_flow_volume = money_flow_multiplier * df['volume']
        
        # Calculate Chaikin Money Flow
        cmf = money_flow_volume.rolling(window=period).sum() / df['volume'].rolling(window=period).sum()
        
        return cmf
    
    def _chaikin_oscillator(self, df: pd.DataFrame, fast_period: int = 3, slow_period: int = 10) -> pd.Series:
        """
        Chaikin Oscillator
        
        Args:
            df: DataFrame with OHLCV data
            fast_period: Fast EMA period
            slow_period: Slow EMA period
            
        Returns:
            Series with Chaikin Oscillator values
        """
        # Calculate Money Flow Multiplier
        high_low_range = df['high'] - df['low']
        money_flow_multiplier = ((df['close'] - df['low']) - (df['high'] - df['close'])) / high_low_range
        money_flow_multiplier = money_flow_multiplier.replace([np.inf, -np.inf], 0)
        
        # Calculate Money Flow Volume
        money_flow_volume = money_flow_multiplier * df['volume']
        
        # Calculate Accumulation/Distribution Line
        adl = money_flow_volume.cumsum()
        
        # Calculate Chaikin Oscillator
        fast_ema = adl.ewm(span=fast_period, adjust=False).mean()
        slow_ema = adl.ewm(span=slow_period, adjust=False).mean()
        chaikin_osc = fast_ema - slow_ema
        
        return chaikin_osc
    
    def _trix(self, df: pd.DataFrame, period: int = 15, input_column: str = 'close') -> pd.Series:
        """
        TRIX
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the EMA calculations
            input_column: Column to use for calculation
            
        Returns:
            Series with TRIX values
        """
        # Calculate Triple EMA
        ema1 = df[input_column].ewm(span=period, adjust=False).mean()
        ema2 = ema1.ewm(span=period, adjust=False).mean()
        ema3 = ema2.ewm(span=period, adjust=False).mean()
        
        # Calculate TRIX
        trix = 100 * (ema3.pct_change(1))
        
        return trix
    
    def _tema(self, df: pd.DataFrame, period: int = 20, input_column: str = 'close') -> pd.Series:
        """
        Triple Exponential Moving Average
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the EMA calculations
            input_column: Column to use for calculation
            
        Returns:
            Series with TEMA values
        """
        # Calculate EMAs
        ema1 = df[input_column].ewm(span=period, adjust=False).mean()
        ema2 = ema1.ewm(span=period, adjust=False).mean()
        ema3 = ema2.ewm(span=period, adjust=False).mean()
        
        # Calculate TEMA
        tema = 3 * ema1 - 3 * ema2 + ema3
        
        return tema
    
    def _tma(self, df: pd.DataFrame, period: int = 20, input_column: str = 'close') -> pd.Series:
        """
        Triangular Moving Average
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the TMA calculation
            input_column: Column to use for calculation
            
        Returns:
            Series with TMA values
        """
        # Calculate the first SMA
        n1 = (period + 1) // 2
        sma1 = df[input_column].rolling(window=n1).mean()
        
        # Calculate the TMA (SMA of the first SMA)
        tma = sma1.rolling(window=n1).mean()
        
        return tma
    
    def _vortex(self, df: pd.DataFrame, period: int = 14) -> pd.DataFrame:
        """
        Vortex Indicator
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the Vortex calculation
            
        Returns:
            DataFrame with positive and negative Vortex values
        """
        # Calculate True Range
        high_low = df['high'] - df['low']
        high_close = np.abs(df['high'] - df['close'].shift())
        low_close = np.abs(df['low'] - df['close'].shift())
        
        ranges = pd.concat([high_low, high_close, low_close], axis=1)
        true_range = ranges.max(axis=1)
        
        # Calculate VM+
        vm_plus = np.abs(df['high'] - df['low'].shift())
        
        # Calculate VM-
        vm_minus = np.abs(df['low'] - df['high'].shift())
        
        # Calculate the sum over the period
        tr_sum = true_range.rolling(window=period).sum()
        vm_plus_sum = vm_plus.rolling(window=period).sum()
        vm_minus_sum = vm_minus.rolling(window=period).sum()
        
        # Calculate VI+ and VI-
        vi_plus = vm_plus_sum / tr_sum
        vi_minus = vm_minus_sum / tr_sum
        
        return pd.DataFrame({
            'plus': vi_plus,
            'minus': vi_minus
        })
    
    def _ultimate_oscillator(self, df: pd.DataFrame, period1: int = 7, period2: int = 14, 
                           period3: int = 28, weights: list = [4, 2, 1]) -> pd.Series:
        """
        Ultimate Oscillator
        
        Args:
            df: DataFrame with OHLCV data
            period1: First period
            period2: Second period
            period3: Third period
            weights: Weights for the three periods
            
        Returns:
            Series with Ultimate Oscillator values
        """
        # Calculate buying pressure
        buying_pressure = df['close'] - pd.Series(
            [min(low, close) for low, close in zip(df['low'], df['close'].shift(1))],
            index=df.index
        )
        
        # Calculate true range
        high_low = df['high'] - df['low']
        high_close = np.abs(df['high'] - df['close'].shift())
        low_close = np.abs(df['low'] - df['close'].shift())
        
        ranges = pd.concat([high_low, high_close, low_close], axis=1)
        true_range = ranges.max(axis=1)
        
        # Calculate average buying pressure and average true range for each period
        avg_bp1 = buying_pressure.rolling(window=period1).sum()
        avg_tr1 = true_range.rolling(window=period1).sum()
        
        avg_bp2 = buying_pressure.rolling(window=period2).sum()
        avg_tr2 = true_range.rolling(window=period2).sum()
        
        avg_bp3 = buying_pressure.rolling(window=period3).sum()
        avg_tr3 = true_range.rolling(window=period3).sum()
        
        # Calculate the raw values
        raw1 = avg_bp1 / avg_tr1
        raw2 = avg_bp2 / avg_tr2
        raw3 = avg_bp3 / avg_tr3
        
        # Calculate the Ultimate Oscillator
        uo = 100 * (weights[0] * raw1 + weights[1] * raw2 + weights[2] * raw3) / sum(weights)
        
        return uo
    
    def _ppo(self, df: pd.DataFrame, fast_period: int = 12, slow_period: int = 26, 
            signal_period: int = 9, input_column: str = 'close') -> pd.DataFrame:
        """
        Percentage Price Oscillator
        
        Args:
            df: DataFrame with OHLCV data
            fast_period: Fast EMA period
            slow_period: Slow EMA period
            signal_period: Signal line period
            input_column: Column to use for calculation
            
        Returns:
            DataFrame with PPO line, signal line, and histogram
        """
        # Calculate the fast and slow EMAs
        fast_ema = df[input_column].ewm(span=fast_period, adjust=False).mean()
        slow_ema = df[input_column].ewm(span=slow_period, adjust=False).mean()
        
        # Calculate the PPO line (percentage difference between fast and slow EMAs)
        ppo_line = 100 * (fast_ema - slow_ema) / slow_ema
        
        # Calculate the signal line
        signal_line = ppo_line.ewm(span=signal_period, adjust=False).mean()
        
        # Calculate the histogram
        histogram = ppo_line - signal_line
        
        # Return all three components
        return pd.DataFrame({
            'ppo': ppo_line,
            'signal': signal_line,
            'histogram': histogram
        })
    
    def _dpo(self, df: pd.DataFrame, period: int = 20, input_column: str = 'close') -> pd.Series:
        """
        Detrended Price Oscillator
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the calculation
            input_column: Column to use for calculation
            
        Returns:
            Series with DPO values
        """
        # Calculate the shifted SMA
        shifted_period = period // 2 + 1
        sma = df[input_column].rolling(window=period).mean().shift(shifted_period)
        
        # Calculate DPO
        dpo = df[input_column] - sma
        
        return dpo
    
    def _fisher(self, df: pd.DataFrame, period: int = 10) -> pd.DataFrame:
        """
        Fisher Transform
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the calculation
            
        Returns:
            DataFrame with Fisher Transform and its signal line
        """
        # Calculate the median price
        median_price = (df['high'] + df['low']) / 2
        
        # Calculate the normalized price (between -1 and 1)
        highest_high = median_price.rolling(window=period).max()
        lowest_low = median_price.rolling(window=period).min()
        normalized_price = pd.Series(index=df.index, dtype=float)
        
        for i in range(period, len(df)):
            price_range = highest_high.iloc[i] - lowest_low.iloc[i]
            if price_range != 0:
                normalized_price.iloc[i] = 2 * ((median_price.iloc[i] - lowest_low.iloc[i]) / price_range - 0.5)
            else:
                normalized_price.iloc[i] = 0
        
        # Apply the Fisher Transform
        fisher = pd.Series(index=df.index, dtype=float)
        fisher_prev = pd.Series(index=df.index, dtype=float)
        
        for i in range(period, len(df)):
            if i > period:
                fisher_prev.iloc[i] = fisher.iloc[i-1]
            else:
                fisher_prev.iloc[i] = 0
                
            # Ensure normalized_price is within bounds to avoid numerical issues
            np_value = max(min(normalized_price.iloc[i], 0.999), -0.999)
            
            # Apply the Fisher Transform formula
            fisher.iloc[i] = 0.5 * np.log((1 + np_value) / (1 - np_value)) + 0.5 * fisher_prev.iloc[i]
        
        # Calculate the signal line (1-period lag)
        signal = fisher.shift(1)
        
        return pd.DataFrame({
            'fisher': fisher,
            'signal': signal
        })
    
    def _cmo(self, df: pd.DataFrame, period: int = 14, input_column: str = 'close') -> pd.Series:
        """
        Chande Momentum Oscillator
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the calculation
            input_column: Column to use for calculation
            
        Returns:
            Series with CMO values
        """
        # Calculate price changes
        delta = df[input_column].diff()
        
        # Separate up and down movements
        up = delta.copy()
        down = delta.copy()
        up[up < 0] = 0
        down[down > 0] = 0
        down = abs(down)
        
        # Calculate the sum of up and down movements over the period
        up_sum = up.rolling(window=period).sum()
        down_sum = down.rolling(window=period).sum()
        
        # Calculate CMO
        cmo = 100 * (up_sum - down_sum) / (up_sum + down_sum)
        
        return cmo
    
    def _cci(self, df: pd.DataFrame, period: int = 20, constant: float = 0.015) -> pd.Series:
        """
        Commodity Channel Index
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the CCI calculation
            constant: Constant multiplier
            
        Returns:
            Series with CCI values
        """
        # Calculate typical price
        typical_price = (df['high'] + df['low'] + df['close']) / 3
        
        # Calculate the SMA of typical price
        tp_sma = typical_price.rolling(window=period).mean()
        
        # Calculate the mean deviation
        mean_deviation = pd.Series(index=df.index, dtype=float)
        for i in range(period-1, len(typical_price)):
            mean_deviation.iloc[i] = np.mean(np.abs(typical_price.iloc[i-period+1:i+1] - tp_sma.iloc[i]))
        
        # Calculate CCI
        cci = (typical_price - tp_sma) / (constant * mean_deviation)
        
        return cci
    
    def _williams_r(self, df: pd.DataFrame, period: int = 14) -> pd.Series:
        """
        Williams %R
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the Williams %R calculation
            
        Returns:
            Series with Williams %R values
        """
        # Calculate highest high and lowest low
        highest_high = df['high'].rolling(window=period).max()
        lowest_low = df['low'].rolling(window=period).min()
        
        # Calculate Williams %R
        williams_r = -100 * ((highest_high - df['close']) / (highest_high - lowest_low))
        
        return williams_r
    
    def _ao(self, df: pd.DataFrame, fast_period: int = 5, slow_period: int = 34) -> pd.Series:
        """
        Awesome Oscillator
        
        Args:
            df: DataFrame with OHLCV data
            fast_period: Fast SMA period
            slow_period: Slow SMA period
            
        Returns:
            Series with Awesome Oscillator values
        """
        # Calculate median price
        median_price = (df['high'] + df['low']) / 2
        
        # Calculate the fast and slow SMAs
        fast_sma = median_price.rolling(window=fast_period).mean()
        slow_sma = median_price.rolling(window=slow_period).mean()
        
        # Calculate Awesome Oscillator
        ao = fast_sma - slow_sma
        
        return ao
    
    def _force_index(self, df: pd.DataFrame, period: int = 13) -> pd.Series:
        """
        Force Index
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the EMA smoothing
            
        Returns:
            Series with Force Index values
        """
        # Calculate the raw Force Index
        raw_fi = df['volume'] * df['close'].diff()
        
        # Apply EMA smoothing
        fi = raw_fi.ewm(span=period, adjust=False).mean()
        
        return fi
    
    def _mass_index(self, df: pd.DataFrame, period: int = 25, ema_period: int = 9) -> pd.Series:
        """
        Mass Index
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the Mass Index calculation
            ema_period: Period for the EMAs
            
        Returns:
            Series with Mass Index values
        """
        # Calculate high-low range
        high_low_range = df['high'] - df['low']
        
        # Calculate the single and double EMAs of the range
        ema1 = high_low_range.ewm(span=ema_period, adjust=False).mean()
        ema2 = ema1.ewm(span=ema_period, adjust=False).mean()
        
        # Calculate the ratio of EMAs
        ema_ratio = ema1 / ema2
        
        # Calculate the Mass Index
        mass_index = ema_ratio.rolling(window=period).sum()
        
        return mass_index
    
    def _chaikin_volatility(self, df: pd.DataFrame, period: int = 10, rate_of_change: int = 10) -> pd.Series:
        """
        Chaikin Volatility
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the EMA calculation
            rate_of_change: Period for the rate of change calculation
            
        Returns:
            Series with Chaikin Volatility values
        """
        # Calculate high-low range
        high_low_range = df['high'] - df['low']
        
        # Calculate the EMA of the range
        ema_range = high_low_range.ewm(span=period, adjust=False).mean()
        
        # Calculate the rate of change
        chaikin_vol = 100 * (ema_range - ema_range.shift(rate_of_change)) / ema_range.shift(rate_of_change)
        
        return chaikin_vol
    
    def _ease_of_movement(self, df: pd.DataFrame, period: int = 14) -> pd.Series:
        """
        Ease of Movement
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the SMA calculation
            
        Returns:
            Series with Ease of Movement values
        """
        # Calculate the distance moved
        distance_moved = (df['high'] + df['low']) / 2 - (df['high'].shift(1) + df['low'].shift(1)) / 2
        
        # Calculate the box ratio
        box_ratio = (df['volume'] / 1000000) / (df['high'] - df['low'])
        
        # Calculate the raw Ease of Movement
        raw_eom = distance_moved / box_ratio
        
        # Apply SMA smoothing
        eom = raw_eom.rolling(window=period).mean()
        
        return eom
    
    def _typical_price(self, df: pd.DataFrame) -> pd.Series:
        """
        Typical Price
        
        Args:
            df: DataFrame with OHLCV data
            
        Returns:
            Series with Typical Price values
        """
        return (df['high'] + df['low'] + df['close']) / 3
    
    def _weighted_close(self, df: pd.DataFrame) -> pd.Series:
        """
        Weighted Close
        
        Args:
            df: DataFrame with OHLCV data
            
        Returns:
            Series with Weighted Close values
        """
        return (df['high'] + df['low'] + df['close'] * 2) / 4
    
    def _median_price(self, df: pd.DataFrame) -> pd.Series:
        """
        Median Price
        
        Args:
            df: DataFrame with OHLCV data
            
        Returns:
            Series with Median Price values
        """
        return (df['high'] + df['low']) / 2
    
    def _price_volume_trend(self, df: pd.DataFrame) -> pd.Series:
        """
        Price Volume Trend
        
        Args:
            df: DataFrame with OHLCV data
            
        Returns:
            Series with Price Volume Trend values
        """
        # Calculate percentage price change
        price_change_pct = df['close'].pct_change()
        
        # Calculate Price Volume Trend
        pvt = (price_change_pct * df['volume']).cumsum()
        
        return pvt
    
    def _price_volume_sma(self, df: pd.DataFrame, period: int = 20) -> pd.Series:
        """
        Price times Volume SMA
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the SMA calculation
            
        Returns:
            Series with Price times Volume SMA values
        """
        # Calculate price times volume
        price_volume = df['close'] * df['volume']
        
        # Calculate SMA
        pv_sma = price_volume.rolling(window=period).mean()
        
        return pv_sma
    
    def _negative_volume_index(self, df: pd.DataFrame) -> pd.Series:
        """
        Negative Volume Index
        
        Args:
            df: DataFrame with OHLCV data
            
        Returns:
            Series with Negative Volume Index values
        """
        # Calculate percentage price change
        price_change_pct = df['close'].pct_change()
        
        # Calculate volume change
        volume_change = df['volume'].pct_change()
        
        # Initialize NVI with 1000
        nvi = pd.Series(1000, index=df.index)
        
        # Calculate NVI
        for i in range(1, len(df)):
            if volume_change.iloc[i] < 0:
                nvi.iloc[i] = nvi.iloc[i-1] * (1 + price_change_pct.iloc[i])
            else:
                nvi.iloc[i] = nvi.iloc[i-1]
        
        return nvi
    
    def _positive_volume_index(self, df: pd.DataFrame) -> pd.Series:
        """
        Positive Volume Index
        
        Args:
            df: DataFrame with OHLCV data
            
        Returns:
            Series with Positive Volume Index values
        """
        # Calculate percentage price change
        price_change_pct = df['close'].pct_change()
        
        # Calculate volume change
        volume_change = df['volume'].pct_change()
        
        # Initialize PVI with 1000
        pvi = pd.Series(1000, index=df.index)
        
        # Calculate PVI
        for i in range(1, len(df)):
            if volume_change.iloc[i] > 0:
                pvi.iloc[i] = pvi.iloc[i-1] * (1 + price_change_pct.iloc[i])
            else:
                pvi.iloc[i] = pvi.iloc[i-1]
        
        return pvi
    
    def _historical_volatility(self, df: pd.DataFrame, period: int = 20) -> pd.Series:
        """
        Historical Volatility
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the calculation
            
        Returns:
            Series with Historical Volatility values
        """
        # Calculate log returns
        log_returns = np.log(df['close'] / df['close'].shift(1))
        
        # Calculate standard deviation of log returns
        volatility = log_returns.rolling(window=period).std() * np.sqrt(252)  # Annualized
        
        return volatility * 100  # Convert to percentage
    
    def _standard_deviation(self, df: pd.DataFrame, period: int = 20, input_column: str = 'close') -> pd.Series:
        """
        Standard Deviation
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the calculation
            input_column: Column to use for calculation
            
        Returns:
            Series with Standard Deviation values
        """
        return df[input_column].rolling(window=period).std()
    
    def _percent_difference(self, df: pd.DataFrame, period: int = 1, input_column: str = 'close') -> pd.Series:
        """
        Percent Difference
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the calculation
            input_column: Column to use for calculation
            
        Returns:
            Series with Percent Difference values
        """
        return df[input_column].pct_change(periods=period) * 100
    
    def _change(self, df: pd.DataFrame, period: int = 1, input_column: str = 'close') -> pd.Series:
        """
        Change
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the calculation
            input_column: Column to use for calculation
            
        Returns:
            Series with Change values
        """
        return df[input_column].diff(periods=period)
    
    def _change_pct(self, df: pd.DataFrame, period: int = 1, input_column: str = 'close') -> pd.Series:
        """
        Change %
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the calculation
            input_column: Column to use for calculation
            
        Returns:
            Series with Change % values
        """
        return df[input_column].pct_change(periods=period) * 100
    
    def _highest_high(self, df: pd.DataFrame, period: int = 20) -> pd.Series:
        """
        Highest High
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the calculation
            
        Returns:
            Series with Highest High values
        """
        return df['high'].rolling(window=period).max()
    
    def _lowest_low(self, df: pd.DataFrame, period: int = 20) -> pd.Series:
        """
        Lowest Low
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the calculation
            
        Returns:
            Series with Lowest Low values
        """
        return df['low'].rolling(window=period).min()
    
    def _bbwidth(self, df: pd.DataFrame, period: int = 20, std_dev: float = 2.0, 
               input_column: str = 'close') -> pd.Series:
        """
        Bollinger Band Width %
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the calculation
            std_dev: Standard deviation multiplier
            input_column: Column to use for calculation
            
        Returns:
            Series with Bollinger Band Width % values
        """
        # Calculate Bollinger Bands
        bbands = self._bbands(df, period, std_dev, input_column)
        
        # Calculate width as a percentage of the middle band
        bbwidth = 100 * (bbands['upper'] - bbands['lower']) / bbands['middle']
        
        return bbwidth
    
    def _bbpercent(self, df: pd.DataFrame, period: int = 20, std_dev: float = 2.0, 
                 input_column: str = 'close') -> pd.Series:
        """
        Bollinger Band %b
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the calculation
            std_dev: Standard deviation multiplier
            input_column: Column to use for calculation
            
        Returns:
            Series with Bollinger Band %b values
        """
        # Calculate Bollinger Bands
        bbands = self._bbands(df, period, std_dev, input_column)
        
        # Calculate %b
        bbpercent = (df[input_column] - bbands['lower']) / (bbands['upper'] - bbands['lower'])
        
        return bbpercent
    
    def _reverse_rsi(self, df: pd.DataFrame, period: int = 14, input_column: str = 'close') -> pd.Series:
        """
        Reverse RSI
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the calculation
            input_column: Column to use for calculation
            
        Returns:
            Series with Reverse RSI values
        """
        # Calculate regular RSI
        rsi = self._rsi(df, period, input_column)
        
        # Reverse it (100 - RSI)
        reverse_rsi = 100 - rsi
        
        return reverse_rsi
    
    def _cutlers_rsi(self, df: pd.DataFrame, period: int = 14, input_column: str = 'close') -> pd.Series:
        """
        Cutler's RSI
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the calculation
            input_column: Column to use for calculation
            
        Returns:
            Series with Cutler's RSI values
        """
        # Calculate price changes
        price_change = df[input_column].diff()
        
        # Calculate the sum of gains and losses over the period
        gains = price_change.copy()
        losses = price_change.copy()
        gains[gains < 0] = 0
        losses[losses > 0] = 0
        losses = abs(losses)
        
        # Calculate the average gain and loss
        avg_gain = gains.rolling(window=period).mean()
        avg_loss = losses.rolling(window=period).mean()
        
        # Calculate Cutler's RSI
        cutlers_rsi = 100 * avg_gain / (avg_gain + avg_loss)
        
        return cutlers_rsi
    
    def _smi(self, df: pd.DataFrame, k_period: int = 10, d_period: int = 3, 
            smooth_period: int = 3) -> pd.DataFrame:
        """
        Stochastic Momentum Index
        
        Args:
            df: DataFrame with OHLCV data
            k_period: K period
            d_period: D period
            smooth_period: Smoothing period
            
        Returns:
            DataFrame with SMI and signal values
        """
        # Calculate highest high and lowest low
        highest_high = df['high'].rolling(window=k_period).max()
        lowest_low = df['low'].rolling(window=k_period).min()
        
        # Calculate distance from close to midpoint
        close_minus_midpoint = df['close'] - (highest_high + lowest_low) / 2
        
        # Calculate range
        price_range = highest_high - lowest_low
        
        # Apply double smoothing to numerator and denominator
        num1 = close_minus_midpoint.ewm(span=smooth_period, adjust=False).mean()
        num2 = num1.ewm(span=smooth_period, adjust=False).mean()
        
        den1 = (price_range / 2).ewm(span=smooth_period, adjust=False).mean()
        den2 = den1.ewm(span=smooth_period, adjust=False).mean()
        
        # Calculate SMI
        smi = 100 * (num2 / den2)
        
        # Calculate signal line
        signal = smi.ewm(span=d_period, adjust=False).mean()
        
        return pd.DataFrame({
            'smi': smi,
            'signal': signal
        })
    
    def _time_series_forecast(self, df: pd.DataFrame, period: int = 14, input_column: str = 'close') -> pd.Series:
        """
        Time Series Forecast
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the calculation
            input_column: Column to use for calculation
            
        Returns:
            Series with Time Series Forecast values
        """
        # Initialize the result series
        tsf = pd.Series(index=df.index, dtype=float)
        
        # Calculate TSF for each window
        for i in range(period, len(df)):
            # Get the window
            window = df[input_column].iloc[i-period+1:i+1]
            
            # Create x and y arrays
            x = np.arange(period)
            y = window.values
            
            # Calculate linear regression
            slope, intercept = np.polyfit(x, y, 1)
            
            # Forecast the next value
            tsf.iloc[i] = intercept + slope * period
        
        return tsf
    
    def _beta(self, df: pd.DataFrame, market_df: pd.DataFrame, period: int = 20) -> pd.Series:
        """
        Beta
        
        Args:
            df: DataFrame with OHLCV data for the security
            market_df: DataFrame with OHLCV data for the market
            period: Period for the calculation
            
        Returns:
            Series with Beta values
        """
        # Calculate returns
        security_returns = df['close'].pct_change()
        market_returns = market_df['close'].pct_change()
        
        # Calculate covariance and variance
        covariance = security_returns.rolling(window=period).cov(market_returns)
        variance = market_returns.rolling(window=period).var()
        
        # Calculate Beta
        beta = covariance / variance
        
        return beta
    
    def _correlation(self, df1: pd.DataFrame, df2: pd.DataFrame, period: int = 20, 
                   column1: str = 'close', column2: str = 'close') -> pd.Series:
        """
        Correlation Coefficient
        
        Args:
            df1: First DataFrame with OHLCV data
            df2: Second DataFrame with OHLCV data
            period: Period for the calculation
            column1: Column to use from first DataFrame
            column2: Column to use from second DataFrame
            
        Returns:
            Series with Correlation Coefficient values
        """
        # Calculate correlation
        correlation = df1[column1].rolling(window=period).corr(df2[column2])
        
        return correlation
    
    def _sharpe_ratio(self, df: pd.DataFrame, risk_free_rate: float = 0.0, period: int = 252, 
                    input_column: str = 'close') -> pd.Series:
        """
        Sharpe Ratio
        
        Args:
            df: DataFrame with OHLCV data
            risk_free_rate: Risk-free rate (annualized)
            period: Period for the calculation (252 for daily data)
            input_column: Column to use for calculation
            
        Returns:
            Series with Sharpe Ratio values
        """
        # Calculate returns
        returns = df[input_column].pct_change()
        
        # Calculate excess returns
        excess_returns = returns - risk_free_rate / period
        
        # Calculate Sharpe Ratio
        sharpe = excess_returns.rolling(window=period).mean() / returns.rolling(window=period).std() * np.sqrt(period)
        
        return sharpe
    
    def _sortino_ratio(self, df: pd.DataFrame, risk_free_rate: float = 0.0, period: int = 252, 
                      input_column: str = 'close') -> pd.Series:
        """
        Sortino Ratio
        
        Args:
            df: DataFrame with OHLCV data
            risk_free_rate: Risk-free rate (annualized)
            period: Period for the calculation (252 for daily data)
            input_column: Column to use for calculation
            
        Returns:
            Series with Sortino Ratio values
        """
        # Calculate returns
        returns = df[input_column].pct_change()
        
        # Calculate excess returns
        excess_returns = returns - risk_free_rate / period
        
        # Calculate downside deviation
        downside_returns = returns.copy()
        downside_returns[downside_returns > 0] = 0
        downside_deviation = np.sqrt(np.sum(downside_returns ** 2) / len(downside_returns)) * np.sqrt(period)
        
        # Calculate Sortino Ratio
        sortino = excess_returns.rolling(window=period).mean() / downside_deviation
        
        return sortino
    
    def _accumulation_distribution(self, df: pd.DataFrame) -> pd.Series:
        """
        Accumulation Distribution Line
        
        Args:
            df: DataFrame with OHLCV data
            
        Returns:
            Series with Accumulation Distribution values
        """
        # Calculate the Money Flow Multiplier
        high_low_range = df['high'] - df['low']
        money_flow_multiplier = ((df['close'] - df['low']) - (df['high'] - df['close'])) / high_low_range
        money_flow_multiplier = money_flow_multiplier.replace([np.inf, -np.inf], 0)
        
        # Calculate the Money Flow Volume
        money_flow_volume = money_flow_multiplier * df['volume']
        
        # Calculate the Accumulation Distribution Line
        adl = money_flow_volume.cumsum()
        
        return adl
    
    def _asi(self, df: pd.DataFrame, limit_move: float = 5.0) -> pd.Series:
        """
        Accumulation Swing Index
        
        Args:
            df: DataFrame with OHLCV data
            limit_move: Limit move value
            
        Returns:
            Series with ASI values
        """
        # Calculate the components
        c_prev = df['close'].shift(1)
        
        # Calculate the swings
        t = df['high'] - df['low']
        k = df['high'] - c_prev
        k_abs = np.abs(k)
        m = df['low'] - c_prev
        m_abs = np.abs(m)
        r = df['high'] - df['close'].shift(1)
        r_abs = np.abs(r)
        s = df['low'] - df['close'].shift(1)
        s_abs = np.abs(s)
        
        # Calculate the R component
        r1 = np.where(k_abs > m_abs, k_abs, m_abs)
        r2 = np.where(r_abs > s_abs, r_abs, s_abs)
        r3 = np.where(r1 > r2, r1, r2)
        
        # Create a Series for SI values
        si_values = np.zeros(len(df))
        
        # Calculate the SI
        for i in range(1, len(df)):
            if t.iloc[i] == 0 or r3[i] == 0 or limit_move == 0:
                si_values[i] = 0
            else:
                k_component = 0.5 * (df['close'].iloc[i] - df['close'].iloc[i-1] + 
                                    0.5 * (df['close'].iloc[i] - df['open'].iloc[i]) + 
                                    0.25 * (df['close'].iloc[i-1] - df['open'].iloc[i-1]))
                r_component = r3[i]
                si_values[i] = 50 * k_component / r_component * limit_move / 100
        
        # Create a Series with the calculated values
        si = pd.Series(si_values, index=df.index)
        
        # Calculate the ASI (cumulative sum of SI)
        asi = si.cumsum()
        
        return asi
    
    def _fast_stochastic(self, df: pd.DataFrame, k_period: int = 14) -> pd.Series:
        """
        Fast Stochastic %K
        
        Args:
            df: DataFrame with OHLCV data
            k_period: K period
            
        Returns:
            Series with Fast Stochastic %K values
        """
        # Calculate highest high and lowest low
        highest_high = df['high'].rolling(window=k_period).max()
        lowest_low = df['low'].rolling(window=k_period).min()
        
        # Calculate Fast Stochastic %K
        fast_k = 100 * (df['close'] - lowest_low) / (highest_high - lowest_low)
        
        return fast_k
    
    def _slow_stochastic(self, df: pd.DataFrame, k_period: int = 14, d_period: int = 3) -> pd.DataFrame:
        """
        Slow Stochastic
        
        Args:
            df: DataFrame with OHLCV data
            k_period: K period
            d_period: D period
            
        Returns:
            DataFrame with Slow Stochastic %K and %D values
        """
        # Calculate Fast Stochastic %K
        fast_k = self._fast_stochastic(df, k_period)
        
        # Calculate Slow Stochastic %K (3-period SMA of Fast %K)
        slow_k = fast_k.rolling(window=d_period).mean()
        
        # Calculate Slow Stochastic %D (3-period SMA of Slow %K)
        slow_d = slow_k.rolling(window=d_period).mean()
        
        return pd.DataFrame({
            'k': slow_k,
            'd': slow_d
        })
    
    def _full_stochastic(self, df: pd.DataFrame, k_period: int = 14, d_period: int = 3, 
                       slowing: int = 3) -> pd.DataFrame:
        """
        Full Stochastic
        
        Args:
            df: DataFrame with OHLCV data
            k_period: K period
            d_period: D period
            slowing: Slowing period
            
        Returns:
            DataFrame with Full Stochastic %K and %D values
        """
        # Calculate highest high and lowest low
        highest_high = df['high'].rolling(window=k_period).max()
        lowest_low = df['low'].rolling(window=k_period).min()
        
        # Calculate Raw %K
        raw_k = 100 * (df['close'] - lowest_low) / (highest_high - lowest_low)
        
        # Calculate Full %K (slowing period SMA of Raw %K)
        full_k = raw_k.rolling(window=slowing).mean()
        
        # Calculate Full %D (d_period SMA of Full %K)
        full_d = full_k.rolling(window=d_period).mean()
        
        return pd.DataFrame({
            'k': full_k,
            'd': full_d
        })
    
    def _heikin_ashi(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Heikin-Ashi
        
        Args:
            df: DataFrame with OHLCV data
            
        Returns:
            DataFrame with Heikin-Ashi OHLC values
        """
        # Initialize the result DataFrame with empty columns
        ha = pd.DataFrame(index=df.index, columns=['open', 'high', 'low', 'close'], dtype=float)
        
        # Calculate the first Heikin-Ashi candle
        ha.loc[df.index[0], 'close'] = (df['open'].iloc[0] + df['high'].iloc[0] + df['low'].iloc[0] + df['close'].iloc[0]) / 4
        ha.loc[df.index[0], 'open'] = (df['open'].iloc[0] + df['close'].iloc[0]) / 2
        ha.loc[df.index[0], 'high'] = df['high'].iloc[0]
        ha.loc[df.index[0], 'low'] = df['low'].iloc[0]
        
        # Calculate the rest of the Heikin-Ashi candles
        for i in range(1, len(df)):
            idx = df.index[i]
            prev_idx = df.index[i-1]
            
            # Calculate close
            ha.loc[idx, 'close'] = (df['open'].iloc[i] + df['high'].iloc[i] + df['low'].iloc[i] + df['close'].iloc[i]) / 4
            
            # Calculate open
            ha.loc[idx, 'open'] = (ha.loc[prev_idx, 'open'] + ha.loc[prev_idx, 'close']) / 2
            
            # Calculate high
            ha.loc[idx, 'high'] = max(df['high'].iloc[i], ha.loc[idx, 'open'], ha.loc[idx, 'close'])
            
            # Calculate low
            ha.loc[idx, 'low'] = min(df['low'].iloc[i], ha.loc[idx, 'open'], ha.loc[idx, 'close'])
        
        return ha
    
    def _hlc_bars(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        HLC Bars
        
        Args:
            df: DataFrame with OHLCV data
            
        Returns:
            DataFrame with HLC values
        """
        return df[['high', 'low', 'close']]
    
    def _ohlc_bars(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        OHLC Bars
        
        Args:
            df: DataFrame with OHLCV data
            
        Returns:
            DataFrame with OHLC values
        """
        return df[['open', 'high', 'low', 'close']]
    
    def _center_of_gravity(self, df: pd.DataFrame, period: int = 10, input_column: str = 'close') -> pd.Series:
        """
        Center of Gravity
        
        Args:
            df: DataFrame with OHLCV data
            period: Period for the calculation
            input_column: Column to use for calculation
            
        Returns:
            Series with Center of Gravity values
        """
        # Initialize the result array
        cog_values = np.zeros(len(df))
        
        # Calculate Center of Gravity for each window
        for i in range(period-1, len(df)):
            # Get the window
            window = df[input_column].iloc[i-period+1:i+1].values
            
            # Calculate numerator and denominator
            numerator = 0
            denominator = 0
            
            for j in range(period):
                numerator += (j+1) * window[j]
                denominator += window[j]
            
            # Calculate COG
            if denominator != 0:
                cog_values[i] = -1 * (numerator / denominator) + (period + 1) / 2
            else:
                cog_values[i] = 0
        
        # Create a Series with the calculated values
        cog = pd.Series(cog_values, index=df.index)
        
        return cog