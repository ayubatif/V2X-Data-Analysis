#!/usr/bin/env python
import json

# string format json test time logs
jsonTimeStr3 = '[{"TOTAL":1000,"ALL_AVG_TQR":96,"ALL_AVG_TPR":10.456,"TQR_SAMPLE_STANDARD_DEVIATION":20.84581311913504,"ALL_AVG_TSQ":41.637,"TPR_STANDARD_ERROR":0.07324802960966059,"TSQ_SAMPLE_STANDARD_DEVIATION":13.065830836893719,"PSEUDO_RATE":10,"TPR_SAMPLE_STANDARD_DEVIATION":2.8828474085164064,"NOT_AVG_TPR":10.33,"NOT_AVG_TQR":95.815,"TQR_STANDARD_ERROR":0.6582159068707846,"TSQ_STANDARD_ERROR":0.4117392753216844,"NOT_AVG_TSQ":41.127},{"TOTAL":1000,"ALL_AVG_TQR":97,"ALL_AVG_TPR":9.314,"TQR_SAMPLE_STANDARD_DEVIATION":20.128207667378227,"ALL_AVG_TSQ":42.673,"TPR_STANDARD_ERROR":0.06620767721543909,"TSQ_SAMPLE_STANDARD_DEVIATION":13.771826007492509,"PSEUDO_RATE":30,"TPR_SAMPLE_STANDARD_DEVIATION":2.7529976983270545,"NOT_AVG_TPR":9.199,"NOT_AVG_TQR":96.868,"TQR_STANDARD_ERROR":0.632724786956192,"TSQ_STANDARD_ERROR":0.4301595751330895,"NOT_AVG_TSQ":42.177},{"TOTAL":1000,"ALL_AVG_TQR":95,"ALL_AVG_TPR":8.828,"TQR_SAMPLE_STANDARD_DEVIATION":19.75860293926425,"ALL_AVG_TSQ":41.885,"TPR_STANDARD_ERROR":0.06520316889217456,"TSQ_SAMPLE_STANDARD_DEVIATION":13.31754753192396,"PSEUDO_RATE":60,"TPR_SAMPLE_STANDARD_DEVIATION":2.7080909932880735,"NOT_AVG_TPR":8.704,"NOT_AVG_TQR":94.498,"TQR_STANDARD_ERROR":0.6232656653973375,"TSQ_STANDARD_ERROR":0.41884050804817263,"NOT_AVG_TSQ":41.332},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":8.233,"TQR_SAMPLE_STANDARD_DEVIATION":20.165896878100146,"ALL_AVG_TSQ":42.107,"TPR_STANDARD_ERROR":0.08624828418186917,"TSQ_SAMPLE_STANDARD_DEVIATION":13.620786142638927,"PSEUDO_RATE":90,"TPR_SAMPLE_STANDARD_DEVIATION":3.4757095441779855,"NOT_AVG_TPR":8.099,"NOT_AVG_TQR":93.852,"TQR_STANDARD_ERROR":0.635797113145119,"TSQ_STANDARD_ERROR":0.42774328134663203,"NOT_AVG_TSQ":41.576},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":8.418,"TQR_SAMPLE_STANDARD_DEVIATION":18.671513203021426,"ALL_AVG_TSQ":41.851,"TPR_STANDARD_ERROR":0.060956855838599326,"TSQ_SAMPLE_STANDARD_DEVIATION":13.77820151839674,"PSEUDO_RATE":120,"TPR_SAMPLE_STANDARD_DEVIATION":2.5088763691531035,"NOT_AVG_TPR":8.308,"NOT_AVG_TQR":93.488,"TQR_STANDARD_ERROR":0.5883893195420404,"TSQ_STANDARD_ERROR":0.4324735102016745,"NOT_AVG_TSQ":41.339},{"TOTAL":1000,"ALL_AVG_TQR":93,"ALL_AVG_TPR":8.016,"TQR_SAMPLE_STANDARD_DEVIATION":19.001073495503114,"ALL_AVG_TSQ":41.635,"TPR_STANDARD_ERROR":0.06476355767848155,"TSQ_SAMPLE_STANDARD_DEVIATION":13.611497345354866,"PSEUDO_RATE":180,"TPR_SAMPLE_STANDARD_DEVIATION":2.602657146288389,"NOT_AVG_TPR":7.909,"NOT_AVG_TQR":92.945,"TQR_STANDARD_ERROR":0.5996685621605788,"TSQ_STANDARD_ERROR":0.4285093668582234,"NOT_AVG_TSQ":41.104},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":8.236,"TQR_SAMPLE_STANDARD_DEVIATION":18.625452085890085,"ALL_AVG_TSQ":42.457,"TPR_STANDARD_ERROR":0.07749827158804148,"TSQ_SAMPLE_STANDARD_DEVIATION":13.927359193577168,"PSEUDO_RATE":240,"TPR_SAMPLE_STANDARD_DEVIATION":3.125977107288336,"NOT_AVG_TPR":8.118,"NOT_AVG_TQR":93.253,"TQR_STANDARD_ERROR":0.5860654724717639,"TSQ_STANDARD_ERROR":0.43586892298984065,"NOT_AVG_TSQ":41.924},{"TOTAL":1000,"ALL_AVG_TQR":92,"ALL_AVG_TPR":8.187,"TQR_SAMPLE_STANDARD_DEVIATION":16.489512629063828,"ALL_AVG_TSQ":41.861,"TPR_STANDARD_ERROR":0.05378125546597703,"TSQ_SAMPLE_STANDARD_DEVIATION":13.589681669144213,"PSEUDO_RATE":300,"TPR_SAMPLE_STANDARD_DEVIATION":2.213541349626743,"NOT_AVG_TPR":8.078,"NOT_AVG_TQR":91.768,"TQR_STANDARD_ERROR":0.5204044040637815,"TSQ_STANDARD_ERROR":0.42782257822921177,"NOT_AVG_TSQ":41.341},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":7.638,"TQR_SAMPLE_STANDARD_DEVIATION":19.232270815768263,"ALL_AVG_TSQ":42.502,"TPR_STANDARD_ERROR":0.07213180306169459,"TSQ_SAMPLE_STANDARD_DEVIATION":13.800718594934395,"PSEUDO_RATE":720,"TPR_SAMPLE_STANDARD_DEVIATION":2.813140319406089,"NOT_AVG_TPR":7.526,"NOT_AVG_TQR":93.171,"TQR_STANDARD_ERROR":0.6045612533257307,"TSQ_STANDARD_ERROR":0.43106202794738846,"NOT_AVG_TSQ":41.997},{"TOTAL":1000,"ALL_AVG_TQR":97,"ALL_AVG_TPR":7.843,"TQR_SAMPLE_STANDARD_DEVIATION":22.60716666747028,"ALL_AVG_TSQ":42.899,"TPR_STANDARD_ERROR":0.06864445642299069,"TSQ_SAMPLE_STANDARD_DEVIATION":14.256324897110533,"PSEUDO_RATE":1000,"TPR_SAMPLE_STANDARD_DEVIATION":2.7302895690779114,"NOT_AVG_TPR":7.73,"NOT_AVG_TQR":96.376,"TQR_STANDARD_ERROR":0.7106501954737345,"TSQ_STANDARD_ERROR":0.44529277797758937,"NOT_AVG_TSQ":42.383}]'
jsonTimeStr4 = '[{"TOTAL":1000,"ALL_AVG_TQR":91,"ALL_AVG_TPR":8.593,"TQR_SAMPLE_STANDARD_DEVIATION":14.280864941016336,"ALL_AVG_TSQ":42.001,"TPR_STANDARD_ERROR":0.04989880282555693,"TSQ_SAMPLE_STANDARD_DEVIATION":13.67382101584391,"PSEUDO_RATE":10,"TPR_SAMPLE_STANDARD_DEVIATION":2.077852296872153,"NOT_AVG_TPR":8.471,"NOT_AVG_TQR":90.815,"TQR_STANDARD_ERROR":0.45070010110825753,"TSQ_STANDARD_ERROR":0.43047140497232217,"NOT_AVG_TSQ":41.456},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":7.084,"TQR_SAMPLE_STANDARD_DEVIATION":18.080188586768717,"ALL_AVG_TSQ":43.426,"TPR_STANDARD_ERROR":0.04095597407732035,"TSQ_SAMPLE_STANDARD_DEVIATION":14.292732748003534,"PSEUDO_RATE":30,"TPR_SAMPLE_STANDARD_DEVIATION":1.6641435883478168,"NOT_AVG_TPR":6.982,"NOT_AVG_TQR":93.7,"TQR_STANDARD_ERROR":0.5666684939681328,"TSQ_STANDARD_ERROR":0.44383944359779937,"NOT_AVG_TSQ":42.931},{"TOTAL":1000,"ALL_AVG_TQR":92,"ALL_AVG_TPR":6.706,"TQR_SAMPLE_STANDARD_DEVIATION":16.16607377393144,"ALL_AVG_TSQ":41.92,"TPR_STANDARD_ERROR":0.04136985382257409,"TSQ_SAMPLE_STANDARD_DEVIATION":13.58523670389484,"PSEUDO_RATE":60,"TPR_SAMPLE_STANDARD_DEVIATION":1.6712601719216171,"NOT_AVG_TPR":6.603,"NOT_AVG_TQR":91.448,"TQR_STANDARD_ERROR":0.509689358151918,"TSQ_STANDARD_ERROR":0.42683742093450666,"NOT_AVG_TSQ":41.436},{"TOTAL":1000,"ALL_AVG_TQR":90,"ALL_AVG_TPR":6.442,"TQR_SAMPLE_STANDARD_DEVIATION":14.729368355247377,"ALL_AVG_TSQ":42.165,"TPR_STANDARD_ERROR":0.040283285484793326,"TSQ_SAMPLE_STANDARD_DEVIATION":13.912899852132172,"PSEUDO_RATE":90,"TPR_SAMPLE_STANDARD_DEVIATION":1.6123381870122273,"NOT_AVG_TPR":6.328,"NOT_AVG_TQR":89.906,"TQR_STANDARD_ERROR":0.46370154201165537,"TSQ_STANDARD_ERROR":0.4358434935039127,"NOT_AVG_TSQ":41.68},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":6.233,"TQR_SAMPLE_STANDARD_DEVIATION":21.019133188723504,"ALL_AVG_TSQ":42.199,"TPR_STANDARD_ERROR":0.04180561921406826,"TSQ_SAMPLE_STANDARD_DEVIATION":14.071756864761122,"PSEUDO_RATE":120,"TPR_SAMPLE_STANDARD_DEVIATION":1.6309550307597958,"NOT_AVG_TPR":6.102,"NOT_AVG_TQR":93.964,"TQR_STANDARD_ERROR":0.662040466565553,"TSQ_STANDARD_ERROR":0.4412531779166976,"NOT_AVG_TSQ":41.706},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":6.68,"TQR_SAMPLE_STANDARD_DEVIATION":20.18146839476337,"ALL_AVG_TSQ":42.839,"TPR_STANDARD_ERROR":0.03782062631893756,"TSQ_SAMPLE_STANDARD_DEVIATION":14.137243149789619,"PSEUDO_RATE":180,"TPR_SAMPLE_STANDARD_DEVIATION":1.5570894704192906,"NOT_AVG_TPR":6.544,"NOT_AVG_TQR":93.034,"TQR_STANDARD_ERROR":0.6359720461345615,"TSQ_STANDARD_ERROR":0.44374319546717805,"NOT_AVG_TSQ":42.338},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":6.507,"TQR_SAMPLE_STANDARD_DEVIATION":22.109886222235062,"ALL_AVG_TSQ":42.887,"TPR_STANDARD_ERROR":0.040536009609617826,"TSQ_SAMPLE_STANDARD_DEVIATION":14.392773572521621,"PSEUDO_RATE":240,"TPR_SAMPLE_STANDARD_DEVIATION":1.6619763939943308,"NOT_AVG_TPR":6.392,"NOT_AVG_TQR":93.303,"TQR_STANDARD_ERROR":0.6960507801612694,"TSQ_STANDARD_ERROR":0.4508762933485263,"NOT_AVG_TSQ":42.407},{"TOTAL":1000,"ALL_AVG_TQR":98,"ALL_AVG_TPR":6.035,"TQR_SAMPLE_STANDARD_DEVIATION":24.14801054821745,"ALL_AVG_TSQ":42.975,"TPR_STANDARD_ERROR":0.040175780672910506,"TSQ_SAMPLE_STANDARD_DEVIATION":14.392068653922367,"PSEUDO_RATE":300,"TPR_SAMPLE_STANDARD_DEVIATION":1.5678852560465972,"NOT_AVG_TPR":5.924,"NOT_AVG_TQR":97.731,"TQR_STANDARD_ERROR":0.7605908400898557,"TSQ_STANDARD_ERROR":0.4512973107318066,"NOT_AVG_TSQ":42.465},{"TOTAL":1000,"ALL_AVG_TQR":99,"ALL_AVG_TPR":6.442,"TQR_SAMPLE_STANDARD_DEVIATION":24.183243644730748,"ALL_AVG_TSQ":43.331,"TPR_STANDARD_ERROR":0.04107545096862602,"TSQ_SAMPLE_STANDARD_DEVIATION":14.441599144211056,"PSEUDO_RATE":720,"TPR_SAMPLE_STANDARD_DEVIATION":1.6644429602354034,"NOT_AVG_TPR":6.343,"NOT_AVG_TQR":98.365,"TQR_STANDARD_ERROR":0.7601937507739854,"TSQ_STANDARD_ERROR":0.4510797732077429,"NOT_AVG_TSQ":42.862},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":6.075,"TQR_SAMPLE_STANDARD_DEVIATION":21.076585757708944,"ALL_AVG_TSQ":42.267,"TPR_STANDARD_ERROR":0.03939448117345244,"TSQ_SAMPLE_STANDARD_DEVIATION":14.48700736812002,"PSEUDO_RATE":1000,"TPR_SAMPLE_STANDARD_DEVIATION":1.5693645873954105,"NOT_AVG_TPR":5.958,"NOT_AVG_TQR":93.559,"TQR_STANDARD_ERROR":0.6645096154517948,"TSQ_STANDARD_ERROR":0.45517034387002836,"NOT_AVG_TSQ":41.775}]'
jsonValStr3 = '[{"TOTAL":1628,"PSEUDO_RATE":240,"VALIDITY2":62.1007371007371,"VALIDITY1":0.2457002457002457,"VALIDITY0":37.65356265356266},{"TOTAL":1695,"PSEUDO_RATE":300,"VALIDITY2":59.29203539823009,"VALIDITY1":0.17699115044247787,"VALIDITY0":40.530973451327434},{"TOTAL":1522,"PSEUDO_RATE":720,"VALIDITY2":66.55716162943496,"VALIDITY1":0.0657030223390276,"VALIDITY0":33.37713534822602},{"TOTAL":1583,"PSEUDO_RATE":1000,"VALIDITY2":63.99241945672773,"VALIDITY1":0,"VALIDITY0":36.00758054327227}]'
jsonValStr4 = '[{"TOTAL":1735,"PSEUDO_RATE":10,"VALIDITY2":57.925072046109506,"VALIDITY1":5.648414985590778,"VALIDITY0":36.42651296829971},{"TOTAL":1652,"PSEUDO_RATE":30,"VALIDITY2":61.68280871670703,"VALIDITY1":2.0581113801452786,"VALIDITY0":36.2590799031477},{"TOTAL":1633,"PSEUDO_RATE":60,"VALIDITY2":61.66564605021433,"VALIDITY1":0.9797917942437232,"VALIDITY0":37.35456215554195},{"TOTAL":1603,"PSEUDO_RATE":90,"VALIDITY2":63.00686213349969,"VALIDITY1":0.6862133499688085,"VALIDITY0":36.3069245165315},{"TOTAL":1523,"PSEUDO_RATE":120,"VALIDITY2":66.25082074852266,"VALIDITY1":0.5252790544977018,"VALIDITY0":33.22390019697964},{"TOTAL":1696,"PSEUDO_RATE":180,"VALIDITY2":59.43396226415094,"VALIDITY1":0.3537735849056604,"VALIDITY0":40.2122641509434},{"TOTAL":1682,"PSEUDO_RATE":240,"VALIDITY2":60.04756242568371,"VALIDITY1":0.2972651605231867,"VALIDITY0":39.6551724137931},{"TOTAL":1524,"PSEUDO_RATE":300,"VALIDITY2":66.20734908136482,"VALIDITY1":0.19685039370078738,"VALIDITY0":33.59580052493438},{"TOTAL":1643,"PSEUDO_RATE":720,"VALIDITY2":61.655508216676814,"VALIDITY1":0.06086427267194157,"VALIDITY0":38.28362751065125},{"TOTAL":1588,"PSEUDO_RATE":1000,"VALIDITY2":63.413098236775824,"VALIDITY1":0,"VALIDITY0":36.58690176322418}]'

# parsed json test logs
jsonTime3 = json.loads(jsonTimeStr3)
jsonTime4 = json.loads(jsonTimeStr4)
jsonVal3 = json.loads(jsonValStr3)
jsonVal4 = json.loads(jsonValStr4)

# total time samples
totalSamples = jsonTime3[0]['TOTAL']

# empty pseudo rate lists to be filled
test3Rates = []
test4Rates = []

# empty TQR lists to be filled
test3TQRs = []
test3TQRstd = []
test4TQRs = []
test4TQRstd = []

# empty TSQ lists to be filled
test3TSQs = []
test3TSQstd = []
test4TSQs = []
test4TSQstd = []

# empty TPR lists to be filled
test3TPRs = []
test3TPRstd = []
test4TPRs = []
test4TPRstd = []

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
    test3TSQstd.append(testRun['TSQ_SAMPLE_STANDARD_DEVIATION'])
    test3TPRs.append(testRun['ALL_AVG_TPR'])
    test3TPRstd.append(testRun['TPR_SAMPLE_STANDARD_DEVIATION'])
    test3TQRs.append(testRun['ALL_AVG_TQR'])
    test3TQRstd.append(testRun['TQR_SAMPLE_STANDARD_DEVIATION'])

for testRun in jsonTime4:
    test4Rates.append(testRun['PSEUDO_RATE'])
    test4TSQs.append(testRun['ALL_AVG_TSQ'])
    test4TSQstd.append(testRun['TSQ_SAMPLE_STANDARD_DEVIATION'])
    test4TPRs.append(testRun['ALL_AVG_TPR'])
    test4TPRstd.append(testRun['TPR_SAMPLE_STANDARD_DEVIATION'])
    test4TQRs.append(testRun['ALL_AVG_TQR'])
    test4TQRstd.append(testRun['TQR_SAMPLE_STANDARD_DEVIATION'])

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
mean3Ts = np.array(test3TSQs) # send q
mean3Tp = np.array(test3TPRs) # process r
mean3Tq = np.array(test3TQRs) # q resolved

mean4Ts = np.array(test4TSQs)
mean4Tp = np.array(test4TPRs)
mean4Tq = np.array(test4TQRs)

stdev3Ts = np.array(test3TSQstd)
stdev3Tp = np.array(test3TPRstd)
stdev3Tq = np.array(test3TQRstd)

stdev4Ts = np.array(test4TSQstd)
stdev4Tp = np.array(test4TPRstd)
stdev4Tq = np.array(test4TQRstd)

mean3V0 = np.array(test3Val0) # outer auth fail
mean3V1 = np.array(test3Val1) # inner auth fail
mean3V2 = np.array(test3Val2) # auth success

mean4V0 = np.array(test4Val0)
mean4V1 = np.array(test4Val1) 
mean4V2 = np.array(test4Val2)

import math
import statistics as meaner
# the distribution of a sum of two normally distributed independent 
# variates X and Y with means and variances (μX,σ2X) and (μY,σ2Y), 
# respectively is another normal distribution

# get one time means instead of 10 because of pseudonym rates
test3MeanTSQ = meaner.mean(mean3Ts)
test3MeanTPR = meaner.mean(mean3Tp)
test3MeanTQR = meaner.mean(mean3Tq)

test4MeanTSQ = meaner.mean(mean4Ts)
test4MeanTPR = meaner.mean(mean4Tp)
test4MeanTQR = meaner.mean(mean4Tq)

# get one time stdevs instead of 10 because of pseudonym rates
def stdev_sum_vars(data):
    v = 0
    for i in range(0, len(data)):
        v += math.pow(data[i], 2)
    return math.sqrt(v)

test3stdevTSQ = stdev_sum_vars(stdev3Ts)
test3stdevTPR = stdev_sum_vars(stdev3Tp)
test3stdevTQR = stdev_sum_vars(stdev3Tq)
test4stdevTSQ = stdev_sum_vars(stdev4Ts)
test4stdevTPR = stdev_sum_vars(stdev4Tp)
test4stdevTQR = stdev_sum_vars(stdev4Tq)

from scipy.stats import norm, t

# https://www.mathsisfun.com/data/confidence-interval-calculator.html
def calculate_confidence_interval(sampleSize, stdev, confidence=0.95):
    n, s = sampleSize, stdev
    z = t.ppf((1 + confidence) / 2., n - 1)
    h = s / math.sqrt(n) * z
    return h

# https://en.wikipedia.org/wiki/Student's_t-test#Independent_two-sample_t-test
# Reject the null hypothesis that the two means are equal if |T| > t 1-α/2,freedom
def two_sample_t_test(sampleSize, mean1, mean2, stdev1, stdev2, alpha=0.05):
    x1, x2 = mean1, mean2
    sp = math.sqrt(math.pow(stdev1, 2) + math.pow(stdev2, 2) / 2)
    T = (x1 - x2) / (sp * math.sqrt(2 / sampleSize))
    freedom = 2 * sampleSize - 2
    critical = t.pdf(1-alpha/2, freedom)
    if (abs(T) > critical):
        return False
    else:
        return True

# calculate confidence intervals
CI_TQR3 = []
CI_TQR4 = []

for i in range(0,len(stdev3Tq)):
    CI_TQR3.append(calculate_confidence_interval(totalSamples, stdev3Tq[i]))
    CI_TQR4.append(calculate_confidence_interval(totalSamples, stdev4Tq[i]))

print("test3 TSQ: "+str(test3MeanTSQ)+" +- "+str(calculate_confidence_interval(totalSamples, test3stdevTSQ)))
print("test4 TSQ: "+str(test4MeanTSQ)+" +- "+str(calculate_confidence_interval(totalSamples, test4stdevTSQ)))
print("test3 TPR: "+str(test3MeanTPR)+" +- "+str(calculate_confidence_interval(totalSamples, test3stdevTPR)))
print("test4 TPR: "+str(test4MeanTPR)+" +- "+str(calculate_confidence_interval(totalSamples, test4stdevTPR)))
print("test3 TQR: "+str(test3MeanTQR)+" +- "+str(calculate_confidence_interval(totalSamples, test3stdevTQR)))
print("test4 TQR: "+str(test4MeanTQR)+" +- "+str(calculate_confidence_interval(totalSamples, test4stdevTQR)))

# test if the null hypothesis the mean TQR for test 3 and 4 are not significantly different is true
print("Null hypothesis \'TSQ diff is not significant\' is: "+str(two_sample_t_test(totalSamples, test3MeanTSQ, test4MeanTSQ, test3stdevTSQ, test4stdevTSQ)))
print("Null hypothesis \'TPR diff is not significant\' is: "+str(two_sample_t_test(totalSamples, test3MeanTPR, test4MeanTPR, test3stdevTPR, test4stdevTPR)))
print("Null hypothesis \'TQR diff is not significant\' is: "+str(two_sample_t_test(totalSamples, test3MeanTQR, test4MeanTQR, test3stdevTQR, test4stdevTQR)))

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