# Rename The key Values
- **Give The List Of Keys And Values**
- **Some Keys Rename The New Key Values For Example** 
    - **city   -  location**
    - **salary -  package**
- **The New Key values To be used to the print of the list**
## sample code for rename Key values
```
sampleDict['Package'] = sampleDict.pop('salary')
sampleDict['Location'] = sampleDict.pop('city')
```
## Example OutPut for rename key values
```
The orginal keys value: {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New york'}
The new keys value: {'name': 'Kelly', 'age': 25, 'Package': 8000, 'Location': 'New york'}
```
