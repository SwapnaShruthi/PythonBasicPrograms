myDict={1:'apple',2:'ball','animal':'cat'}
print(myDict[2])
print(len(myDict))
print(myDict.keys())
print(myDict.values())
print(myDict.items())
print(myDict.get('animal'))
print(myDict['animal'])

myDict.update({'animal':'doll'})
print(myDict)
print(myDict.pop(2))
print(myDict)
