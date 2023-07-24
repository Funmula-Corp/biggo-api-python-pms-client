# BigGo PMS API

This is a library for accessing BigGo PMS API.

## First Step

To get started, first obtain an API key and secret from BigGo API. Then, use the following code to obtain an API object:
```python
api = BiggoAPIPMS(
  clientID = client_id, 
  clientSecret = client_secret
)
```

## Usage

### Get Platform List
Get list of platforms the user has access.  
`api.get_Platform_List()`  


```python
api.get_Platform_List()
```
---

### Get Group List
Get list of groups in the platform.  
`api.get_Group_List(<Platform ID>)`


```python
api.get_Group_List('<Platform ID>')
```
---

### Get Report List
Get list of reports in the platform.  
`api.get_Report_List('<Platform ID>', [Options])`


```python
api.get_Report_List('<Platform ID>')
```
`Options`
||required|default value|type|description|
|:---:|:---:|:---:|:---:|:---:|
|size||`5000`|int|size of report list returned|
|startIndex||`0`|int|start index of report list returned|
|sort||`desc`|`asc`\|`desc`|sort order based on report create time|
|groupID||`undefined`|str[]|filter report list by group ID|
|startDate||`undefined`|Date|filter report list by report create time|
|endDate||`undefined`|Date|filter report list by report create time|

---

### Get Report
Save report as file or get file content.  
`api.get_Report('<Platform ID>', '<Report ID>', 'json'|'csv'|'excel', [Options])`


```python
api.get_Report('<Platform ID>', '<Report ID>', 'json')
```  
`Options`  
||required|default value|type|description|
|:---:|:---:|:---:|:---:|:---:|
|saveAsFile||`false`|boolean|save report as file|
|saveDir||`.`|str|Directory to save file|
|fileName||`<Platform Name>_<Group Name>_<Report Create Time>.<Format>`|str|file name|