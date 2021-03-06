path: blob/master/src/hexpy
source:  models.py

Data Validation
===============

[Pydantic Style Classes](https://pydantic-docs.helpmanual.io/) for validating data for [Custom Content Upload](Upload.md#upload) and [BrightView Training](Monitor.md#train_monitor)

## `UploadItem`
Validation model for an item of custom content to be uploaded. Checks for required fields, with valid types and formatting.

### Fields
* title: String, Document Title
* url: Url, Unique Document Url,
* guid: String, Unique Document Identifier
* author: String, Document Author
* language: String, 2 letter langauge code
* date: String, Date or Datetime
* contents: String, Document text (max length 16384 characters)
* geolocation: Optional Mapping Identifier
* custom: Optinal Mapping of key value string pairs
* age: Optional Integer
* gender: Optional gender M/F
* pageId: Optional String
* parentGuid: Optional String
* authorProfileID: Optional String
* engagementType: Optional String REPLY/RETWEET/COMMENT

### Example Usage
<div class="termy">

```python
>>> from hexpy.models import UploadItem
>>> item_dict = {
    "date": "2010-01-26T16:14:00",
    "contents": "Example content",
    "guid": "This is my guid",
    "title": "Example Title",
    "author": "me",
    "language": "en",
    "gender": "F",
    "geolocation": {
        "id": "USA.NY"
    },
    "pageId": "This is a pageId",
    "parentGuid": "123123",
    "authorProfileId": "1234567",
    "custom": {
        "field0": "value0",
        "field1": "45.2",
        "field2": "123",
        "field3": "value3",
        "field4": "value4",
        "field5": "5_stars",
        "field6": "1200",
        "field7": "5",
        "field8": "value5",
        "field9": "value6"
    }
}
>>> upload_item = UploadItem(**item_dict)
```
</div>

## `UploadCollection`
Validation model for collection of items to be uploaded. Checks for duplicate upload items, easily convert to/from dataframe

### Fields
* items: List of UploadItems or valid dictionaries

### Example Usage
<div class="termy">

```python
>>> from hexpy.models import UploadItem, UploadCollection
>>> items = [
    {
        "date": "2010-01-26T16:14:00",
        "contents": "Example content",
        "guid": "This is my guid",
        "title": "Example Title",
        "author": "me",
        "language": "en",
        "gender": "F",
        "geolocation": {
            "id": "USA.NY"
        },
        "pageId": "This is a pageId",
        "parentGuid": "123123",
        "authorProfileId": "1234567",
        "custom": {
            "field0": "value0",
            "field1": "45.2",
            "field2": "123",
            "field3": "value3",
            "field4": "value4",
            "field5": "5_stars",
            "field6": "1200",
            "field7": "5",
            "field8": "value5",
            "field9": "value6"
        }
    }
]
>>> upload_collection = UploadCollection(items=items)
```
</div>

### Methods

### from_dataframe
```python
from_dataframe(df: pd.DataFrame) -> UploadCollection
```
Create UploadCollection from pandas DataFrame containing necessary fields.

#### Arguments:
* df: pd.DataFrame

### to_dataframe
 ```python
 to_dataframe() -> pd.DataFrame
 ```
 Convert UploadCollection to pandas Dataframe with one colume for each field.

## `TrainItem`
Validation model for training post to be uploaded. Checks for required fields, with valid types and formatting.

### Fields
* type: String, Custom Content Type Name
* title: String, Document Title
* url: Url, Unique Document Url
* author: String, Document Author
* language: String, 2 letter langauge code
* date: String, Date or Datetime
* contents: String, Document Body
* categoryid: Integer of Category defined in Monitor

### Example Usage
<div class="termy">

```python
>>> from hexpy.models import TrainItem
>>> item_dict = {
    "title": "Example Title",
    "date": "2010-01-26T16:14:00",
    "author": "me",
    "url": "http://www.crimsonhexagon.com/post1",
    "contents": "Example content",
    "language": "en",
    "categoryid": 9107252649,
}
>>> train_item = TrainItem(**item)
```
</div>

## `TrainCollection`
Validation model for collections of training posts to be uploaded. Checks for duplicate training posts, easily convert to/from dataframe


### Fields
* items: List of TrainItems or valid dictionaries

### Example Usage
<div class="termy">

```python
>>> from hexpy.models import TrainItem, TrainCollection
>>> items = [
    {
        "title": "Example Title",
        "date": "2010-01-26T16:14:00",
        "author": "me",
        "url": "http://www.crimsonhexagon.com/post1",
        "contents": "Example content",
        "language": "en",
        "categoryid": 9107252649,
    }
]
>>> train_collection = TrainCollection(items=items])
```
</div>

### Methods

### from_dataframe
```python
from_dataframe(df: pd.DataFrame) -> TrainCollection
```
Create TrainCollection from pandas DataFrame containing necessary fields.

#### Arguments:
* df: pd.DataFrame

### to_dataframe
 ```python
 to_dataframe() -> pd.DataFrame
 ```
 Convert TrainCollection to pandas Dataframe with one colume for each field.

## `AnalysisRequest`
Model for submitting valid analysis request via [AnalysisAPI](Analysis.md#analysis_request)

### Fields
* analysis: List of analysis type strings
* keywords: String of boolean logic
* sources: List of source strings
* startDate: Datetime String
* endDate: Datetime String
* timezone: String
* requestUsage: Boolean
* gender: Optional include/exclude and array of gender strings
* languages: Optional include/exclude and array of language strings
* locations: Optional include/exclude and array of location strings

### Example Usage
<div class="termy">

```python
>>> from hexpy.models import AnalysisRequest
>>> request_dict = {
    "analysis": [
        "volume",
        "sentiment",
        "emotion",
        "affinity",
        "gender",
        "age",
        "location",
        "source",
        "reach"
    ],
    "keywords": "iPhone",
    "languages": {
        "type": "include",
        "values": [
            "EN"
        ]
    },
    "gender": {
        "type": "include",
        "values": [
            "M"
        ]
    },
    "locations": {
        "type": "exclude",
        "values": [
            "JPN"
        ]
    },
    "sources": [
        "TWITTER",
        "TUMBLR",
        "INSTAGRAM",
        "BLOGS",
        "REVIEWS",
        "GOOGLE_PLUS",
        "NEWS",
        "YOUTUBE",
        "FORUMS"
    ],
    "startDate": "2016-09-20T00:00:00+00:00",
    "endDate": "2016-09-21T00:00:00+00:00",
    "timezone": "America/New_York",
    "requestUsage": True
}

>>> analysis_request = AnalysisRequest(**request_dict)
```
</div>