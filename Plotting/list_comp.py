#!/usr/bin/env python
import json

# string format json test time logs
jsonTimeStr3 = '[{"TOTAL":1000,"ALL_AVG_TQR":96,"ALL_AVG_TPR":10.456,"TQR_SAMPLE_STANDARD_DEVIATION":20.84581311913504,"ALL_AVG_TSQ":41.637,"TPR_STANDARD_ERROR":0.07324802960966059,"TSQ_SAMPLE_STANDARD_DEVIATION":13.065830836893719,"PSEUDO_RATE":10,"TPR_SAMPLE_STANDARD_DEVIATION":2.8828474085164064,"NOT_AVG_TPR":10.33,"NOT_AVG_TQR":95.815,"TQR_STANDARD_ERROR":0.6582159068707846,"TSQ_STANDARD_ERROR":0.4117392753216844,"NOT_AVG_TSQ":41.127},{"TOTAL":1000,"ALL_AVG_TQR":97,"ALL_AVG_TPR":9.314,"TQR_SAMPLE_STANDARD_DEVIATION":20.128207667378227,"ALL_AVG_TSQ":42.673,"TPR_STANDARD_ERROR":0.06620767721543909,"TSQ_SAMPLE_STANDARD_DEVIATION":13.771826007492509,"PSEUDO_RATE":30,"TPR_SAMPLE_STANDARD_DEVIATION":2.7529976983270545,"NOT_AVG_TPR":9.199,"NOT_AVG_TQR":96.868,"TQR_STANDARD_ERROR":0.632724786956192,"TSQ_STANDARD_ERROR":0.4301595751330895,"NOT_AVG_TSQ":42.177},{"TOTAL":1000,"ALL_AVG_TQR":95,"ALL_AVG_TPR":8.828,"TQR_SAMPLE_STANDARD_DEVIATION":19.75860293926425,"ALL_AVG_TSQ":41.885,"TPR_STANDARD_ERROR":0.06520316889217456,"TSQ_SAMPLE_STANDARD_DEVIATION":13.31754753192396,"PSEUDO_RATE":60,"TPR_SAMPLE_STANDARD_DEVIATION":2.7080909932880735,"NOT_AVG_TPR":8.704,"NOT_AVG_TQR":94.498,"TQR_STANDARD_ERROR":0.6232656653973375,"TSQ_STANDARD_ERROR":0.41884050804817263,"NOT_AVG_TSQ":41.332},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":8.233,"TQR_SAMPLE_STANDARD_DEVIATION":20.165896878100146,"ALL_AVG_TSQ":42.107,"TPR_STANDARD_ERROR":0.08624828418186917,"TSQ_SAMPLE_STANDARD_DEVIATION":13.620786142638927,"PSEUDO_RATE":90,"TPR_SAMPLE_STANDARD_DEVIATION":3.4757095441779855,"NOT_AVG_TPR":8.099,"NOT_AVG_TQR":93.852,"TQR_STANDARD_ERROR":0.635797113145119,"TSQ_STANDARD_ERROR":0.42774328134663203,"NOT_AVG_TSQ":41.576},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":8.418,"TQR_SAMPLE_STANDARD_DEVIATION":18.671513203021426,"ALL_AVG_TSQ":41.851,"TPR_STANDARD_ERROR":0.060956855838599326,"TSQ_SAMPLE_STANDARD_DEVIATION":13.77820151839674,"PSEUDO_RATE":120,"TPR_SAMPLE_STANDARD_DEVIATION":2.5088763691531035,"NOT_AVG_TPR":8.308,"NOT_AVG_TQR":93.488,"TQR_STANDARD_ERROR":0.5883893195420404,"TSQ_STANDARD_ERROR":0.4324735102016745,"NOT_AVG_TSQ":41.339},{"TOTAL":1000,"ALL_AVG_TQR":93,"ALL_AVG_TPR":8.016,"TQR_SAMPLE_STANDARD_DEVIATION":19.001073495503114,"ALL_AVG_TSQ":41.635,"TPR_STANDARD_ERROR":0.06476355767848155,"TSQ_SAMPLE_STANDARD_DEVIATION":13.611497345354866,"PSEUDO_RATE":180,"TPR_SAMPLE_STANDARD_DEVIATION":2.602657146288389,"NOT_AVG_TPR":7.909,"NOT_AVG_TQR":92.945,"TQR_STANDARD_ERROR":0.5996685621605788,"TSQ_STANDARD_ERROR":0.4285093668582234,"NOT_AVG_TSQ":41.104},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":8.236,"TQR_SAMPLE_STANDARD_DEVIATION":18.625452085890085,"ALL_AVG_TSQ":42.457,"TPR_STANDARD_ERROR":0.07749827158804148,"TSQ_SAMPLE_STANDARD_DEVIATION":13.927359193577168,"PSEUDO_RATE":240,"TPR_SAMPLE_STANDARD_DEVIATION":3.125977107288336,"NOT_AVG_TPR":8.118,"NOT_AVG_TQR":93.253,"TQR_STANDARD_ERROR":0.5860654724717639,"TSQ_STANDARD_ERROR":0.43586892298984065,"NOT_AVG_TSQ":41.924},{"TOTAL":1000,"ALL_AVG_TQR":92,"ALL_AVG_TPR":8.187,"TQR_SAMPLE_STANDARD_DEVIATION":16.489512629063828,"ALL_AVG_TSQ":41.861,"TPR_STANDARD_ERROR":0.05378125546597703,"TSQ_SAMPLE_STANDARD_DEVIATION":13.589681669144213,"PSEUDO_RATE":300,"TPR_SAMPLE_STANDARD_DEVIATION":2.213541349626743,"NOT_AVG_TPR":8.078,"NOT_AVG_TQR":91.768,"TQR_STANDARD_ERROR":0.5204044040637815,"TSQ_STANDARD_ERROR":0.42782257822921177,"NOT_AVG_TSQ":41.341},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":7.638,"TQR_SAMPLE_STANDARD_DEVIATION":19.232270815768263,"ALL_AVG_TSQ":42.502,"TPR_STANDARD_ERROR":0.07213180306169459,"TSQ_SAMPLE_STANDARD_DEVIATION":13.800718594934395,"PSEUDO_RATE":720,"TPR_SAMPLE_STANDARD_DEVIATION":2.813140319406089,"NOT_AVG_TPR":7.526,"NOT_AVG_TQR":93.171,"TQR_STANDARD_ERROR":0.6045612533257307,"TSQ_STANDARD_ERROR":0.43106202794738846,"NOT_AVG_TSQ":41.997},{"TOTAL":1000,"ALL_AVG_TQR":97,"ALL_AVG_TPR":7.843,"TQR_SAMPLE_STANDARD_DEVIATION":22.60716666747028,"ALL_AVG_TSQ":42.899,"TPR_STANDARD_ERROR":0.06864445642299069,"TSQ_SAMPLE_STANDARD_DEVIATION":14.256324897110533,"PSEUDO_RATE":1000,"TPR_SAMPLE_STANDARD_DEVIATION":2.7302895690779114,"NOT_AVG_TPR":7.73,"NOT_AVG_TQR":96.376,"TQR_STANDARD_ERROR":0.7106501954737345,"TSQ_STANDARD_ERROR":0.44529277797758937,"NOT_AVG_TSQ":42.383}]'
jsonTimeStr4 = '[{"TOTAL":1000,"ALL_AVG_TQR":63,"ALL_AVG_TPR":8,"PSEUDO_RATE":10,"NOT_AVG_TPR":8,"NOT_AVG_TQR":62,"ALL_AVG_TSQ":42,"NOT_AVG_TSQ":42},{"TOTAL":1000,"ALL_AVG_TQR":62,"ALL_AVG_TPR":6,"PSEUDO_RATE":30,"NOT_AVG_TPR":6,"NOT_AVG_TQR":61,"ALL_AVG_TSQ":41,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":62,"ALL_AVG_TPR":6,"PSEUDO_RATE":60,"NOT_AVG_TPR":6,"NOT_AVG_TQR":61,"ALL_AVG_TSQ":42,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":61,"ALL_AVG_TPR":6,"PSEUDO_RATE":90,"NOT_AVG_TPR":6,"NOT_AVG_TQR":61,"ALL_AVG_TSQ":42,"NOT_AVG_TSQ":42},{"TOTAL":1000,"ALL_AVG_TQR":63,"ALL_AVG_TPR":6,"PSEUDO_RATE":120,"NOT_AVG_TPR":6,"NOT_AVG_TQR":62,"ALL_AVG_TSQ":41,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":60,"ALL_AVG_TPR":6,"PSEUDO_RATE":180,"NOT_AVG_TPR":5,"NOT_AVG_TQR":59,"ALL_AVG_TSQ":42,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":59,"ALL_AVG_TPR":6,"PSEUDO_RATE":240,"NOT_AVG_TPR":6,"NOT_AVG_TQR":58,"ALL_AVG_TSQ":42,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":61,"ALL_AVG_TPR":5,"PSEUDO_RATE":300,"NOT_AVG_TPR":5,"NOT_AVG_TQR":60,"ALL_AVG_TSQ":42,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":61,"ALL_AVG_TPR":6,"PSEUDO_RATE":720,"NOT_AVG_TPR":6,"NOT_AVG_TQR":60,"ALL_AVG_TSQ":42,"NOT_AVG_TSQ":41},{"TOTAL":1000,"ALL_AVG_TQR":59,"ALL_AVG_TPR":5,"PSEUDO_RATE":1000,"NOT_AVG_TPR":5,"NOT_AVG_TQR":59,"ALL_AVG_TSQ":41,"NOT_AVG_TSQ":41}]'
jsonValStr3 = '[{"TOTAL":1550,"PSEUDO_RATE":10,"VALIDITY2":64.77419354838709,"VALIDITY1":6.387096774193549,"VALIDITY0":28.838709677419356},{"TOTAL":1730,"PSEUDO_RATE":30,"VALIDITY2":58.554913294797686,"VALIDITY1":1.907514450867052,"VALIDITY0":39.53757225433526},{"TOTAL":1726,"PSEUDO_RATE":60,"VALIDITY2":58.28505214368482,"VALIDITY1":0.9269988412514484,"VALIDITY0":40.78794901506373},{"TOTAL":1625,"PSEUDO_RATE":90,"VALIDITY2":61.96923076923076,"VALIDITY1":0.6153846153846154,"VALIDITY0":37.41538461538462},{"TOTAL":1695,"PSEUDO_RATE":120,"VALIDITY2":59.469026548672566,"VALIDITY1":0.471976401179941,"VALIDITY0":40.0589970501475},{"TOTAL":1616,"PSEUDO_RATE":180,"VALIDITY2":62.190594059405946,"VALIDITY1":0.3094059405940594,"VALIDITY0":37.5},{"TOTAL":1628,"PSEUDO_RATE":240,"VALIDITY2":62.1007371007371,"VALIDITY1":0.2457002457002457,"VALIDITY0":37.65356265356266},{"TOTAL":1695,"PSEUDO_RATE":300,"VALIDITY2":59.29203539823009,"VALIDITY1":0.17699115044247787,"VALIDITY0":40.530973451327434},{"TOTAL":1522,"PSEUDO_RATE":720,"VALIDITY2":66.55716162943496,"VALIDITY1":0.0657030223390276,"VALIDITY0":33.37713534822602},{"TOTAL":1583,"PSEUDO_RATE":1000,"VALIDITY2":63.99241945672773,"VALIDITY1":0,"VALIDITY0":36.00758054327227}]'
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
percentTicks = range(0, 110, 10)

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

import scipy.stats as stats

def mean_confidence_interval(data, confidence=0.9999999999):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), stats.sem(a)
    h = se * stats.t.ppf((1 + confidence) / 2., n-1)
    return -h, +h

import matplotlib.pyplot as plt
import pandas as pantelis

# #test3 auth plot
# df = pantelis.DataFrame({'Inner Auth Fail' : dep3V1, 'Outer Auth Fail' : dep3V0, 'Successful Auth' : dep3V2}, index=test3Rates)
# ax = df.plot.bar(rot=0)
# print(df)
# plt.xticks(indpRates, test3Rates)
# plt.yticks(percentTicks)
# plt.xlabel('Pseudonym Change Rate')
# plt.ylabel('% of total Authentication Attempts')
# plt.grid(color='black', which='major', axis='y', linestyle='dotted')
# plt.show()

# #test4 auth plot
# df = pantelis.DataFrame({'Inner Auth Fail' : dep4V1, 'Outer Auth Fail' : dep4V0, 'Successful Auth' : dep4V2}, index=test3Rates)
# ax = df.plot.bar(rot=0)
# print(df)
# plt.xticks(indpRates, test3Rates)
# plt.yticks(percentTicks)
# plt.xlabel('Pseudonym Change Rate')
# plt.ylabel('% of total Authentication Attempts')
# plt.grid(color='black', which='major', axis='y', linestyle='dotted')
# plt.show()

#test3 time plot

## >> Testing <<

# timeData = []
# for i in range(len(test3Rates)):
#     timeData.append([dep3Ts[i], dep3Tp[i], dep3Tq[i]])

# df = pantelis.DataFrame(timeData, columns = ['TSQ', 'TPR', 'TQR'])

# # calc the 95% confidence intervals
# tsqCI = mean_confidence_interval(df['TSQ'])
# tprCI = mean_confidence_interval(df['TPR'])
# tqrCI = mean_confidence_interval(df['TQR'])

# print(tsqCI[1])
# print(tprCI )
# print(tqrCI)

# df.plot.bar(stacked=True, yerr=1)
# print(df)

# plt.xticks(indpRates, test3Rates)
# plt.xlabel('Pseudonym Change Rate')
# plt.ylabel('Time in milliseconds')
# plt.show()

# #test4 time plot
# timeData = []
# for i in range(len(test3Rates)):
#     timeData.append([dep4Ts[i], dep4Tp[i], dep4Tq[i]])

# df = pantelis.DataFrame(timeData, columns = ['TSQ', 'TPR', 'TQR'])
# df.plot.bar(stacked=True)
# print(df)
# plt.xticks(indpRates, test3Rates)
# plt.xlabel('Pseudonym Change Rate')
# plt.ylabel('Time in milliseconds')
# plt.show()

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