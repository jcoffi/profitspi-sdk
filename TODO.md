# Technical Indicators Implementation - TODO

## Remaining Tasks

1. **Fix Pandas FutureWarnings**
   - Update remaining indicators that use `.iloc` assignment to use `.loc` instead
   - Specifically check the Time Series Forecast and Fisher Transform implementations

2. **Implement Fundamental Indicators**
   - Current EPS (requires fundamental data)
   - Dividend Yield % (requires fundamental data)
   - PE Ratio (requires fundamental data)
   - Shares Outstanding (requires fundamental data)

3. **Implement Specialized Indicators**
   - Candlesticks (requires specialized charting library)
   - Open Interest (requires futures/options data)

4. **Testing and Validation**
   - Create comprehensive unit tests for all indicators
   - Compare results with established libraries like TA-Lib
   - Test with different data frequencies (daily, hourly, minute)
   - Test with different assets (stocks, forex, crypto)

5. **Documentation**
   - Create detailed documentation for each indicator
   - Include formulas, parameters, and usage examples
   - Add references to academic papers or books where applicable

6. **Performance Optimization**
   - Profile the code to identify bottlenecks
   - Optimize slow indicators (especially those with loops)
   - Consider using Numba or Cython for critical sections

7. **API Improvements**
   - Create a unified API for accessing all indicators
   - Add parameter validation and error handling
   - Support for different input formats (OHLCV, HLCV, etc.)

## Known Issues

1. Some indicators produce FutureWarnings due to pandas' upcoming changes in 3.0
2. The ASI (Accumulation Swing Index) implementation may need further validation
3. The Fisher Transform implementation has edge cases that need to be handled better
4. The Time Series Forecast implementation is computationally expensive for large datasets