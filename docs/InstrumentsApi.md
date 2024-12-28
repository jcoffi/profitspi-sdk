# profitspi-sdk.InstrumentsApi

All URIs are relative to *https://www.profitspi.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instruments_get_instrument_group_item_instruments**](InstrumentsApi.md#instruments_get_instrument_group_item_instruments) | **GET** /instrumentgroups/{id}/{item}/instruments | Retrieves the list of Instruments for a specific Instrument Group Item together with adhoc technical indicators.
[**instruments_get_instrument_group_item_sub_types**](InstrumentsApi.md#instruments_get_instrument_group_item_sub_types) | **GET** /instrumentgroups/{id}/{item}/subtypes | Retrieves the list of different subtypes for a specific Instrument Group Item.
[**instruments_get_instrument_groups**](InstrumentsApi.md#instruments_get_instrument_groups) | **GET** /instrumentgroups | Retrieves the list of different types of Instrument Groups.
[**instruments_get_instrument_groups_0**](InstrumentsApi.md#instruments_get_instrument_groups_0) | **GET** /instrumentgroups/{id} | Retrieves the list of different items for a specific Instrument Group.
[**instruments_get_instrument_history**](InstrumentsApi.md#instruments_get_instrument_history) | **GET** /instrumenthistory/{id} | Retrieves historic data for a specific Instrument together with adhoc technical indicators.
[**instruments_get_instrument_search_instruments**](InstrumentsApi.md#instruments_get_instrument_search_instruments) | **GET** /instrumentsearch/{search} | Retrieves the list of Instruments matching a search string together with adhoc technical indicators.


# **instruments_get_instrument_group_item_instruments**
> Instrumentgroupiteminstruments instruments_get_instrument_group_item_instruments(id, item, api_key, user_id, history_date=history_date, per_page=per_page, page=page, av_0=av_0, av_1=av_1, av_2=av_2, av_3=av_3, av_4=av_4, av_5=av_5, av_6=av_6, av_7=av_7, av_8=av_8, av_9=av_9)

Retrieves the list of Instruments for a specific Instrument Group Item together with adhoc technical indicators.

Returns a list of Instruments with their Name and Exchange for a specific Instrument Group Item. Eg Exchange NASDAQ.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.InstrumentsApi()
id = 'id_example' # str | The instrument_group_id from the Instrument Groups API.
item = 'item_example' # str | The instrument_group_item_id from the Instrument Group Items API.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.
history_date = '2013-10-20T19:20:30+01:00' # datetime | A date in the format yyyy-mm-dd to backdate the search. Default is latest date. (optional)
per_page = 56 # int | The page size for the results. Default is 100. (optional)
page = 56 # int | A specific page when paging thru the results. Default is 0. (optional)
av_0 = 'av_0_example' # str | Specify adhoc Indicator values to be included in the results together with optional Parameters, Period, Offset and Custom Inputs. For example: av_0=CLOSE&amp;av_1=BBUPPER(30 2)&amp;av_2=WEEKLY BBUPPER(30 2)[-1]&amp;av_3=WEEKLY SMA(VOLUME 20) (optional)
av_1 = 'av_1_example' # str |  (optional)
av_2 = 'av_2_example' # str |  (optional)
av_3 = 'av_3_example' # str |  (optional)
av_4 = 'av_4_example' # str |  (optional)
av_5 = 'av_5_example' # str |  (optional)
av_6 = 'av_6_example' # str |  (optional)
av_7 = 'av_7_example' # str |  (optional)
av_8 = 'av_8_example' # str |  (optional)
av_9 = 'av_9_example' # str |  (optional)

try:
    # Retrieves the list of Instruments for a specific Instrument Group Item together with adhoc technical indicators.
    api_response = api_instance.instruments_get_instrument_group_item_instruments(id, item, api_key, user_id, history_date=history_date, per_page=per_page, page=page, av_0=av_0, av_1=av_1, av_2=av_2, av_3=av_3, av_4=av_4, av_5=av_5, av_6=av_6, av_7=av_7, av_8=av_8, av_9=av_9)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->instruments_get_instrument_group_item_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The instrument_group_id from the Instrument Groups API. | 
 **item** | **str**| The instrument_group_item_id from the Instrument Group Items API. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 
 **history_date** | **datetime**| A date in the format yyyy-mm-dd to backdate the search. Default is latest date. | [optional] 
 **per_page** | **int**| The page size for the results. Default is 100. | [optional] 
 **page** | **int**| A specific page when paging thru the results. Default is 0. | [optional] 
 **av_0** | **str**| Specify adhoc Indicator values to be included in the results together with optional Parameters, Period, Offset and Custom Inputs. For example: av_0&#x3D;CLOSE&amp;amp;av_1&#x3D;BBUPPER(30 2)&amp;amp;av_2&#x3D;WEEKLY BBUPPER(30 2)[-1]&amp;amp;av_3&#x3D;WEEKLY SMA(VOLUME 20) | [optional] 
 **av_1** | **str**|  | [optional] 
 **av_2** | **str**|  | [optional] 
 **av_3** | **str**|  | [optional] 
 **av_4** | **str**|  | [optional] 
 **av_5** | **str**|  | [optional] 
 **av_6** | **str**|  | [optional] 
 **av_7** | **str**|  | [optional] 
 **av_8** | **str**|  | [optional] 
 **av_9** | **str**|  | [optional] 

### Return type

[**Instrumentgroupiteminstruments**](Instrumentgroupiteminstruments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instruments_get_instrument_group_item_sub_types**
> list[Instrumentgroupitemsubtype] instruments_get_instrument_group_item_sub_types(id, item, api_key, user_id)

Retrieves the list of different subtypes for a specific Instrument Group Item.

Returns a list of Instrument Group Item Subtypes with their descriptions. Only some Items have Subtypes.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.InstrumentsApi()
id = 'id_example' # str | The instrument_group_id from the Instrument Groups API.
item = 'item_example' # str | The instrument_group_item_id from the Instrument Group Items API.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of different subtypes for a specific Instrument Group Item.
    api_response = api_instance.instruments_get_instrument_group_item_sub_types(id, item, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->instruments_get_instrument_group_item_sub_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The instrument_group_id from the Instrument Groups API. | 
 **item** | **str**| The instrument_group_item_id from the Instrument Group Items API. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Instrumentgroupitemsubtype]**](Instrumentgroupitemsubtype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instruments_get_instrument_groups**
> list[Instrumentgroup] instruments_get_instrument_groups(api_key, user_id)

Retrieves the list of different types of Instrument Groups.

Instrument Groups are used to group related Instruments. The different Types include Exchange and Sector.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.InstrumentsApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of different types of Instrument Groups.
    api_response = api_instance.instruments_get_instrument_groups(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->instruments_get_instrument_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Instrumentgroup]**](Instrumentgroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instruments_get_instrument_groups_0**
> list[Instrumentgroupitem] instruments_get_instrument_groups_0(id, api_key, user_id)

Retrieves the list of different items for a specific Instrument Group.

Retrieve the different Items for a specific Instrument Group. Eg the Exchange group includes NASDAQ, NYSE, etc.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.InstrumentsApi()
id = 'id_example' # str | The instrument_group_id from the Instrument Groups API.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of different items for a specific Instrument Group.
    api_response = api_instance.instruments_get_instrument_groups_0(id, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->instruments_get_instrument_groups_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The instrument_group_id from the Instrument Groups API. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Instrumentgroupitem]**](Instrumentgroupitem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instruments_get_instrument_history**
> Instrumenthistory instruments_get_instrument_history(id, api_key, user_id, begin_date=begin_date, end_date=end_date, period_type=period_type, per_page=per_page, page=page, av_0=av_0, av_1=av_1, av_2=av_2, av_3=av_3, av_4=av_4, av_5=av_5, av_6=av_6, av_7=av_7, av_8=av_8, av_9=av_9)

Retrieves historic data for a specific Instrument together with adhoc technical indicators.

Retrieve historical data for a specific Instrument.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.InstrumentsApi()
id = 'id_example' # str | The instrument_id. Eg AAPL
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.
begin_date = '2013-10-20T19:20:30+01:00' # datetime | A date in the format yyyy-mm-dd to restrict the search. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | A date in the format yyyy-mm-dd to restrict the search. (optional)
period_type = 'period_type_example' # str | Use \"W\" for Weekly, \"M\" for Monthly, \"Y\" for Yearly. Default is \"D\" for Daily (optional)
per_page = 56 # int | The page size for the results. Default is 100. (optional)
page = 56 # int | A specific page when paging thru the results. Default is 0. (optional)
av_0 = 'av_0_example' # str | Specify adhoc Indicator values to be included in the results together with optional Parameters, Period, Offset and Custom Inputs. For example: av_0=CLOSE&amp;av_1=BBUPPER(30 2)&amp;av_2=WEEKLY BBUPPER(30 2)[-1]&amp;av_3=WEEKLY SMA(VOLUME 20) (optional)
av_1 = 'av_1_example' # str |  (optional)
av_2 = 'av_2_example' # str |  (optional)
av_3 = 'av_3_example' # str |  (optional)
av_4 = 'av_4_example' # str |  (optional)
av_5 = 'av_5_example' # str |  (optional)
av_6 = 'av_6_example' # str |  (optional)
av_7 = 'av_7_example' # str |  (optional)
av_8 = 'av_8_example' # str |  (optional)
av_9 = 'av_9_example' # str |  (optional)

try:
    # Retrieves historic data for a specific Instrument together with adhoc technical indicators.
    api_response = api_instance.instruments_get_instrument_history(id, api_key, user_id, begin_date=begin_date, end_date=end_date, period_type=period_type, per_page=per_page, page=page, av_0=av_0, av_1=av_1, av_2=av_2, av_3=av_3, av_4=av_4, av_5=av_5, av_6=av_6, av_7=av_7, av_8=av_8, av_9=av_9)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->instruments_get_instrument_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The instrument_id. Eg AAPL | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 
 **begin_date** | **datetime**| A date in the format yyyy-mm-dd to restrict the search. | [optional] 
 **end_date** | **datetime**| A date in the format yyyy-mm-dd to restrict the search. | [optional] 
 **period_type** | **str**| Use \&quot;W\&quot; for Weekly, \&quot;M\&quot; for Monthly, \&quot;Y\&quot; for Yearly. Default is \&quot;D\&quot; for Daily | [optional] 
 **per_page** | **int**| The page size for the results. Default is 100. | [optional] 
 **page** | **int**| A specific page when paging thru the results. Default is 0. | [optional] 
 **av_0** | **str**| Specify adhoc Indicator values to be included in the results together with optional Parameters, Period, Offset and Custom Inputs. For example: av_0&#x3D;CLOSE&amp;amp;av_1&#x3D;BBUPPER(30 2)&amp;amp;av_2&#x3D;WEEKLY BBUPPER(30 2)[-1]&amp;amp;av_3&#x3D;WEEKLY SMA(VOLUME 20) | [optional] 
 **av_1** | **str**|  | [optional] 
 **av_2** | **str**|  | [optional] 
 **av_3** | **str**|  | [optional] 
 **av_4** | **str**|  | [optional] 
 **av_5** | **str**|  | [optional] 
 **av_6** | **str**|  | [optional] 
 **av_7** | **str**|  | [optional] 
 **av_8** | **str**|  | [optional] 
 **av_9** | **str**|  | [optional] 

### Return type

[**Instrumenthistory**](Instrumenthistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instruments_get_instrument_search_instruments**
> Instrumentsearchinstruments instruments_get_instrument_search_instruments(search, api_key, user_id, history_date=history_date, per_page=per_page, page=page, av_0=av_0, av_1=av_1, av_2=av_2, av_3=av_3, av_4=av_4, av_5=av_5, av_6=av_6, av_7=av_7, av_8=av_8, av_9=av_9)

Retrieves the list of Instruments matching a search string together with adhoc technical indicators.

Search for Instruments that have the search string in their Instrument symbol or Name.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.InstrumentsApi()
search = 'search_example' # str | The string to be used for the search. Eg BANK
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.
history_date = '2013-10-20T19:20:30+01:00' # datetime | A date in the format yyyy-mm-dd to backdate the search. Default is latest date. (optional)
per_page = 56 # int | The page size for the results. Default is 100. (optional)
page = 56 # int | A specific page when paging thru the results. Default is 0. (optional)
av_0 = 'av_0_example' # str | Specify adhoc Indicator values to be included in the results together with optional Parameters, Period, Offset and Custom Inputs. For example: av_0=CLOSE&amp;av_1=BBUPPER(30 2)&amp;av_2=WEEKLY BBUPPER(30 2)[-1]&amp;av_3=WEEKLY SMA(VOLUME 20) (optional)
av_1 = 'av_1_example' # str |  (optional)
av_2 = 'av_2_example' # str |  (optional)
av_3 = 'av_3_example' # str |  (optional)
av_4 = 'av_4_example' # str |  (optional)
av_5 = 'av_5_example' # str |  (optional)
av_6 = 'av_6_example' # str |  (optional)
av_7 = 'av_7_example' # str |  (optional)
av_8 = 'av_8_example' # str |  (optional)
av_9 = 'av_9_example' # str |  (optional)

try:
    # Retrieves the list of Instruments matching a search string together with adhoc technical indicators.
    api_response = api_instance.instruments_get_instrument_search_instruments(search, api_key, user_id, history_date=history_date, per_page=per_page, page=page, av_0=av_0, av_1=av_1, av_2=av_2, av_3=av_3, av_4=av_4, av_5=av_5, av_6=av_6, av_7=av_7, av_8=av_8, av_9=av_9)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->instruments_get_instrument_search_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| The string to be used for the search. Eg BANK | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 
 **history_date** | **datetime**| A date in the format yyyy-mm-dd to backdate the search. Default is latest date. | [optional] 
 **per_page** | **int**| The page size for the results. Default is 100. | [optional] 
 **page** | **int**| A specific page when paging thru the results. Default is 0. | [optional] 
 **av_0** | **str**| Specify adhoc Indicator values to be included in the results together with optional Parameters, Period, Offset and Custom Inputs. For example: av_0&#x3D;CLOSE&amp;amp;av_1&#x3D;BBUPPER(30 2)&amp;amp;av_2&#x3D;WEEKLY BBUPPER(30 2)[-1]&amp;amp;av_3&#x3D;WEEKLY SMA(VOLUME 20) | [optional] 
 **av_1** | **str**|  | [optional] 
 **av_2** | **str**|  | [optional] 
 **av_3** | **str**|  | [optional] 
 **av_4** | **str**|  | [optional] 
 **av_5** | **str**|  | [optional] 
 **av_6** | **str**|  | [optional] 
 **av_7** | **str**|  | [optional] 
 **av_8** | **str**|  | [optional] 
 **av_9** | **str**|  | [optional] 

### Return type

[**Instrumentsearchinstruments**](Instrumentsearchinstruments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

