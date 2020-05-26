#! /usr/bin/python
import json

# string format json test time logs
jsonStr3 = '[{"TOTAL":100,"ALL_AVG_TQR":90,"PSEUDO_RATE":10,"NOT_AVG_TQR":68},{"TOTAL":1000,"ALL_AVG_TQR":94,"PSEUDO_RATE":10,"NOT_AVG_TQR":93},{"TOTAL":1000,"ALL_AVG_TQR":93,"PSEUDO_RATE":30,"NOT_AVG_TQR":92},{"TOTAL":1000,"ALL_AVG_TQR":92,"PSEUDO_RATE":60,"NOT_AVG_TQR":91},{"TOTAL":1000,"ALL_AVG_TQR":91,"PSEUDO_RATE":90,"NOT_AVG_TQR":90},{"TOTAL":1000,"ALL_AVG_TQR":92,"PSEUDO_RATE":120,"NOT_AVG_TQR":91},{"TOTAL":1000,"ALL_AVG_TQR":93,"PSEUDO_RATE":180,"NOT_AVG_TQR":92},{"TOTAL":1000,"ALL_AVG_TQR":92,"PSEUDO_RATE":240,"NOT_AVG_TQR":91},{"TOTAL":1000,"ALL_AVG_TQR":92,"PSEUDO_RATE":300,"NOT_AVG_TQR":91},{"TOTAL":1000,"ALL_AVG_TQR":90,"PSEUDO_RATE":720,"NOT_AVG_TQR":89},{"TOTAL":1000,"ALL_AVG_TQR":90,"PSEUDO_RATE":1000,"NOT_AVG_TQR":89}]'
jsonStr4 = '[{"TOTAL":100,"ALL_AVG_TQR":78,"PSEUDO_RATE":10,"NOT_AVG_TQR":58},{"TOTAL":1000,"ALL_AVG_TQR":62,"PSEUDO_RATE":10,"NOT_AVG_TQR":61},{"TOTAL":1000,"ALL_AVG_TQR":60,"PSEUDO_RATE":30,"NOT_AVG_TQR":59},{"TOTAL":1000,"ALL_AVG_TQR":59,"PSEUDO_RATE":60,"NOT_AVG_TQR":58},{"TOTAL":1000,"ALL_AVG_TQR":60,"PSEUDO_RATE":90,"NOT_AVG_TQR":59},{"TOTAL":1000,"ALL_AVG_TQR":59,"PSEUDO_RATE":120,"NOT_AVG_TQR":58},{"TOTAL":1000,"ALL_AVG_TQR":59,"PSEUDO_RATE":180,"NOT_AVG_TQR":58},{"TOTAL":1000,"ALL_AVG_TQR":58,"PSEUDO_RATE":240,"NOT_AVG_TQR":57},{"TOTAL":1000,"ALL_AVG_TQR":60,"PSEUDO_RATE":300,"NOT_AVG_TQR":59},{"TOTAL":1000,"ALL_AVG_TQR":59,"PSEUDO_RATE":720,"NOT_AVG_TQR":58},{"TOTAL":1000,"ALL_AVG_TQR":58,"PSEUDO_RATE":1000,"NOT_AVG_TQR":57}]'

# parsed json test time logs
json3 = json.loads(jsonStr3)
json4 = json.loads(jsonStr4)

# print json logs
# print(json3[3])
# print(json4[5])

# empty pseudo rate lists to be filled
test3Rates = []
test4Rates = []

# empty TQR lists to be filled
test3TQRs = []
test4TQRs = []

# empty TSQ lists to be filled
test3TSQ = []
test4TSQ = []

# empty TPR lists to be filled
test3TPR = []
test4TPR = []

# append pseudo rates & avg times from log to lists
for testRun in json3:
    test3Rates.append(testRun['PSEUDO_RATE'])
    test3TQRs.append(testRun['ALL_AVG_TQR'])
    # test3TSQs.append(testRun['ALL_AVG_TSQ'])
    # test3TPRs.append(testRun['ALL_AVG_TPR'])

for testRun in json4:
    test4Rates.append(testRun['PSEUDO_RATE'])
    test4TQRs.append(testRun['ALL_AVG_TQR'])
    # test4TSQs.append(testRun['ALL_AVG_TSQ'])
    # test4TPRs.append(testRun['ALL_AVG_TPR'])

print(test3Rates)
print(test4Rates)
print(test3TQRs)
print(test4TQRs)
# print(test3TSQs)
# print(test4TSQs)
# print(test3TPRs)
# print(test4TPRs)

