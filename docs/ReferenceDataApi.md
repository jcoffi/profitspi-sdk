# profitspi-sdk.ReferenceDataApi

All URIs are relative to *https://www.profitspi.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reference_data_get_criteria_conditions**](ReferenceDataApi.md#reference_data_get_criteria_conditions) | **GET** /criteriaconditions | Retrieves the list of Criteria Conditions.
[**reference_data_get_days_to_test_codes**](ReferenceDataApi.md#reference_data_get_days_to_test_codes) | **GET** /daystotestcodes | Retrieves the list of Strategy Days to Test Codes.
[**reference_data_get_indicator_aliases**](ReferenceDataApi.md#reference_data_get_indicator_aliases) | **GET** /indicatoraliases | Retrieves the list of Indicator Aliases.
[**reference_data_get_indicator_types**](ReferenceDataApi.md#reference_data_get_indicator_types) | **GET** /indicatortypes | Retrieves the list of Indicator Types.
[**reference_data_get_indicators**](ReferenceDataApi.md#reference_data_get_indicators) | **GET** /indicators | Retrieves the list of Indicators.
[**reference_data_get_periods**](ReferenceDataApi.md#reference_data_get_periods) | **GET** /periods | Retrieves the list of Periods.
[**reference_data_get_position_entry_price_types**](ReferenceDataApi.md#reference_data_get_position_entry_price_types) | **GET** /positionentrypricetypes | Retrieves the list of Strategy Position Entry Price Types.
[**reference_data_get_position_exit_price_types**](ReferenceDataApi.md#reference_data_get_position_exit_price_types) | **GET** /positionexitpricetypes | Retrieves the list of Strategy Position Exit Price Types.
[**reference_data_get_position_rounding_amounts**](ReferenceDataApi.md#reference_data_get_position_rounding_amounts) | **GET** /positionroundingamounts | Retrieves the list of Strategy Position Rounding Amounts.
[**reference_data_get_position_sizing_types**](ReferenceDataApi.md#reference_data_get_position_sizing_types) | **GET** /positionsizingtypes | Retrieves the list of Strategy Position Sizing Types.
[**reference_data_get_stop_loss_exit_price_types**](ReferenceDataApi.md#reference_data_get_stop_loss_exit_price_types) | **GET** /stoplossexitpricetypes | Retrieves the list of Strategy Stop Loss Exit Price Types.
[**reference_data_get_target_exit_price_types**](ReferenceDataApi.md#reference_data_get_target_exit_price_types) | **GET** /targetexitpricetypes | Retrieves the list of Strategy Target Exit Price Types.
[**reference_data_get_time_stop_exit_price_types**](ReferenceDataApi.md#reference_data_get_time_stop_exit_price_types) | **GET** /timestopexitpricetypes | Retrieves the list of Strategy Time Stop Exit Price Types.
[**reference_data_get_trailing_stop_loss_exit_price_types**](ReferenceDataApi.md#reference_data_get_trailing_stop_loss_exit_price_types) | **GET** /trailingstoplossexitpricetypes | Retrieves the list of Strategy Trailing Stop Loss Exit Price Types.
[**reference_data_get_trailing_stop_loss_price_to_use_types**](ReferenceDataApi.md#reference_data_get_trailing_stop_loss_price_to_use_types) | **GET** /trailingstoplosspricetouses | Retrieves the list of Strategy Trailing Stop Loss Price to Use Types.


# **reference_data_get_criteria_conditions**
> list[Criteriacondition] reference_data_get_criteria_conditions(api_key, user_id)

Retrieves the list of Criteria Conditions.

Returns a list of Criteria Condition ids with their descriptions and usage.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ReferenceDataApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Criteria Conditions.
    api_response = api_instance.reference_data_get_criteria_conditions(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceDataApi->reference_data_get_criteria_conditions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Criteriacondition]**](Criteriacondition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_data_get_days_to_test_codes**
> list[Daystotest] reference_data_get_days_to_test_codes(api_key, user_id)

Retrieves the list of Strategy Days to Test Codes.

Returns a list of Strategy Days to Test Codes with their descriptions.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ReferenceDataApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Strategy Days to Test Codes.
    api_response = api_instance.reference_data_get_days_to_test_codes(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceDataApi->reference_data_get_days_to_test_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Daystotest]**](Daystotest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_data_get_indicator_aliases**
> list[Indicatoralias] reference_data_get_indicator_aliases(api_key, user_id)

Retrieves the list of Indicator Aliases.

Returns a list of Indicators with their aliases and descriptions.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ReferenceDataApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Indicator Aliases.
    api_response = api_instance.reference_data_get_indicator_aliases(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceDataApi->reference_data_get_indicator_aliases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Indicatoralias]**](Indicatoralias.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_data_get_indicator_types**
> list[Indicatortype] reference_data_get_indicator_types(api_key, user_id)

Retrieves the list of Indicator Types.

Returns a list of Indicator Types with their descriptions.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ReferenceDataApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Indicator Types.
    api_response = api_instance.reference_data_get_indicator_types(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceDataApi->reference_data_get_indicator_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Indicatortype]**](Indicatortype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_data_get_indicators**
> list[Indicator] reference_data_get_indicators(api_key, user_id)

Retrieves the list of Indicators.

Returns a list of Indicators with their descriptions and attributes.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ReferenceDataApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Indicators.
    api_response = api_instance.reference_data_get_indicators(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceDataApi->reference_data_get_indicators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Indicator]**](Indicator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_data_get_periods**
> list[Period] reference_data_get_periods(api_key, user_id)

Retrieves the list of Periods.

Returns a list of Period ids with their descriptions.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ReferenceDataApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Periods.
    api_response = api_instance.reference_data_get_periods(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceDataApi->reference_data_get_periods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Period]**](Period.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_data_get_position_entry_price_types**
> list[Positionentrypricetype] reference_data_get_position_entry_price_types(api_key, user_id)

Retrieves the list of Strategy Position Entry Price Types.

Returns a list of Strategy Position Entry Price Types with their descriptions.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ReferenceDataApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Strategy Position Entry Price Types.
    api_response = api_instance.reference_data_get_position_entry_price_types(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceDataApi->reference_data_get_position_entry_price_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Positionentrypricetype]**](Positionentrypricetype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_data_get_position_exit_price_types**
> list[Positionexitpricetype] reference_data_get_position_exit_price_types(api_key, user_id)

Retrieves the list of Strategy Position Exit Price Types.

Returns a list of Strategy Position Exit Price Types with their descriptions.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ReferenceDataApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Strategy Position Exit Price Types.
    api_response = api_instance.reference_data_get_position_exit_price_types(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceDataApi->reference_data_get_position_exit_price_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Positionexitpricetype]**](Positionexitpricetype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_data_get_position_rounding_amounts**
> list[Positionroundingamount] reference_data_get_position_rounding_amounts(api_key, user_id)

Retrieves the list of Strategy Position Rounding Amounts.

Returns a list of Strategy Position Rounding Amounts with their descriptions.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ReferenceDataApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Strategy Position Rounding Amounts.
    api_response = api_instance.reference_data_get_position_rounding_amounts(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceDataApi->reference_data_get_position_rounding_amounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Positionroundingamount]**](Positionroundingamount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_data_get_position_sizing_types**
> list[Positionsizingtype] reference_data_get_position_sizing_types(api_key, user_id)

Retrieves the list of Strategy Position Sizing Types.

Returns a list of Strategy Position Sizing Ids with their descriptions.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ReferenceDataApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Strategy Position Sizing Types.
    api_response = api_instance.reference_data_get_position_sizing_types(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceDataApi->reference_data_get_position_sizing_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Positionsizingtype]**](Positionsizingtype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_data_get_stop_loss_exit_price_types**
> list[Stoplossexitpricetype] reference_data_get_stop_loss_exit_price_types(api_key, user_id)

Retrieves the list of Strategy Stop Loss Exit Price Types.

Returns a list of Strategy Stop Loss Exit Price Types with their descriptions.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ReferenceDataApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Strategy Stop Loss Exit Price Types.
    api_response = api_instance.reference_data_get_stop_loss_exit_price_types(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceDataApi->reference_data_get_stop_loss_exit_price_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Stoplossexitpricetype]**](Stoplossexitpricetype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_data_get_target_exit_price_types**
> list[Targetexitpricetype] reference_data_get_target_exit_price_types(api_key, user_id)

Retrieves the list of Strategy Target Exit Price Types.

Returns a list of Strategy Target Exit Price Types with their descriptions.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ReferenceDataApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Strategy Target Exit Price Types.
    api_response = api_instance.reference_data_get_target_exit_price_types(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceDataApi->reference_data_get_target_exit_price_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Targetexitpricetype]**](Targetexitpricetype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_data_get_time_stop_exit_price_types**
> list[Timestopexitpricetype] reference_data_get_time_stop_exit_price_types(api_key, user_id)

Retrieves the list of Strategy Time Stop Exit Price Types.

Returns a list of Strategy Time Exit Price Types with their descriptions.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ReferenceDataApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Strategy Time Stop Exit Price Types.
    api_response = api_instance.reference_data_get_time_stop_exit_price_types(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceDataApi->reference_data_get_time_stop_exit_price_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Timestopexitpricetype]**](Timestopexitpricetype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_data_get_trailing_stop_loss_exit_price_types**
> list[Trailingstoplossexitpricetype] reference_data_get_trailing_stop_loss_exit_price_types(api_key, user_id)

Retrieves the list of Strategy Trailing Stop Loss Exit Price Types.

Returns a list of Strategy Trailing Stop Loss Exit Price Types with their descriptions.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ReferenceDataApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Strategy Trailing Stop Loss Exit Price Types.
    api_response = api_instance.reference_data_get_trailing_stop_loss_exit_price_types(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceDataApi->reference_data_get_trailing_stop_loss_exit_price_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Trailingstoplossexitpricetype]**](Trailingstoplossexitpricetype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_data_get_trailing_stop_loss_price_to_use_types**
> list[Trailingstoplosspricetouse] reference_data_get_trailing_stop_loss_price_to_use_types(api_key, user_id)

Retrieves the list of Strategy Trailing Stop Loss Price to Use Types.

Returns a list of Strategy Trailing Stop Loss Price to Use Types with their descriptions.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ReferenceDataApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Strategy Trailing Stop Loss Price to Use Types.
    api_response = api_instance.reference_data_get_trailing_stop_loss_price_to_use_types(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceDataApi->reference_data_get_trailing_stop_loss_price_to_use_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Trailingstoplosspricetouse]**](Trailingstoplosspricetouse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

