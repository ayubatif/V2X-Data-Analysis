#!/usr/bin/env python
import json

# string format json test time logs
jsonTimeStr3 = '[{"TOTAL":1000,"ALL_AVG_TQR":95,"ALL_AVG_TPR":10,"PSEUDO_RATE":10,"NOT_AVG_TPR":10,"NOT_AVG_TQR":94,"ALL_AVG_TSQ":42,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":91,"ALL_AVG_TPR":8,"PSEUDO_RATE":30,"NOT_AVG_TPR":8,"NOT_AVG_TQR":90,"ALL_AVG_TSQ":41,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":92,"ALL_AVG_TPR":8,"PSEUDO_RATE":60,"NOT_AVG_TPR":8,"NOT_AVG_TQR":91,"ALL_AVG_TSQ":41,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":92,"ALL_AVG_TPR":8,"PSEUDO_RATE":90,"NOT_AVG_TPR":8,"NOT_AVG_TQR":91,"ALL_AVG_TSQ":42,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":91,"ALL_AVG_TPR":8,"PSEUDO_RATE":120,"NOT_AVG_TPR":8,"NOT_AVG_TQR":90,"ALL_AVG_TSQ":42,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":92,"ALL_AVG_TPR":8,"PSEUDO_RATE":180,"NOT_AVG_TPR":8,"NOT_AVG_TQR":91,"ALL_AVG_TSQ":41,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":7,"PSEUDO_RATE":240,"NOT_AVG_TPR":7,"NOT_AVG_TQR":92,"ALL_AVG_TSQ":42,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":101,"ALL_AVG_TPR":8,"PSEUDO_RATE":300,"NOT_AVG_TPR":8,"NOT_AVG_TQR":100,"ALL_AVG_TSQ":43,"NOT_AVG_TSQ":42},{"TOTAL":1000,"ALL_AVG_TQR":105,"ALL_AVG_TPR":8,"PSEUDO_RATE":720,"NOT_AVG_TPR":8,"NOT_AVG_TQR":104,"ALL_AVG_TSQ":43,"NOT_AVG_TSQ":43},{"TOTAL":1000,"ALL_AVG_TQR":97,"ALL_AVG_TPR":7,"PSEUDO_RATE":1000,"NOT_AVG_TPR":7,"NOT_AVG_TQR":96,"ALL_AVG_TSQ":43,"NOT_AVG_TSQ":42}]'
jsonTimeStr4 = '[{"TOTAL":1000,"ALL_AVG_TQR":63,"ALL_AVG_TPR":8,"PSEUDO_RATE":10,"NOT_AVG_TPR":8,"NOT_AVG_TQR":62,"ALL_AVG_TSQ":42,"NOT_AVG_TSQ":42},{"TOTAL":1000,"ALL_AVG_TQR":62,"ALL_AVG_TPR":6,"PSEUDO_RATE":30,"NOT_AVG_TPR":6,"NOT_AVG_TQR":61,"ALL_AVG_TSQ":41,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":62,"ALL_AVG_TPR":6,"PSEUDO_RATE":60,"NOT_AVG_TPR":6,"NOT_AVG_TQR":61,"ALL_AVG_TSQ":42,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":61,"ALL_AVG_TPR":6,"PSEUDO_RATE":90,"NOT_AVG_TPR":6,"NOT_AVG_TQR":61,"ALL_AVG_TSQ":42,"NOT_AVG_TSQ":42},{"TOTAL":1000,"ALL_AVG_TQR":63,"ALL_AVG_TPR":6,"PSEUDO_RATE":120,"NOT_AVG_TPR":6,"NOT_AVG_TQR":62,"ALL_AVG_TSQ":41,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":60,"ALL_AVG_TPR":6,"PSEUDO_RATE":180,"NOT_AVG_TPR":5,"NOT_AVG_TQR":59,"ALL_AVG_TSQ":42,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":59,"ALL_AVG_TPR":6,"PSEUDO_RATE":240,"NOT_AVG_TPR":6,"NOT_AVG_TQR":58,"ALL_AVG_TSQ":42,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":61,"ALL_AVG_TPR":5,"PSEUDO_RATE":300,"NOT_AVG_TPR":5,"NOT_AVG_TQR":60,"ALL_AVG_TSQ":42,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":61,"ALL_AVG_TPR":6,"PSEUDO_RATE":720,"NOT_AVG_TPR":6,"NOT_AVG_TQR":60,"ALL_AVG_TSQ":42,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":59,"ALL_AVG_TPR":5,"PSEUDO_RATE":1000,"NOT_AVG_TPR":5,"NOT_AVG_TQR":59,"ALL_AVG_TSQ":41,"NOT_AVG_TSQ":41}]'
jsonValStr3 = '[{"TOTAL":1562,"PSEUDO_RATE":10,"VALIDITY2":64.5966709346991,"VALIDITY1":6.402048655569782,"VALIDITY0":29.001280409731113},{"TOTAL":1554,"PSEUDO_RATE":30,"VALIDITY2":64.73616473616474,"VALIDITY1":2.1235521235521233,"VALIDITY0":33.14028314028314},{"TOTAL":1642,"PSEUDO_RATE":60,"VALIDITY2":61.14494518879415,"VALIDITY1":0.9744214372716199,"VALIDITY0":37.880633373934224},{"TOTAL":1629,"PSEUDO_RATE":90,"VALIDITY2":62.0012277470841,"VALIDITY1":0.6752608962553714,"VALIDITY0":37.323511356660525},{"TOTAL":1644,"PSEUDO_RATE":120,"VALIDITY2":61.25304136253041,"VALIDITY1":0.48661800486618007,"VALIDITY0":38.26034063260341},{"TOTAL":1619,"PSEUDO_RATE":180,"VALIDITY2":62.32242124768376,"VALIDITY1":0.3088326127239036,"VALIDITY0":37.36874613959234},{"TOTAL":1502,"PSEUDO_RATE":240,"VALIDITY2":67.17709720372837,"VALIDITY1":0.1997336884154461,"VALIDITY0":32.62316910785619},{"TOTAL":1676,"PSEUDO_RATE":300,"VALIDITY2":60.32219570405728,"VALIDITY1":0.17899761336515513,"VALIDITY0":39.498806682577566},{"TOTAL":1895,"PSEUDO_RATE":720,"VALIDITY2":53.720316622691286,"VALIDITY1":0.05277044854881266,"VALIDITY0":46.226912928759894},{"TOTAL":1610,"PSEUDO_RATE":1000,"VALIDITY2":62.732919254658384,"VALIDITY1":0,"VALIDITY0":37.267080745341616}]'
jsonValStr4 = '[{"TOTAL":1513,"PSEUDO_RATE":10,"VALIDITY2":66.82088565763384,"VALIDITY1":6.5432914738929275,"VALIDITY0":26.63582286847323},{"TOTAL":1499,"PSEUDO_RATE":30,"VALIDITY2":67.11140760507006,"VALIDITY1":2.201467645096731,"VALIDITY0":30.687124749833224},{"TOTAL":1471,"PSEUDO_RATE":60,"VALIDITY2":68.38885112168592,"VALIDITY1":1.087695445275323,"VALIDITY0":30.52345343303875},{"TOTAL":1484,"PSEUDO_RATE":90,"VALIDITY2":68.1266846361186,"VALIDITY1":0.7412398921832885,"VALIDITY0":31.132075471698112},{"TOTAL":1551,"PSEUDO_RATE":120,"VALIDITY2":64.66795615731786,"VALIDITY1":0.5157962604771116,"VALIDITY0":34.81624758220503},{"TOTAL":1454,"PSEUDO_RATE":180,"VALIDITY2":69.25722145804677,"VALIDITY1":0.34387895460797796,"VALIDITY0":30.39889958734526},{"TOTAL":1505,"PSEUDO_RATE":240,"VALIDITY2":66.84385382059801,"VALIDITY1":0.26578073089701,"VALIDITY0":32.89036544850498},{"TOTAL":1442,"PSEUDO_RATE":300,"VALIDITY2":69.97226074895978,"VALIDITY1":0.20804438280166435,"VALIDITY0":29.819694868238557},{"TOTAL":1516,"PSEUDO_RATE":720,"VALIDITY2":66.2928759894459,"VALIDITY1":0.06596306068601583,"VALIDITY0":33.64116094986807},{"TOTAL":1383,"PSEUDO_RATE":1000,"VALIDITY2":72.81272595806219,"VALIDITY1":0,"VALIDITY0":27.187274041937815}]'


# parsed json test logs
jsonTime3 = json.loads(jsonTimeStr3)
jsonTime4 = json.loads(jsonTimeStr4)
jsonVal3 = json.loads(jsonValStr3)
jsonVal4 = json.loads(jsonValStr4)

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
test3TSQs = []
test4TSQs = []

# empty TPR lists to be filled
test3TPRs = []
test4TPRs = []

# empty val lists to be filled
test3Val0 = []
test3Val1 = []
test3Val2 = []
test4Val0 = []
test4Val1 = []
test4Val2 = []

# append pseudo rates & avg times from log to lists
for testRun in jsonTime3:
    test3Rates.append(testRun['PSEUDO_RATE'])
    test3TSQs.append(testRun['ALL_AVG_TSQ'])
    test3TPRs.append(testRun['ALL_AVG_TPR'])
    test3TQRs.append(testRun['ALL_AVG_TQR']-testRun['ALL_AVG_TSQ']-testRun['ALL_AVG_TPR'])

for testRun in jsonTime4:
    test4Rates.append(testRun['PSEUDO_RATE'])
    test4TSQs.append(testRun['ALL_AVG_TSQ'])
    test4TPRs.append(testRun['ALL_AVG_TPR'])
    test4TQRs.append(testRun['ALL_AVG_TQR']-testRun['ALL_AVG_TSQ']-testRun['ALL_AVG_TPR'])

# append val results from log to lists
for testRun in jsonVal3:
    test3Val0.append(testRun['VALIDITY0'])
    test3Val1.append(testRun['VALIDITY1'])
    test3Val2.append(testRun['VALIDITY2'])

for testRun in jsonVal4:
    test4Val0.append(testRun['VALIDITY0'])
    test4Val1.append(testRun['VALIDITY1'])
    test4Val2.append(testRun['VALIDITY2'])

import numpy as np

# indep var spaced properly
N = len(test3Rates)
indpRates = np.arange(N)

# dep vars
dep3Ts = np.array(test3TSQs) # send q
dep3Tp = np.array(test3TPRs) # process r
dep3Tq = np.array(test3TQRs) # q resolved
dep3V0 = np.array(test3Val0) # outer auth fail
dep3V1 = np.array(test3Val1) # inner auth fail
dep3V2 = np.array(test3Val2) # auth success
dep4Ts = np.array(test4TSQs) # send q
dep4Tp = np.array(test4TPRs) # process r
dep4Tq = np.array(test4TQRs) # q resolved
dep4V0 = np.array(test4Val0) # outer auth fail
dep4V1 = np.array(test4Val1) # inner auth fail
dep4V2 = np.array(test4Val2) # auth success

import matplotlib.pyplot as plt
import pandas as pantelis

#test3 plots
df = pantelis.DataFrame({'Inner Auth Fail' : dep3V1, 'Outer Auth Fail' : dep3V0, 'Successful Auth' : dep3V2}, index=test3Rates)
ax = df.plot.bar(rot=0)
print(df)
plt.xlabel('Pseudonym Change Rate')
plt.ylabel('% of total Authentication Attempts')
plt.show()

timeData = []
for i in range(len(test3Rates)):
    timeData.append([dep3Ts[i], dep3Tp[i], dep3Tq[i]])

df = pantelis.DataFrame(timeData, columns = ['TSQ', 'TPR', 'TQR'])
df.plot.bar(stacked=True)
print(df)
plt.xticks(indpRates, test3Rates)
plt.xlabel('Pseudonym Change Rate')
plt.ylabel('Time in milliseconds')
plt.show()

#test4 plots
df = pantelis.DataFrame({'Inner Auth Fail' : dep4V1, 'Outer Auth Fail' : dep4V0, 'Successful Auth' : dep4V2}, index=test3Rates)
ax = df.plot.bar(rot=0)
print(df)
plt.xlabel('Pseudonym Change Rate')
plt.ylabel('% of total Authentication Attempts')
plt.show()

timeData = []
for i in range(len(test3Rates)):
    timeData.append([dep4Ts[i], dep4Tp[i], dep4Tq[i]])

df = pantelis.DataFrame(timeData, columns = ['TSQ', 'TPR', 'TQR'])
df.plot.bar(stacked=True)
print(df)
plt.xticks(indpRates, test3Rates)
plt.xlabel('Pseudonym Change Rate')
plt.ylabel('Time in milliseconds')
plt.show()


# >> LEGACY CODE: So matplotlib is great but these two plots were better handled with pandas afaik <<
# pv2 = plt.plot(indp, test3Val2)
# pv1 = plt.plot(indp, test3Val1)
# pv0 = plt.plot(indp, test3Val0)
# plt.xticks(indp, test3Rates)
# plt.xlabel('Pseudonym Change Rate')
# plt.ylabel('Authentication Attempts')
# plt.legend((pv2[0], pv1[0], pv0[0]), ('Proper Auth', 'Outer Auth Fail', 'Inner Auth Fail'))
# plt.show()

# width = 0.35      # the width of the bars: can also be len(x) sequence
# pts = plt.bar(indp, test3TSQs, width)
# ptr = plt.bar(indp, test3TPRs, width, bottom=test3TSQs)
# ptq = plt.bar(indp, test3TQRs, width, bottom=test3TPRs)
# plt.title('Categorical Plotting')
# plt.xlabel('pseudo rate / queries')
# plt.ylabel('time / s')
# plt.ylabel('Scores')
# plt.xticks(indp, test3Rates)
# plt.yticks(np.arange(0, 81, 10))
# plt.legend((pts[0], ptr[0]), ('TSQ', 'TPR', 'TQR'))
# plt.show()