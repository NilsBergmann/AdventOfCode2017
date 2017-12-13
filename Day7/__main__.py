_input = open("Day7/Input.txt", "r")
_dict = {}
for line in _input:
    arr = line.split()
    _dict[arr[0]] = {} 
    _dict[arr[0]]['weight'] = arr[1][1:-1] #remove ()
    if len(arr) >= 3: #Has children
        _dict[arr[0]]['children']=arr[3:]
    