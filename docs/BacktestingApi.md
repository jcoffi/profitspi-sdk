# profitspi-sdk.BacktestingApi

All URIs are relative to *https://www.profitspi.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backtesting_delete_strategy**](BacktestingApi.md#backtesting_delete_strategy) | **DELETE** /strategies/{id} | Deletes a User Strategy and all it&#39;s Tests.
[**backtesting_delete_strategy_test**](BacktestingApi.md#backtesting_delete_strategy_test) | **DELETE** /strategies/{id}/tests/{test} | Deletes a User Strategy Test.
[**backtesting_get_default_strategies**](BacktestingApi.md#backtesting_get_default_strategies) | **GET** /defaultstrategies | Retrieves the list of Default Strategies.
[**backtesting_get_default_strategy_test**](BacktestingApi.md#backtesting_get_default_strategy_test) | **GET** /defaultstrategies/{id}/tests/{test} | Retrieves the definition and results for a Default Strategy Test.
[**backtesting_get_user_strategies**](BacktestingApi.md#backtesting_get_user_strategies) | **GET** /strategies | Retrieves the list of Strategies for a User.
[**backtesting_get_user_strategy_test**](BacktestingApi.md#backtesting_get_user_strategy_test) | **GET** /strategies/{id}/tests | Retrieves the list of Tests for a User Strategy.
[**backtesting_get_user_strategy_test_0**](BacktestingApi.md#backtesting_get_user_strategy_test_0) | **GET** /strategies/{id}/tests/{test} | Retrieves the definition and results for a User Strategy Test.
[**backtesting_get_user_strategy_test_history**](BacktestingApi.md#backtesting_get_user_strategy_test_history) | **GET** /strategies/{id}/tests/{test}/history | Retrieves the history for a User Strategy Test.
[**backtesting_get_user_strategy_test_trades**](BacktestingApi.md#backtesting_get_user_strategy_test_trades) | **GET** /strategies/{id}/tests/{test}/trades | Retrieves the trades generated for a User Strategy Test.
[**backtesting_post_strategy**](BacktestingApi.md#backtesting_post_strategy) | **POST** /strategies | Adds a new User Strategy Test to a new Strategy and initiates a Test Run.
[**backtesting_post_strategy_test**](BacktestingApi.md#backtesting_post_strategy_test) | **POST** /strategies/{id}/tests | Adds a new User Strategy Test to an existing Strategy and initiates a Test Run.
[**backtesting_put_strategy**](BacktestingApi.md#backtesting_put_strategy) | **PUT** /strategies/{id} | Updates header information for a User Strategy.


# **backtesting_delete_strategy**
> Object backtesting_delete_strategy(id, api_key, user_id)

Deletes a User Strategy and all it's Tests.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.BacktestingApi()
id = 56 # int | The strategy_id from the User Strategies API.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Deletes a User Strategy and all it's Tests.
    api_response = api_instance.backtesting_delete_strategy(id, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BacktestingApi->backtesting_delete_strategy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The strategy_id from the User Strategies API. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backtesting_delete_strategy_test**
> Object backtesting_delete_strategy_test(id, test, api_key, user_id)

Deletes a User Strategy Test.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.BacktestingApi()
id = 56 # int | The strategy_id from the User Strategies API.
test = 56 # int | The test_num from the User Strategies API.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Deletes a User Strategy Test.
    api_response = api_instance.backtesting_delete_strategy_test(id, test, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BacktestingApi->backtesting_delete_strategy_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The strategy_id from the User Strategies API. | 
 **test** | **int**| The test_num from the User Strategies API. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backtesting_get_default_strategies**
> list[Defaultstrategy] backtesting_get_default_strategies(api_key, user_id)

Retrieves the list of Default Strategies.

Returns a list of Default Strategies with summary information.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.BacktestingApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Default Strategies.
    api_response = api_instance.backtesting_get_default_strategies(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BacktestingApi->backtesting_get_default_strategies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Defaultstrategy]**](Defaultstrategy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backtesting_get_default_strategy_test**
> Strategytest backtesting_get_default_strategy_test(id, test, api_key, user_id)

Retrieves the definition and results for a Default Strategy Test.

Returns the definition and results for a Default Strategy Test. View the results or use the definition to create a User Strategy.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.BacktestingApi()
id = 56 # int | The strategy_id from the Default Strategies API.
test = 56 # int | The test_num from the Default Strategies API.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the definition and results for a Default Strategy Test.
    api_response = api_instance.backtesting_get_default_strategy_test(id, test, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BacktestingApi->backtesting_get_default_strategy_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The strategy_id from the Default Strategies API. | 
 **test** | **int**| The test_num from the Default Strategies API. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**Strategytest**](Strategytest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backtesting_get_user_strategies**
> list[Strategy] backtesting_get_user_strategies(api_key, user_id)

Retrieves the list of Strategies for a User.

Returns a list of Strategies for a User with summary information.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.BacktestingApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Strategies for a User.
    api_response = api_instance.backtesting_get_user_strategies(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BacktestingApi->backtesting_get_user_strategies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Strategy]**](Strategy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backtesting_get_user_strategy_test**
> list[Strategytestsummary] backtesting_get_user_strategy_test(id, api_key, user_id)

Retrieves the list of Tests for a User Strategy.

Returns a list of Tests for a User Strategy.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.BacktestingApi()
id = 56 # int | The strategy_id from the User Strategies API.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Tests for a User Strategy.
    api_response = api_instance.backtesting_get_user_strategy_test(id, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BacktestingApi->backtesting_get_user_strategy_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The strategy_id from the User Strategies API. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Strategytestsummary]**](Strategytestsummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backtesting_get_user_strategy_test_0**
> Strategytest backtesting_get_user_strategy_test_0(id, test, api_key, user_id)

Retrieves the definition and results for a User Strategy Test.

Returns the definition and results for a User Strategy Test. View the results or use the definition to create a User Strategy.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.BacktestingApi()
id = 56 # int | The strategy_id from the User Strategies API.
test = 56 # int | The test_num from the User Strategies API.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the definition and results for a User Strategy Test.
    api_response = api_instance.backtesting_get_user_strategy_test_0(id, test, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BacktestingApi->backtesting_get_user_strategy_test_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The strategy_id from the User Strategies API. | 
 **test** | **int**| The test_num from the User Strategies API. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**Strategytest**](Strategytest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backtesting_get_user_strategy_test_history**
> Strategytesthistory backtesting_get_user_strategy_test_history(id, test, api_key, user_id, period_type=period_type, per_page=per_page, page=page)

Retrieves the history for a User Strategy Test.

Returns the history for a User Strategy Test.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.BacktestingApi()
id = 56 # int | The strategy_id from the User Strategies API.
test = 56 # int | The test_num from the User Strategies API.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.
period_type = 'period_type_example' # str | Use \"M\" for Monthly, \"Y\" for Yearly. Default is \"D\" for Daily (optional)
per_page = 56 # int | The page size for the results. Default is 100. (optional)
page = 56 # int | A specific page when paging thru the results. Default is 0. (optional)

try:
    # Retrieves the history for a User Strategy Test.
    api_response = api_instance.backtesting_get_user_strategy_test_history(id, test, api_key, user_id, period_type=period_type, per_page=per_page, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BacktestingApi->backtesting_get_user_strategy_test_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The strategy_id from the User Strategies API. | 
 **test** | **int**| The test_num from the User Strategies API. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 
 **period_type** | **str**| Use \&quot;M\&quot; for Monthly, \&quot;Y\&quot; for Yearly. Default is \&quot;D\&quot; for Daily | [optional] 
 **per_page** | **int**| The page size for the results. Default is 100. | [optional] 
 **page** | **int**| A specific page when paging thru the results. Default is 0. | [optional] 

### Return type

[**Strategytesthistory**](Strategytesthistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backtesting_get_user_strategy_test_trades**
> Strategytesttrades backtesting_get_user_strategy_test_trades(id, test, api_key, user_id, per_page=per_page, page=page)

Retrieves the trades generated for a User Strategy Test.

Returns the trades generated for a User Strategy Test.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.BacktestingApi()
id = 56 # int | The strategy_id from the User Strategies API.
test = 56 # int | The test_num from the User Strategies API.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.
per_page = 56 # int | The page size for the results. Default is 100. (optional)
page = 56 # int | A specific page when paging thru the results. Default is 0. (optional)

try:
    # Retrieves the trades generated for a User Strategy Test.
    api_response = api_instance.backtesting_get_user_strategy_test_trades(id, test, api_key, user_id, per_page=per_page, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BacktestingApi->backtesting_get_user_strategy_test_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The strategy_id from the User Strategies API. | 
 **test** | **int**| The test_num from the User Strategies API. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 
 **per_page** | **int**| The page size for the results. Default is 100. | [optional] 
 **page** | **int**| A specific page when paging thru the results. Default is 0. | [optional] 

### Return type

[**Strategytesttrades**](Strategytesttrades.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backtesting_post_strategy**
> Object backtesting_post_strategy(strategytest, api_key, user_id)

Adds a new User Strategy Test to a new Strategy and initiates a Test Run.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.BacktestingApi()
strategytest = profitspi-sdk.Strategytest() # Strategytest | 
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Adds a new User Strategy Test to a new Strategy and initiates a Test Run.
    api_response = api_instance.backtesting_post_strategy(strategytest, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BacktestingApi->backtesting_post_strategy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strategytest** | [**Strategytest**](Strategytest.md)|  | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backtesting_post_strategy_test**
> Object backtesting_post_strategy_test(strategytest, id, api_key, user_id)

Adds a new User Strategy Test to an existing Strategy and initiates a Test Run.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.BacktestingApi()
strategytest = profitspi-sdk.Strategytest() # Strategytest | 
id = 56 # int | The strategy_id from the User Strategies API.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Adds a new User Strategy Test to an existing Strategy and initiates a Test Run.
    api_response = api_instance.backtesting_post_strategy_test(strategytest, id, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BacktestingApi->backtesting_post_strategy_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strategytest** | [**Strategytest**](Strategytest.md)|  | 
 **id** | **int**| The strategy_id from the User Strategies API. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backtesting_put_strategy**
> Object backtesting_put_strategy(strategy, id, api_key, user_id)

Updates header information for a User Strategy.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.BacktestingApi()
strategy = profitspi-sdk.Strategy() # Strategy | 
id = 56 # int | The strategy_id from the User Strategies API.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Updates header information for a User Strategy.
    api_response = api_instance.backtesting_put_strategy(strategy, id, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BacktestingApi->backtesting_put_strategy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strategy** | [**Strategy**](Strategy.md)|  | 
 **id** | **int**| The strategy_id from the User Strategies API. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

