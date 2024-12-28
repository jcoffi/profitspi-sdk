# profitspi-sdk.UserInstrumentsApi

All URIs are relative to *https://www.profitspi.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_instruments_delete_user_calendar_holidays**](UserInstrumentsApi.md#user_instruments_delete_user_calendar_holidays) | **DELETE** /usercalendars/{id}/holidays | Deletes all Holidays for a User or Corporate Calendar.
[**user_instruments_delete_user_exchange_instrument**](UserInstrumentsApi.md#user_instruments_delete_user_exchange_instrument) | **DELETE** /userexchanges/{id}/instruments/{instrument} | Deletes a specific Instrument for a User or Corporate Instrument.
[**user_instruments_delete_user_instrument_price_history**](UserInstrumentsApi.md#user_instruments_delete_user_instrument_price_history) | **DELETE** /userexchanges/{id}/instruments/{instrument}/pricehistory | Deletes all price history for a User or Corporate Instrument.
[**user_instruments_delete_user_instrument_splits**](UserInstrumentsApi.md#user_instruments_delete_user_instrument_splits) | **DELETE** /userexchanges/{id}/instruments/{instrument}/splits | Deletes all Splits for a User or Corporate Instrument.
[**user_instruments_get_user_calendar**](UserInstrumentsApi.md#user_instruments_get_user_calendar) | **GET** /usercalendars/{id} | Retrieves a specific User or Corporate Calendar.
[**user_instruments_get_user_calendar_holidays**](UserInstrumentsApi.md#user_instruments_get_user_calendar_holidays) | **GET** /usercalendars/{id}/holidays | Retrieves the list of Holidays for a User or Corporate Calendar.
[**user_instruments_get_user_calendars**](UserInstrumentsApi.md#user_instruments_get_user_calendars) | **GET** /usercalendars | Retrieves the list of User or Corporate Calendars.
[**user_instruments_get_user_exchange**](UserInstrumentsApi.md#user_instruments_get_user_exchange) | **GET** /userexchanges/{id} | Retrieves a specific User or Corporate Exchange.
[**user_instruments_get_user_exchange_instrument**](UserInstrumentsApi.md#user_instruments_get_user_exchange_instrument) | **GET** /userexchanges/{id}/instruments/{instrument} | Retrieves a specific Instrument for a User or Corporate Exchange.
[**user_instruments_get_user_exchange_instruments**](UserInstrumentsApi.md#user_instruments_get_user_exchange_instruments) | **GET** /userexchanges/{id}/instruments | Retrieves the list of Instruments for a User or Corporate Exchange.
[**user_instruments_get_user_exchanges**](UserInstrumentsApi.md#user_instruments_get_user_exchanges) | **GET** /userexchanges | Retrieves the list of User and Corporate Exchanges.
[**user_instruments_get_user_instrument_price_history**](UserInstrumentsApi.md#user_instruments_get_user_instrument_price_history) | **GET** /userexchanges/{id}/instruments/{instrument}/pricehistory | Retrieves price history for a specific User or Corporate Instrument.
[**user_instruments_get_user_instrument_splits**](UserInstrumentsApi.md#user_instruments_get_user_instrument_splits) | **GET** /userexchanges/{id}/instruments/{instrument}/splits | Retrieves Splits for a specific User or Corporate Instrument.
[**user_instruments_post_user_calendar**](UserInstrumentsApi.md#user_instruments_post_user_calendar) | **POST** /usercalendars | Adds a new User or Corporate Calendar.
[**user_instruments_post_user_calendar_holidays**](UserInstrumentsApi.md#user_instruments_post_user_calendar_holidays) | **POST** /usercalendars/{id}/holidays | Adds one or more new Holidays to a User or Corporate Calendar.
[**user_instruments_post_user_exchange**](UserInstrumentsApi.md#user_instruments_post_user_exchange) | **POST** /userexchanges | Adds a new User or Corporate Exchange.
[**user_instruments_post_user_exchange_instrument**](UserInstrumentsApi.md#user_instruments_post_user_exchange_instrument) | **POST** /userexchanges/{id}/instruments | Adds a new Instrument to a User or Corporate Exchange.
[**user_instruments_post_user_instrument_price_history**](UserInstrumentsApi.md#user_instruments_post_user_instrument_price_history) | **POST** /userexchanges/{id}/instruments/{instrument}/pricehistory | Adds / replaces price history for a User or Corporate Instrument.
[**user_instruments_post_user_instrument_splits**](UserInstrumentsApi.md#user_instruments_post_user_instrument_splits) | **POST** /userexchanges/{id}/instruments/{instrument}/splits | Adds one or more Splits to a Corporate Instrument.
[**user_instruments_put_exchange**](UserInstrumentsApi.md#user_instruments_put_exchange) | **PUT** /userexchanges/{id} | Updates a User or Corporate Exchange.
[**user_instruments_put_user_calendar**](UserInstrumentsApi.md#user_instruments_put_user_calendar) | **PUT** /usercalendars/{id} | Updates a User or Corporate Calendar.
[**user_instruments_put_user_exchange_instrument**](UserInstrumentsApi.md#user_instruments_put_user_exchange_instrument) | **PUT** /userexchanges/{id}/instruments/{instrument} | Updates a specific Instrument for a User or Corporate Exchange.


# **user_instruments_delete_user_calendar_holidays**
> Object user_instruments_delete_user_calendar_holidays(id, api_key, user_id)

Deletes all Holidays for a User or Corporate Calendar.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
id = 56 # int | The calendar_id.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Deletes all Holidays for a User or Corporate Calendar.
    api_response = api_instance.user_instruments_delete_user_calendar_holidays(id, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_delete_user_calendar_holidays: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The calendar_id. | 
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

# **user_instruments_delete_user_exchange_instrument**
> Object user_instruments_delete_user_exchange_instrument(id, instrument, api_key, user_id)

Deletes a specific Instrument for a User or Corporate Instrument.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
id = 'id_example' # str | The exchange_id.
instrument = 'instrument_example' # str | The Instrument symbol.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Deletes a specific Instrument for a User or Corporate Instrument.
    api_response = api_instance.user_instruments_delete_user_exchange_instrument(id, instrument, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_delete_user_exchange_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The exchange_id. | 
 **instrument** | **str**| The Instrument symbol. | 
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

# **user_instruments_delete_user_instrument_price_history**
> Object user_instruments_delete_user_instrument_price_history(id, instrument, api_key, user_id)

Deletes all price history for a User or Corporate Instrument.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
id = 'id_example' # str | The exchange_id.
instrument = 'instrument_example' # str | The Instrument symbol.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Deletes all price history for a User or Corporate Instrument.
    api_response = api_instance.user_instruments_delete_user_instrument_price_history(id, instrument, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_delete_user_instrument_price_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The exchange_id. | 
 **instrument** | **str**| The Instrument symbol. | 
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

# **user_instruments_delete_user_instrument_splits**
> Object user_instruments_delete_user_instrument_splits(id, instrument, api_key, user_id)

Deletes all Splits for a User or Corporate Instrument.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
id = 'id_example' # str | The exchange_id.
instrument = 'instrument_example' # str | The Instrument symbol.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Deletes all Splits for a User or Corporate Instrument.
    api_response = api_instance.user_instruments_delete_user_instrument_splits(id, instrument, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_delete_user_instrument_splits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The exchange_id. | 
 **instrument** | **str**| The Instrument symbol. | 
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

# **user_instruments_get_user_calendar**
> list[Usercalendar] user_instruments_get_user_calendar(id, api_key, user_id)

Retrieves a specific User or Corporate Calendar.

Retrieve a specific User or Corporate Calendar.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
id = 56 # int | The calendar_id.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves a specific User or Corporate Calendar.
    api_response = api_instance.user_instruments_get_user_calendar(id, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_get_user_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The calendar_id. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Usercalendar]**](Usercalendar.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_instruments_get_user_calendar_holidays**
> list[Usercalendarholiday] user_instruments_get_user_calendar_holidays(id, api_key, user_id)

Retrieves the list of Holidays for a User or Corporate Calendar.

Retrieves the list of Holidays for a User or Corporate Calendar.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
id = 56 # int | The calendar_id.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Holidays for a User or Corporate Calendar.
    api_response = api_instance.user_instruments_get_user_calendar_holidays(id, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_get_user_calendar_holidays: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The calendar_id. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Usercalendarholiday]**](Usercalendarholiday.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_instruments_get_user_calendars**
> list[Usercalendar] user_instruments_get_user_calendars(api_key, user_id)

Retrieves the list of User or Corporate Calendars.

Retrieves the list of User or Corporate Calendars.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of User or Corporate Calendars.
    api_response = api_instance.user_instruments_get_user_calendars(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_get_user_calendars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Usercalendar]**](Usercalendar.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_instruments_get_user_exchange**
> list[Userexchange] user_instruments_get_user_exchange(id, api_key, user_id)

Retrieves a specific User or Corporate Exchange.

Retrieve a specific User or Corporate Exchange.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
id = 'id_example' # str | The exchange_id.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves a specific User or Corporate Exchange.
    api_response = api_instance.user_instruments_get_user_exchange(id, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_get_user_exchange: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The exchange_id. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Userexchange]**](Userexchange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_instruments_get_user_exchange_instrument**
> list[Userexchangeinstrument] user_instruments_get_user_exchange_instrument(id, instrument, api_key, user_id)

Retrieves a specific Instrument for a User or Corporate Exchange.

Retrieves a specific Instrument for a User or Corporate Exchange.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
id = 'id_example' # str | The exchange_id.
instrument = 'instrument_example' # str | The Instrument symbol.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves a specific Instrument for a User or Corporate Exchange.
    api_response = api_instance.user_instruments_get_user_exchange_instrument(id, instrument, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_get_user_exchange_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The exchange_id. | 
 **instrument** | **str**| The Instrument symbol. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Userexchangeinstrument]**](Userexchangeinstrument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_instruments_get_user_exchange_instruments**
> list[Userexchangeinstrument] user_instruments_get_user_exchange_instruments(id, api_key, user_id)

Retrieves the list of Instruments for a User or Corporate Exchange.

Retrieves the list of Instruments for a User or Corporate Exchange.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
id = 'id_example' # str | The exchange_id.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Instruments for a User or Corporate Exchange.
    api_response = api_instance.user_instruments_get_user_exchange_instruments(id, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_get_user_exchange_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The exchange_id. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Userexchangeinstrument]**](Userexchangeinstrument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_instruments_get_user_exchanges**
> list[Userexchange] user_instruments_get_user_exchanges(api_key, user_id)

Retrieves the list of User and Corporate Exchanges.

Retrieve the list of User and Corporate Exchanges.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of User and Corporate Exchanges.
    api_response = api_instance.user_instruments_get_user_exchanges(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_get_user_exchanges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Userexchange]**](Userexchange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_instruments_get_user_instrument_price_history**
> list[Userexchangeinstrument] user_instruments_get_user_instrument_price_history(id, instrument, api_key, user_id)

Retrieves price history for a specific User or Corporate Instrument.

Retrieves price history for a specific User or Corporate Instrument.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
id = 'id_example' # str | The exchange_id.
instrument = 'instrument_example' # str | The Instrument symbol.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves price history for a specific User or Corporate Instrument.
    api_response = api_instance.user_instruments_get_user_instrument_price_history(id, instrument, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_get_user_instrument_price_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The exchange_id. | 
 **instrument** | **str**| The Instrument symbol. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Userexchangeinstrument]**](Userexchangeinstrument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_instruments_get_user_instrument_splits**
> list[Userinstrumentsplit] user_instruments_get_user_instrument_splits(id, instrument, api_key, user_id)

Retrieves Splits for a specific User or Corporate Instrument.

Retrieves Splits for a specific User or Corporate Instrument.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
id = 'id_example' # str | The exchange_id.
instrument = 'instrument_example' # str | The Instrument symbol.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves Splits for a specific User or Corporate Instrument.
    api_response = api_instance.user_instruments_get_user_instrument_splits(id, instrument, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_get_user_instrument_splits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The exchange_id. | 
 **instrument** | **str**| The Instrument symbol. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Userinstrumentsplit]**](Userinstrumentsplit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_instruments_post_user_calendar**
> Object user_instruments_post_user_calendar(calendar, api_key, user_id)

Adds a new User or Corporate Calendar.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
calendar = profitspi-sdk.Usercalendar() # Usercalendar | 
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Adds a new User or Corporate Calendar.
    api_response = api_instance.user_instruments_post_user_calendar(calendar, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_post_user_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar** | [**Usercalendar**](Usercalendar.md)|  | 
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

# **user_instruments_post_user_calendar_holidays**
> Object user_instruments_post_user_calendar_holidays(id, holidays, api_key, user_id)

Adds one or more new Holidays to a User or Corporate Calendar.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
id = 56 # int | The calendar_id.
holidays = [profitspi-sdk.Usercalendarholiday()] # list[Usercalendarholiday] | 
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Adds one or more new Holidays to a User or Corporate Calendar.
    api_response = api_instance.user_instruments_post_user_calendar_holidays(id, holidays, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_post_user_calendar_holidays: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The calendar_id. | 
 **holidays** | [**list[Usercalendarholiday]**](Usercalendarholiday.md)|  | 
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

# **user_instruments_post_user_exchange**
> Object user_instruments_post_user_exchange(exchange, api_key, user_id)

Adds a new User or Corporate Exchange.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
exchange = profitspi-sdk.Userexchange() # Userexchange | 
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Adds a new User or Corporate Exchange.
    api_response = api_instance.user_instruments_post_user_exchange(exchange, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_post_user_exchange: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange** | [**Userexchange**](Userexchange.md)|  | 
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

# **user_instruments_post_user_exchange_instrument**
> Object user_instruments_post_user_exchange_instrument(id, instrument, api_key, user_id)

Adds a new Instrument to a User or Corporate Exchange.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
id = 'id_example' # str | The exchange_id.
instrument = profitspi-sdk.Userexchangeinstrument() # Userexchangeinstrument | 
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Adds a new Instrument to a User or Corporate Exchange.
    api_response = api_instance.user_instruments_post_user_exchange_instrument(id, instrument, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_post_user_exchange_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The exchange_id. | 
 **instrument** | [**Userexchangeinstrument**](Userexchangeinstrument.md)|  | 
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

# **user_instruments_post_user_instrument_price_history**
> Object user_instruments_post_user_instrument_price_history(id, instrument, pricehistory, api_key, user_id)

Adds / replaces price history for a User or Corporate Instrument.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
id = 'id_example' # str | The exchange_id.
instrument = 'instrument_example' # str | The Instrument symbol.
pricehistory = [profitspi-sdk.Userinstrumentpricehistory()] # list[Userinstrumentpricehistory] | 
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Adds / replaces price history for a User or Corporate Instrument.
    api_response = api_instance.user_instruments_post_user_instrument_price_history(id, instrument, pricehistory, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_post_user_instrument_price_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The exchange_id. | 
 **instrument** | **str**| The Instrument symbol. | 
 **pricehistory** | [**list[Userinstrumentpricehistory]**](Userinstrumentpricehistory.md)|  | 
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

# **user_instruments_post_user_instrument_splits**
> Object user_instruments_post_user_instrument_splits(id, instrument, splits, api_key, user_id)

Adds one or more Splits to a Corporate Instrument.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
id = 'id_example' # str | The exchange_id.
instrument = 'instrument_example' # str | The Instrument symbol.
splits = [profitspi-sdk.Userinstrumentsplit()] # list[Userinstrumentsplit] | 
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Adds one or more Splits to a Corporate Instrument.
    api_response = api_instance.user_instruments_post_user_instrument_splits(id, instrument, splits, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_post_user_instrument_splits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The exchange_id. | 
 **instrument** | **str**| The Instrument symbol. | 
 **splits** | [**list[Userinstrumentsplit]**](Userinstrumentsplit.md)|  | 
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

# **user_instruments_put_exchange**
> Object user_instruments_put_exchange(id, exchange, api_key, user_id)

Updates a User or Corporate Exchange.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
id = 'id_example' # str | The exchange_id.
exchange = profitspi-sdk.Userexchange() # Userexchange | 
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Updates a User or Corporate Exchange.
    api_response = api_instance.user_instruments_put_exchange(id, exchange, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_put_exchange: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The exchange_id. | 
 **exchange** | [**Userexchange**](Userexchange.md)|  | 
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

# **user_instruments_put_user_calendar**
> Object user_instruments_put_user_calendar(id, calendar, api_key, user_id)

Updates a User or Corporate Calendar.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
id = 56 # int | The calendar_id.
calendar = profitspi-sdk.Usercalendar() # Usercalendar | 
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Updates a User or Corporate Calendar.
    api_response = api_instance.user_instruments_put_user_calendar(id, calendar, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_put_user_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The calendar_id. | 
 **calendar** | [**Usercalendar**](Usercalendar.md)|  | 
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

# **user_instruments_put_user_exchange_instrument**
> Object user_instruments_put_user_exchange_instrument(id, instrument, userexchangeinstrument, api_key, user_id)

Updates a specific Instrument for a User or Corporate Exchange.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.UserInstrumentsApi()
id = 'id_example' # str | The exchange_id.
instrument = 'instrument_example' # str | The Instrument symbol.
userexchangeinstrument = profitspi-sdk.Userexchangeinstrument() # Userexchangeinstrument | 
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Updates a specific Instrument for a User or Corporate Exchange.
    api_response = api_instance.user_instruments_put_user_exchange_instrument(id, instrument, userexchangeinstrument, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInstrumentsApi->user_instruments_put_user_exchange_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The exchange_id. | 
 **instrument** | **str**| The Instrument symbol. | 
 **userexchangeinstrument** | [**Userexchangeinstrument**](Userexchangeinstrument.md)|  | 
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

