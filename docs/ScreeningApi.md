# profitspi-sdk.ScreeningApi

All URIs are relative to *https://www.profitspi.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**screening_delete_screen**](ScreeningApi.md#screening_delete_screen) | **DELETE** /screens/{id} | Deletes a User Screen.
[**screening_get_default_screen**](ScreeningApi.md#screening_get_default_screen) | **GET** /defaultscreens/{id} | Retrieves the definition and results for a Default Screen.
[**screening_get_default_screens**](ScreeningApi.md#screening_get_default_screens) | **GET** /defaultscreens | Retrieves the list of Default Screens.
[**screening_get_user_screen_additional_items**](ScreeningApi.md#screening_get_user_screen_additional_items) | **GET** /screens/{id}/additionalresultitems | Retrieves the additional result items definition only for a User Screen.
[**screening_get_user_screen_criteria**](ScreeningApi.md#screening_get_user_screen_criteria) | **GET** /screens/{id}/criteria | Retrieves the criteria definition only for a User Screen.
[**screening_get_user_screen_results**](ScreeningApi.md#screening_get_user_screen_results) | **GET** /screens/{id}/results | Retrieves the results only for a User Screen.
[**screening_get_user_screens**](ScreeningApi.md#screening_get_user_screens) | **GET** /screens | Retrieves the list of Screens for a User.
[**screening_get_user_screens_0**](ScreeningApi.md#screening_get_user_screens_0) | **GET** /screens/{id} | Retrieves the definition and results for a User Screen.
[**screening_post_screen**](ScreeningApi.md#screening_post_screen) | **POST** /screens | Adds a new User Screen.
[**screening_put_screen**](ScreeningApi.md#screening_put_screen) | **PUT** /screens/{id} | Updates a User Screen.


# **screening_delete_screen**
> Object screening_delete_screen(id, api_key, user_id)

Deletes a User Screen.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ScreeningApi()
id = 56 # int | The screen_id from the User Screens API.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Deletes a User Screen.
    api_response = api_instance.screening_delete_screen(id, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningApi->screening_delete_screen: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The screen_id from the User Screens API. | 
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

# **screening_get_default_screen**
> Screen screening_get_default_screen(id, api_key, user_id, screen_date=screen_date, per_page=per_page, page=page)

Retrieves the definition and results for a Default Screen.

Returns the definition and results for a Default Screen. View the results or use the definition to create a User Screen.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ScreeningApi()
id = 56 # int | The screen_id from the Default Screens API.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.
screen_date = '2013-10-20T19:20:30+01:00' # datetime | A date in the format yyyy-mm-dd to backdate the screen. Default is latest date. (optional)
per_page = 56 # int | The page size for the results. Default is 100. (optional)
page = 56 # int | A specific page when paging thru the results. Default is 0. (optional)

try:
    # Retrieves the definition and results for a Default Screen.
    api_response = api_instance.screening_get_default_screen(id, api_key, user_id, screen_date=screen_date, per_page=per_page, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningApi->screening_get_default_screen: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The screen_id from the Default Screens API. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 
 **screen_date** | **datetime**| A date in the format yyyy-mm-dd to backdate the screen. Default is latest date. | [optional] 
 **per_page** | **int**| The page size for the results. Default is 100. | [optional] 
 **page** | **int**| A specific page when paging thru the results. Default is 0. | [optional] 

### Return type

[**Screen**](Screen.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **screening_get_default_screens**
> list[Defaultscreen] screening_get_default_screens(api_key, user_id)

Retrieves the list of Default Screens.

Returns a list of Default Screens with summary information.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ScreeningApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Default Screens.
    api_response = api_instance.screening_get_default_screens(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningApi->screening_get_default_screens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Defaultscreen]**](Defaultscreen.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **screening_get_user_screen_additional_items**
> Additionalresultitems screening_get_user_screen_additional_items(id, api_key, user_id)

Retrieves the additional result items definition only for a User Screen.

Returns the additional results items definition for a User Screen.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ScreeningApi()
id = 56 # int | The screen_id from the User Screens API.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the additional result items definition only for a User Screen.
    api_response = api_instance.screening_get_user_screen_additional_items(id, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningApi->screening_get_user_screen_additional_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The screen_id from the User Screens API. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**Additionalresultitems**](Additionalresultitems.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **screening_get_user_screen_criteria**
> Criteriapair screening_get_user_screen_criteria(id, api_key, user_id)

Retrieves the criteria definition only for a User Screen.

Returns the criteria definition for a User Screen.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ScreeningApi()
id = 56 # int | The screen_id from the User Screens API.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the criteria definition only for a User Screen.
    api_response = api_instance.screening_get_user_screen_criteria(id, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningApi->screening_get_user_screen_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The screen_id from the User Screens API. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**Criteriapair**](Criteriapair.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **screening_get_user_screen_results**
> Screenresult screening_get_user_screen_results(id, api_key, user_id, screen_date=screen_date, per_page=per_page, page=page)

Retrieves the results only for a User Screen.

Returns the results for a User Screen.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ScreeningApi()
id = 56 # int | The screen_id from the User Screens API.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.
screen_date = '2013-10-20T19:20:30+01:00' # datetime | A date in the format yyyy-mm-dd to backdate the screen. Default is latest date. (optional)
per_page = 56 # int | The page size for the results. Default is 100. (optional)
page = 56 # int | A specific page when paging thru the results. Default is 0. (optional)

try:
    # Retrieves the results only for a User Screen.
    api_response = api_instance.screening_get_user_screen_results(id, api_key, user_id, screen_date=screen_date, per_page=per_page, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningApi->screening_get_user_screen_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The screen_id from the User Screens API. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 
 **screen_date** | **datetime**| A date in the format yyyy-mm-dd to backdate the screen. Default is latest date. | [optional] 
 **per_page** | **int**| The page size for the results. Default is 100. | [optional] 
 **page** | **int**| A specific page when paging thru the results. Default is 0. | [optional] 

### Return type

[**Screenresult**](Screenresult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **screening_get_user_screens**
> list[Userscreen] screening_get_user_screens(api_key, user_id)

Retrieves the list of Screens for a User.

Returns a list of Screens for a User with summary information.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ScreeningApi()
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Retrieves the list of Screens for a User.
    api_response = api_instance.screening_get_user_screens(api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningApi->screening_get_user_screens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 

### Return type

[**list[Userscreen]**](Userscreen.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **screening_get_user_screens_0**
> Screen screening_get_user_screens_0(id, api_key, user_id, screen_date=screen_date, per_page=per_page, page=page)

Retrieves the definition and results for a User Screen.

Returns the definition and results for a User Screen. View the results or use the definition to create another User Screen.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ScreeningApi()
id = 56 # int | The screen_id from the User Screens API.
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.
screen_date = '2013-10-20T19:20:30+01:00' # datetime | A date in the format yyyy-mm-dd to backdate the screen. Default is latest date. (optional)
per_page = 56 # int | The page size for the results. Default is 100. (optional)
page = 56 # int | A specific page when paging thru the results. Default is 0. (optional)

try:
    # Retrieves the definition and results for a User Screen.
    api_response = api_instance.screening_get_user_screens_0(id, api_key, user_id, screen_date=screen_date, per_page=per_page, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningApi->screening_get_user_screens_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The screen_id from the User Screens API. | 
 **api_key** | **str**| The unique key provided to you by Profitspi.com. | 
 **user_id** | **str**| The unique id identifying the user. | 
 **screen_date** | **datetime**| A date in the format yyyy-mm-dd to backdate the screen. Default is latest date. | [optional] 
 **per_page** | **int**| The page size for the results. Default is 100. | [optional] 
 **page** | **int**| A specific page when paging thru the results. Default is 0. | [optional] 

### Return type

[**Screen**](Screen.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **screening_post_screen**
> Object screening_post_screen(screen, api_key, user_id)

Adds a new User Screen.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ScreeningApi()
screen = profitspi-sdk.Screen() # Screen | 
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Adds a new User Screen.
    api_response = api_instance.screening_post_screen(screen, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningApi->screening_post_screen: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screen** | [**Screen**](Screen.md)|  | 
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

# **screening_put_screen**
> Object screening_put_screen(id, screen, api_key, user_id)

Updates a User Screen.

### Example
```python
from __future__ import print_function
import time
import profitspi-sdk
from profitspi-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = profitspi-sdk.ScreeningApi()
id = 56 # int | The screen_id from the User Screens API.
screen = profitspi-sdk.Screen() # Screen | 
api_key = 'api_key_example' # str | The unique key provided to you by Profitspi.com.
user_id = 'user_id_example' # str | The unique id identifying the user.

try:
    # Updates a User Screen.
    api_response = api_instance.screening_put_screen(id, screen, api_key, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningApi->screening_put_screen: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The screen_id from the User Screens API. | 
 **screen** | [**Screen**](Screen.md)|  | 
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

