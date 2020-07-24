def a(sampleDict):
    print('The orginal key value:',sampleDict)
    sampleDict['Package'] = sampleDict.pop('salary')
    sampleDict['Location'] = sampleDict.pop('city')
    print('The Key value Change list is:',sampleDict)
b= {
      "name": "Kelly",
      "age":25,
      "salary": 8000,
      "city": "New york"
    }
(a(b))