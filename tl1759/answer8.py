Dict = {'first':[2,1],'second':[2,3],'third':[3,4]}
value3 = Dict['first']
Dict['first'] = Dict['third']
Dict['third'] = value3
# print Dict
Dict['third'].sort()
Dict['fourth'] = Dict['second']
# print Dict
del Dict['second']
print Dict
