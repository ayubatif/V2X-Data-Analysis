#!/usr/bin/env python
import json

# string format json test time logs
jsonDataStr1 = '[{"TOTAL":1002,"DATA2":0,"DATA1":60.67864271457086,"DATA0":39.321357285429144}]'
jsonDataStr2 = '[{"TOTAL":1009,"DATA2":0,"DATA1":0,"DATA0":100}]'
jsonDataStr3 = '[{"TOTAL":1004,"PSEUDO_RATE":10,"DATA2":0,"DATA1":0,"DATA0":100},{"TOTAL":1013,"PSEUDO_RATE":30,"DATA2":0,"DATA1":0,"DATA0":100},{"TOTAL":1006,"PSEUDO_RATE":60,"DATA2":0,"DATA1":0,"DATA0":100},{"TOTAL":1007,"PSEUDO_RATE":90,"DATA2":0,"DATA1":0,"DATA0":100},{"TOTAL":1008,"PSEUDO_RATE":120,"DATA2":0,"DATA1":0,"DATA0":100},{"TOTAL":1005,"PSEUDO_RATE":180,"DATA2":0,"DATA1":0,"DATA0":100},{"TOTAL":1011,"PSEUDO_RATE":240,"DATA2":0,"DATA1":0,"DATA0":100},{"TOTAL":1005,"PSEUDO_RATE":300,"DATA2":0,"DATA1":0,"DATA0":100},{"TOTAL":1013,"PSEUDO_RATE":720,"DATA2":0,"DATA1":0,"DATA0":100},{"TOTAL":1013,"PSEUDO_RATE":1000,"DATA2":0,"DATA1":0,"DATA0":100}]'
jsonDataStr4 = '[{"TOTAL":1008,"PSEUDO_RATE":10,"DATA2":0,"DATA1":0,"DATA0":100},{"TOTAL":1010,"PSEUDO_RATE":30,"DATA2":0,"DATA1":0,"DATA0":100},{"TOTAL":1005,"PSEUDO_RATE":60,"DATA2":0,"DATA1":0,"DATA0":100},{"TOTAL":1004,"PSEUDO_RATE":90,"DATA2":0,"DATA1":0,"DATA0":100},{"TOTAL":1010,"PSEUDO_RATE":120,"DATA2":0,"DATA1":0,"DATA0":100},{"TOTAL":1012,"PSEUDO_RATE":180,"DATA2":0,"DATA1":0,"DATA0":100},{"TOTAL":1011,"PSEUDO_RATE":240,"DATA2":0,"DATA1":0,"DATA0":100},{"TOTAL":1005,"PSEUDO_RATE":300,"DATA2":0,"DATA1":0,"DATA0":100},{"TOTAL":1015,"PSEUDO_RATE":720,"DATA2":0,"DATA1":0,"DATA0":100},{"TOTAL":1008,"PSEUDO_RATE":1000,"DATA2":0,"DATA1":0,"DATA0":100}]'
jsonTimeStr1 = '[{"TOTAL":1000,"ALL_AVG_TQR":4,"ALL_AVG_TPR":0.582,"TQR_SAMPLE_STANDARD_DEVIATION":9.748330585240703,"ALL_AVG_TSQ":2.201,"TPR_STANDARD_ERROR":0.031589330447903644,"TSQ_SAMPLE_STANDARD_DEVIATION":1.4900842851804346,"TPR_SAMPLE_STANDARD_DEVIATION":0.6262340765813634,"NOT_AVG_TPR":0.558,"NOT_AVG_TQR":4.626,"TQR_STANDARD_ERROR":0.49173822966269864,"TSQ_STANDARD_ERROR":0.04705008019973274,"NOT_AVG_TSQ":2.071}]'
jsonTimeStr2 = '[{"TOTAL":1000,"ALL_AVG_TQR":60,"ALL_AVG_TPR":5.018,"TQR_SAMPLE_STANDARD_DEVIATION":19.42167861601677,"ALL_AVG_TSQ":41.988,"TPR_STANDARD_ERROR":0.038794456126370405,"TSQ_SAMPLE_STANDARD_DEVIATION":13.101399250025933,"TPR_SAMPLE_STANDARD_DEVIATION":1.487907743864932,"NOT_AVG_TPR":4.858,"NOT_AVG_TQR":59.493,"TQR_STANDARD_ERROR":0.6117253769214464,"TSQ_STANDARD_ERROR":0.41082532265082017,"NOT_AVG_TSQ":41.327}]'
jsonTimeStr3 = '[{"TOTAL":1000,"ALL_AVG_TQR":96,"ALL_AVG_TPR":10.456,"TQR_SAMPLE_STANDARD_DEVIATION":20.84581311913504,"ALL_AVG_TSQ":41.637,"TPR_STANDARD_ERROR":0.07324802960966059,"TSQ_SAMPLE_STANDARD_DEVIATION":13.065830836893719,"PSEUDO_RATE":10,"TPR_SAMPLE_STANDARD_DEVIATION":2.8828474085164064,"NOT_AVG_TPR":10.33,"NOT_AVG_TQR":95.815,"TQR_STANDARD_ERROR":0.6582159068707846,"TSQ_STANDARD_ERROR":0.4117392753216844,"NOT_AVG_TSQ":41.127},{"TOTAL":1000,"ALL_AVG_TQR":97,"ALL_AVG_TPR":9.314,"TQR_SAMPLE_STANDARD_DEVIATION":20.128207667378227,"ALL_AVG_TSQ":42.673,"TPR_STANDARD_ERROR":0.06620767721543909,"TSQ_SAMPLE_STANDARD_DEVIATION":13.771826007492509,"PSEUDO_RATE":30,"TPR_SAMPLE_STANDARD_DEVIATION":2.7529976983270545,"NOT_AVG_TPR":9.199,"NOT_AVG_TQR":96.868,"TQR_STANDARD_ERROR":0.632724786956192,"TSQ_STANDARD_ERROR":0.4301595751330895,"NOT_AVG_TSQ":42.177},{"TOTAL":1000,"ALL_AVG_TQR":95,"ALL_AVG_TPR":8.828,"TQR_SAMPLE_STANDARD_DEVIATION":19.75860293926425,"ALL_AVG_TSQ":41.885,"TPR_STANDARD_ERROR":0.06520316889217456,"TSQ_SAMPLE_STANDARD_DEVIATION":13.31754753192396,"PSEUDO_RATE":60,"TPR_SAMPLE_STANDARD_DEVIATION":2.7080909932880735,"NOT_AVG_TPR":8.704,"NOT_AVG_TQR":94.498,"TQR_STANDARD_ERROR":0.6232656653973375,"TSQ_STANDARD_ERROR":0.41884050804817263,"NOT_AVG_TSQ":41.332},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":8.233,"TQR_SAMPLE_STANDARD_DEVIATION":20.165896878100146,"ALL_AVG_TSQ":42.107,"TPR_STANDARD_ERROR":0.08624828418186917,"TSQ_SAMPLE_STANDARD_DEVIATION":13.620786142638927,"PSEUDO_RATE":90,"TPR_SAMPLE_STANDARD_DEVIATION":3.4757095441779855,"NOT_AVG_TPR":8.099,"NOT_AVG_TQR":93.852,"TQR_STANDARD_ERROR":0.635797113145119,"TSQ_STANDARD_ERROR":0.42774328134663203,"NOT_AVG_TSQ":41.576},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":8.418,"TQR_SAMPLE_STANDARD_DEVIATION":18.671513203021426,"ALL_AVG_TSQ":41.851,"TPR_STANDARD_ERROR":0.060956855838599326,"TSQ_SAMPLE_STANDARD_DEVIATION":13.77820151839674,"PSEUDO_RATE":120,"TPR_SAMPLE_STANDARD_DEVIATION":2.5088763691531035,"NOT_AVG_TPR":8.308,"NOT_AVG_TQR":93.488,"TQR_STANDARD_ERROR":0.5883893195420404,"TSQ_STANDARD_ERROR":0.4324735102016745,"NOT_AVG_TSQ":41.339},{"TOTAL":1000,"ALL_AVG_TQR":93,"ALL_AVG_TPR":8.016,"TQR_SAMPLE_STANDARD_DEVIATION":19.001073495503114,"ALL_AVG_TSQ":41.635,"TPR_STANDARD_ERROR":0.06476355767848155,"TSQ_SAMPLE_STANDARD_DEVIATION":13.611497345354866,"PSEUDO_RATE":180,"TPR_SAMPLE_STANDARD_DEVIATION":2.602657146288389,"NOT_AVG_TPR":7.909,"NOT_AVG_TQR":92.945,"TQR_STANDARD_ERROR":0.5996685621605788,"TSQ_STANDARD_ERROR":0.4285093668582234,"NOT_AVG_TSQ":41.104},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":8.236,"TQR_SAMPLE_STANDARD_DEVIATION":18.625452085890085,"ALL_AVG_TSQ":42.457,"TPR_STANDARD_ERROR":0.07749827158804148,"TSQ_SAMPLE_STANDARD_DEVIATION":13.927359193577168,"PSEUDO_RATE":240,"TPR_SAMPLE_STANDARD_DEVIATION":3.125977107288336,"NOT_AVG_TPR":8.118,"NOT_AVG_TQR":93.253,"TQR_STANDARD_ERROR":0.5860654724717639,"TSQ_STANDARD_ERROR":0.43586892298984065,"NOT_AVG_TSQ":41.924},{"TOTAL":1000,"ALL_AVG_TQR":92,"ALL_AVG_TPR":8.187,"TQR_SAMPLE_STANDARD_DEVIATION":16.489512629063828,"ALL_AVG_TSQ":41.861,"TPR_STANDARD_ERROR":0.05378125546597703,"TSQ_SAMPLE_STANDARD_DEVIATION":13.589681669144213,"PSEUDO_RATE":300,"TPR_SAMPLE_STANDARD_DEVIATION":2.213541349626743,"NOT_AVG_TPR":8.078,"NOT_AVG_TQR":91.768,"TQR_STANDARD_ERROR":0.5204044040637815,"TSQ_STANDARD_ERROR":0.42782257822921177,"NOT_AVG_TSQ":41.341},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":7.638,"TQR_SAMPLE_STANDARD_DEVIATION":19.232270815768263,"ALL_AVG_TSQ":42.502,"TPR_STANDARD_ERROR":0.07213180306169459,"TSQ_SAMPLE_STANDARD_DEVIATION":13.800718594934395,"PSEUDO_RATE":720,"TPR_SAMPLE_STANDARD_DEVIATION":2.813140319406089,"NOT_AVG_TPR":7.526,"NOT_AVG_TQR":93.171,"TQR_STANDARD_ERROR":0.6045612533257307,"TSQ_STANDARD_ERROR":0.43106202794738846,"NOT_AVG_TSQ":41.997},{"TOTAL":1000,"ALL_AVG_TQR":97,"ALL_AVG_TPR":7.843,"TQR_SAMPLE_STANDARD_DEVIATION":22.60716666747028,"ALL_AVG_TSQ":42.899,"TPR_STANDARD_ERROR":0.06864445642299069,"TSQ_SAMPLE_STANDARD_DEVIATION":14.256324897110533,"PSEUDO_RATE":1000,"TPR_SAMPLE_STANDARD_DEVIATION":2.7302895690779114,"NOT_AVG_TPR":7.73,"NOT_AVG_TQR":96.376,"TQR_STANDARD_ERROR":0.7106501954737345,"TSQ_STANDARD_ERROR":0.44529277797758937,"NOT_AVG_TSQ":42.383}]'
jsonTimeStr4 = '[{"TOTAL":1000,"ALL_AVG_TQR":91,"ALL_AVG_TPR":8.593,"TQR_SAMPLE_STANDARD_DEVIATION":14.280864941016336,"ALL_AVG_TSQ":42.001,"TPR_STANDARD_ERROR":0.04989880282555693,"TSQ_SAMPLE_STANDARD_DEVIATION":13.67382101584391,"PSEUDO_RATE":10,"TPR_SAMPLE_STANDARD_DEVIATION":2.077852296872153,"NOT_AVG_TPR":8.471,"NOT_AVG_TQR":90.815,"TQR_STANDARD_ERROR":0.45070010110825753,"TSQ_STANDARD_ERROR":0.43047140497232217,"NOT_AVG_TSQ":41.456},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":7.084,"TQR_SAMPLE_STANDARD_DEVIATION":18.080188586768717,"ALL_AVG_TSQ":43.426,"TPR_STANDARD_ERROR":0.04095597407732035,"TSQ_SAMPLE_STANDARD_DEVIATION":14.292732748003534,"PSEUDO_RATE":30,"TPR_SAMPLE_STANDARD_DEVIATION":1.6641435883478168,"NOT_AVG_TPR":6.982,"NOT_AVG_TQR":93.7,"TQR_STANDARD_ERROR":0.5666684939681328,"TSQ_STANDARD_ERROR":0.44383944359779937,"NOT_AVG_TSQ":42.931},{"TOTAL":1000,"ALL_AVG_TQR":92,"ALL_AVG_TPR":6.706,"TQR_SAMPLE_STANDARD_DEVIATION":16.16607377393144,"ALL_AVG_TSQ":41.92,"TPR_STANDARD_ERROR":0.04136985382257409,"TSQ_SAMPLE_STANDARD_DEVIATION":13.58523670389484,"PSEUDO_RATE":60,"TPR_SAMPLE_STANDARD_DEVIATION":1.6712601719216171,"NOT_AVG_TPR":6.603,"NOT_AVG_TQR":91.448,"TQR_STANDARD_ERROR":0.509689358151918,"TSQ_STANDARD_ERROR":0.42683742093450666,"NOT_AVG_TSQ":41.436},{"TOTAL":1000,"ALL_AVG_TQR":90,"ALL_AVG_TPR":6.442,"TQR_SAMPLE_STANDARD_DEVIATION":14.729368355247377,"ALL_AVG_TSQ":42.165,"TPR_STANDARD_ERROR":0.040283285484793326,"TSQ_SAMPLE_STANDARD_DEVIATION":13.912899852132172,"PSEUDO_RATE":90,"TPR_SAMPLE_STANDARD_DEVIATION":1.6123381870122273,"NOT_AVG_TPR":6.328,"NOT_AVG_TQR":89.906,"TQR_STANDARD_ERROR":0.46370154201165537,"TSQ_STANDARD_ERROR":0.4358434935039127,"NOT_AVG_TSQ":41.68},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":6.233,"TQR_SAMPLE_STANDARD_DEVIATION":21.019133188723504,"ALL_AVG_TSQ":42.199,"TPR_STANDARD_ERROR":0.04180561921406826,"TSQ_SAMPLE_STANDARD_DEVIATION":14.071756864761122,"PSEUDO_RATE":120,"TPR_SAMPLE_STANDARD_DEVIATION":1.6309550307597958,"NOT_AVG_TPR":6.102,"NOT_AVG_TQR":93.964,"TQR_STANDARD_ERROR":0.662040466565553,"TSQ_STANDARD_ERROR":0.4412531779166976,"NOT_AVG_TSQ":41.706},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":6.68,"TQR_SAMPLE_STANDARD_DEVIATION":20.18146839476337,"ALL_AVG_TSQ":42.839,"TPR_STANDARD_ERROR":0.03782062631893756,"TSQ_SAMPLE_STANDARD_DEVIATION":14.137243149789619,"PSEUDO_RATE":180,"TPR_SAMPLE_STANDARD_DEVIATION":1.5570894704192906,"NOT_AVG_TPR":6.544,"NOT_AVG_TQR":93.034,"TQR_STANDARD_ERROR":0.6359720461345615,"TSQ_STANDARD_ERROR":0.44374319546717805,"NOT_AVG_TSQ":42.338},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":6.507,"TQR_SAMPLE_STANDARD_DEVIATION":22.109886222235062,"ALL_AVG_TSQ":42.887,"TPR_STANDARD_ERROR":0.040536009609617826,"TSQ_SAMPLE_STANDARD_DEVIATION":14.392773572521621,"PSEUDO_RATE":240,"TPR_SAMPLE_STANDARD_DEVIATION":1.6619763939943308,"NOT_AVG_TPR":6.392,"NOT_AVG_TQR":93.303,"TQR_STANDARD_ERROR":0.6960507801612694,"TSQ_STANDARD_ERROR":0.4508762933485263,"NOT_AVG_TSQ":42.407},{"TOTAL":1000,"ALL_AVG_TQR":98,"ALL_AVG_TPR":6.035,"TQR_SAMPLE_STANDARD_DEVIATION":24.14801054821745,"ALL_AVG_TSQ":42.975,"TPR_STANDARD_ERROR":0.040175780672910506,"TSQ_SAMPLE_STANDARD_DEVIATION":14.392068653922367,"PSEUDO_RATE":300,"TPR_SAMPLE_STANDARD_DEVIATION":1.5678852560465972,"NOT_AVG_TPR":5.924,"NOT_AVG_TQR":97.731,"TQR_STANDARD_ERROR":0.7605908400898557,"TSQ_STANDARD_ERROR":0.4512973107318066,"NOT_AVG_TSQ":42.465},{"TOTAL":1000,"ALL_AVG_TQR":99,"ALL_AVG_TPR":6.442,"TQR_SAMPLE_STANDARD_DEVIATION":24.183243644730748,"ALL_AVG_TSQ":43.331,"TPR_STANDARD_ERROR":0.04107545096862602,"TSQ_SAMPLE_STANDARD_DEVIATION":14.441599144211056,"PSEUDO_RATE":720,"TPR_SAMPLE_STANDARD_DEVIATION":1.6644429602354034,"NOT_AVG_TPR":6.343,"NOT_AVG_TQR":98.365,"TQR_STANDARD_ERROR":0.7601937507739854,"TSQ_STANDARD_ERROR":0.4510797732077429,"NOT_AVG_TSQ":42.862},{"TOTAL":1000,"ALL_AVG_TQR":94,"ALL_AVG_TPR":6.075,"TQR_SAMPLE_STANDARD_DEVIATION":21.076585757708944,"ALL_AVG_TSQ":42.267,"TPR_STANDARD_ERROR":0.03939448117345244,"TSQ_SAMPLE_STANDARD_DEVIATION":14.48700736812002,"PSEUDO_RATE":1000,"TPR_SAMPLE_STANDARD_DEVIATION":1.5693645873954105,"NOT_AVG_TPR":5.958,"NOT_AVG_TQR":93.559,"TQR_STANDARD_ERROR":0.6645096154517948,"TSQ_STANDARD_ERROR":0.45517034387002836,"NOT_AVG_TSQ":41.775}]'
jsonValStr1 = '[{"TOTAL":1002,"VALIDITY2":100,"VALIDITY1":0,"VALIDITY0":0}]'
jsonValStr2 = '[{"TOTAL":1472,"VALIDITY2":68.5461956521739,"VALIDITY1":0,"VALIDITY0":31.453804347826086}]'
jsonValStr3 = '[{"TOTAL":1550,"PSEUDO_RATE":10,"VALIDITY2":64.77419354838709,"VALIDITY1":6.387096774193549,"VALIDITY0":28.838709677419356},{"TOTAL":1730,"PSEUDO_RATE":30,"VALIDITY2":58.554913294797686,"VALIDITY1":1.907514450867052,"VALIDITY0":39.53757225433526},{"TOTAL":1726,"PSEUDO_RATE":60,"VALIDITY2":58.28505214368482,"VALIDITY1":0.9269988412514484,"VALIDITY0":40.78794901506373},{"TOTAL":1625,"PSEUDO_RATE":90,"VALIDITY2":61.96923076923076,"VALIDITY1":0.6153846153846154,"VALIDITY0":37.41538461538462},{"TOTAL":1695,"PSEUDO_RATE":120,"VALIDITY2":59.469026548672566,"VALIDITY1":0.471976401179941,"VALIDITY0":40.0589970501475},{"TOTAL":1616,"PSEUDO_RATE":180,"VALIDITY2":62.190594059405946,"VALIDITY1":0.3094059405940594,"VALIDITY0":37.5},{"TOTAL":1628,"PSEUDO_RATE":240,"VALIDITY2":62.1007371007371,"VALIDITY1":0.2457002457002457,"VALIDITY0":37.65356265356266},{"TOTAL":1695,"PSEUDO_RATE":300,"VALIDITY2":59.29203539823009,"VALIDITY1":0.17699115044247787,"VALIDITY0":40.530973451327434},{"TOTAL":1522,"PSEUDO_RATE":720,"VALIDITY2":66.55716162943496,"VALIDITY1":0.0657030223390276,"VALIDITY0":33.37713534822602},{"TOTAL":1583,"PSEUDO_RATE":1000,"VALIDITY2":63.99241945672773,"VALIDITY1":0,"VALIDITY0":36.00758054327227}]'
jsonValStr4 = '[{"TOTAL":1735,"PSEUDO_RATE":10,"VALIDITY2":57.925072046109506,"VALIDITY1":5.648414985590778,"VALIDITY0":36.42651296829971},{"TOTAL":1652,"PSEUDO_RATE":30,"VALIDITY2":61.68280871670703,"VALIDITY1":2.0581113801452786,"VALIDITY0":36.2590799031477},{"TOTAL":1633,"PSEUDO_RATE":60,"VALIDITY2":61.66564605021433,"VALIDITY1":0.9797917942437232,"VALIDITY0":37.35456215554195},{"TOTAL":1603,"PSEUDO_RATE":90,"VALIDITY2":63.00686213349969,"VALIDITY1":0.6862133499688085,"VALIDITY0":36.3069245165315},{"TOTAL":1523,"PSEUDO_RATE":120,"VALIDITY2":66.25082074852266,"VALIDITY1":0.5252790544977018,"VALIDITY0":33.22390019697964},{"TOTAL":1696,"PSEUDO_RATE":180,"VALIDITY2":59.43396226415094,"VALIDITY1":0.3537735849056604,"VALIDITY0":40.2122641509434},{"TOTAL":1682,"PSEUDO_RATE":240,"VALIDITY2":60.04756242568371,"VALIDITY1":0.2972651605231867,"VALIDITY0":39.6551724137931},{"TOTAL":1524,"PSEUDO_RATE":300,"VALIDITY2":66.20734908136482,"VALIDITY1":0.19685039370078738,"VALIDITY0":33.59580052493438},{"TOTAL":1643,"PSEUDO_RATE":720,"VALIDITY2":61.655508216676814,"VALIDITY1":0.06086427267194157,"VALIDITY0":38.28362751065125},{"TOTAL":1588,"PSEUDO_RATE":1000,"VALIDITY2":63.413098236775824,"VALIDITY1":0,"VALIDITY0":36.58690176322418}]'

# parsed json test logs
jsonData1 = json.loads(jsonDataStr1)
jsonData2 = json.loads(jsonDataStr2)
jsonData3 = json.loads(jsonDataStr3)
jsonData4 = json.loads(jsonDataStr4)
jsonTime1 = json.loads(jsonTimeStr1)
jsonTime2 = json.loads(jsonTimeStr2)
jsonTime3 = json.loads(jsonTimeStr3)
jsonTime4 = json.loads(jsonTimeStr4)
jsonVal3 = json.loads(jsonValStr3)
jsonVal4 = json.loads(jsonValStr4)

# empty data 0 averages to be filled
test2Data0 = 0
test3Data0 = 0
test4Data0 = 0

# empty data 1 averages to be filled
test2Data1 = 0
test3Data1 = 0
test4Data1 = 0

# empty data 2 averages to be filled
test2Data2 = 0
test3Data2 = 0
test4Data2 = 0

# total time samples
totalSamples = jsonTime3[0]['TOTAL']

# empty pseudo rate lists to be filled
test1Rates = []
test2Rates = []
test3Rates = []
test4Rates = []

# empty TQR lists to be filled
test1TQRs = []
test1TQRstd = []
test2TQRs = []
test2TQRstd = []
test3TQRs = []
test3TQRstd = []
test4TQRs = []
test4TQRstd = []

# empty TSQ lists to be filled
test1TSQs = []
test1TSQstd = []
test2TSQs = []
test2TSQstd = []
test3TSQs = []
test3TSQstd = []
test4TSQs = []
test4TSQstd = []

# empty TPR lists to be filled
test1TPRs = []
test1TPRstd = []
test2TPRs = []
test2TPRstd = []
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

# append data rates  from log to lists

sum0 = 0
sum1 = 0
sum2 = 0
total0 = 0
total1 = 0
total2 = 0
for testRun in jsonData2:
    sum0 += testRun['DATA0']
    if testRun['DATA0'] != None:
        total0 = total0 + 1
    sum1 += testRun['DATA1']
    if testRun['DATA0'] != None:
        total1 = total1 + 1
    sum2 += testRun['DATA2']
    if testRun['DATA0'] != None:
        total2 = total2 + 1

if total0 != 0:
    test2Data0 = sum0 / total0

if total1 != 0:
    test2Data1 = sum1 / total1

if total1 != 0:
    test2Data2 = sum2 / total2


sum0 = 0
sum1 = 0
sum2 = 0
total0 = 0
total1 = 0
total2 = 0
for testRun in jsonData3:
    sum0 += testRun['DATA0']
    if testRun['DATA0'] != None:
        total0 = total0 + 1
    sum1 += testRun['DATA1']
    if testRun['DATA0'] != None:
        total1 = total1 + 1
    sum2 += testRun['DATA2']
    if testRun['DATA0'] != None:
        total2 = total2 + 1

if total0 != 0:
    test3Data0 = sum0 / total0

if total1 != 0:
    test3Data1 = sum1 / total1

if total1 != 0:
    test3Data2 = sum2 / total2


sum0 = 0
sum1 = 0
sum2 = 0
total0 = 0
total1 = 0
total2 = 0
for testRun in jsonData4:
    sum0 += testRun['DATA0']
    if testRun['DATA0'] != None:
        total0 = total0 + 1
    sum1 += testRun['DATA1']
    if testRun['DATA0'] != None:
        total1 = total1 + 1
    sum2 += testRun['DATA2']
    if testRun['DATA0'] != None:
        total2 = total2 + 1

if total0 != 0:
    test4Data0 = sum0 / total0

if total1 != 0:
    test4Data1 = sum1 / total1

if total1 != 0:
    test4Data2 = sum2 / total2


# append pseudo rates & avg times from log to lists
for testRun in jsonTime1:
    # test1Rates.append(testRun['PSEUDO_RATE'])
    test1TSQs.append(testRun['ALL_AVG_TSQ'])
    # test1TSQstd.append(testRun['TSQ_SAMPLE_STANDARD_DEVIATION'])
    test1TPRs.append(testRun['ALL_AVG_TPR'])
    # test1TPRstd.append(testRun['TPR_SAMPLE_STANDARD_DEVIATION'])
    test1TQRs.append(testRun['ALL_AVG_TQR'])
    # test1TQRstd.append(testRun['TQR_SAMPLE_STANDARD_DEVIATION'])

for testRun in jsonTime2:
    # test2Rates.append(testRun['PSEUDO_RATE'])
    test2TSQs.append(testRun['ALL_AVG_TSQ'])
    # test2TSQstd.append(testRun['TSQ_SAMPLE_STANDARD_DEVIATION'])
    test2TPRs.append(testRun['ALL_AVG_TPR'])
    # test2TPRstd.append(testRun['TPR_SAMPLE_STANDARD_DEVIATION'])
    test2TQRs.append(testRun['ALL_AVG_TQR'])
    # test2TQRstd.append(testRun['TQR_SAMPLE_STANDARD_DEVIATION'])

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

import math
import statistics as meaner
# the distribution of a sum of two normally distributed independent 
# variates X and Y with means and variances (μX,σ2X) and (μY,σ2Y), 
# respectively is another normal distribution

# get one time means instead of 10 because of pseudonym rates
test1MeanTSQ = meaner.mean(test1TSQs)
test1MeanTPR = meaner.mean(test1TPRs)
test1MeanTQR = meaner.mean(test1TQRs)

test2MeanTSQ = meaner.mean(test2TSQs)
test2MeanTPR = meaner.mean(test2TPRs)
test2MeanTQR = meaner.mean(test2TQRs)

test3MeanTSQ = meaner.mean(test3TSQs)
test3MeanTPR = meaner.mean(test3TPRs)
test3MeanTQR = meaner.mean(test3TQRs)

test4MeanTSQ = meaner.mean(test4TSQs)
test4MeanTPR = meaner.mean(test4TPRs)
test4MeanTQR = meaner.mean(test4TQRs)

# get one time stdevs instead of 10 because of pseudonym rates
def stdev_sum_vars(data):
    v = 0
    for i in range(0, len(data)):
        v += math.pow(data[i], 2)
    return math.sqrt(v)

test1stdevTSQ = stdev_sum_vars(test1TSQstd)
test1stdevTPR = stdev_sum_vars(test1TPRstd)
test1stdevTQR = stdev_sum_vars(test1TQRstd)
test2stdevTSQ = stdev_sum_vars(test2TSQstd)
test2stdevTPR = stdev_sum_vars(test2TPRstd)
test2stdevTQR = stdev_sum_vars(test2TQRstd)
test3stdevTSQ = stdev_sum_vars(test3TSQstd)
test3stdevTPR = stdev_sum_vars(test3TPRstd)
test3stdevTQR = stdev_sum_vars(test3TQRstd)
test4stdevTSQ = stdev_sum_vars(test4TSQstd)
test4stdevTPR = stdev_sum_vars(test4TPRstd)
test4stdevTQR = stdev_sum_vars(test4TQRstd)

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
    print("crit: "+str(critical)+"\nTval: "+str(abs(T)))
    if (abs(T) > critical):
        return False
    else:
        return True

# calculate confidence intervals for TQR chart
CI_TQR3 = []
CI_TQR4 = []
for i in range(0,len(test3TQRstd)):
    CI_TQR3.append(calculate_confidence_interval(totalSamples, test3TQRstd[i]))
    CI_TQR4.append(calculate_confidence_interval(totalSamples, test4TQRstd[i]))

# print means and their confidence intervals
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

# #test1 data plot
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.axis('equal')
data = ['Data 0', 'Data 1', 'Data 2']
data0 = 0
data1 = 0
data2 = 0
for testRun in jsonData1:
    data0 = testRun['DATA0']
    data1 = testRun['DATA1']
    data2 = testRun['DATA2']
test1Data = [data0, data1, data2]
# ax.pie(test1Data, labels = data,autopct='%1.2f%%')
# plt.show()

objects = ('Data 0', 'Data 1', 'Data 2')
y_pos = np.arange(len(objects))
test1Data = [data0, data1, data2]

plt.bar(y_pos, test1Data, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.yticks(percentTicks)
plt.ylabel('Percentage')
plt.title('Test 1 data type percentage')

plt.show()

# #test2 data plot
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.axis('equal')
data = ['Data 0', 'Data 1', 'Data 2']
test2Data = [test2Data0, test2Data1, test2Data2]
# ax.pie(test2Data, labels = data,autopct='%1.2f%%')
# plt.show()

objects = ('Data 0', 'Data 1', 'Data 2')
y_pos = np.arange(len(objects))

plt.bar(y_pos, test2Data, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.yticks(percentTicks)
plt.ylabel('Percentage')
plt.title('Test 2 data type percentage')


plt.show()

# #test3 data plot
objects = ('Data 0', 'Data 1', 'Data 2')
y_pos = np.arange(len(objects))

test3Data = [test3Data0, test3Data1, test3Data2]
plt.bar(y_pos, test3Data, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.yticks(percentTicks)
plt.ylabel('Percentage')
plt.title('Test 3 data type percentage')

plt.show()

# #test4 data plot
objects = ('Data 0', 'Data 1', 'Data 2')
y_pos = np.arange(len(objects))

test4Data = [test4Data0, test4Data1, test4Data2]
plt.bar(y_pos, test4Data, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.yticks(percentTicks)
plt.ylabel('Percentage')
plt.title('Test 4 data type percentage')

plt.show()

# test data summary plot
objects = ('Test 1', 'Test 2', 'Test 3', 'Test 4')
y_pos = np.arange(len(objects))

testSummaryData = [data0/(data0+data1+data2)*100, test2Data0/(test2Data0+test2Data1+test2Data2)*100, test3Data0/(test3Data0+test3Data1+test3Data2)*100, test4Data0/(test4Data0+test4Data1+test4Data2)*100]
plt.bar(y_pos, testSummaryData, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.yticks(percentTicks)
plt.ylabel('Percentage of data used was legit')
plt.title('Test data security success percentage')
plt.show()

# #test3 auth plot
df = pantelis.DataFrame({'Inner Auth Fail' : test3Val1, 'Outer Auth Fail' : test3Val0, 'Successful Auth' : test3Val2}, index=test3Rates)
ax = df.plot.bar(rot=0)
print(df)
plt.xticks(indpRates, test3Rates)
plt.yticks(percentTicks)
plt.xlabel('Pseudonym Change Rate')
plt.ylabel('% of total Authentication Attempts')
plt.title('Experiment 3 Authentication Scenario Ratios')
plt.grid(color='black', which='major', axis='y', linestyle='dotted')
plt.show()

#test3 time plot
timeData = []
for i in range(len(test3Rates)):
    timeData.append([test3TSQs[i], test3TPRs[i], test3TQRs[i]])

df = pantelis.DataFrame(timeData, columns = ['TSQ', 'TPR', 'TQR'])
df.plot.bar(stacked=True)
print(df)
plt.xticks(indpRates, test3Rates)
plt.xlabel('Pseudonym Change Rate')
plt.ylabel('Time in milliseconds')
plt.title('Experiment 3 Time Analysis')
plt.show()

# #test4 time plot
timeData = []
for i in range(len(test3Rates)):
    timeData.append([test4TSQs[i], test4TPRs[i], test4TQRs[i]])

df = pantelis.DataFrame(timeData, columns = ['TSQ', 'TPR', 'TQR'])
df.plot.bar(stacked=True)
print(df)
plt.xticks(indpRates, test3Rates)
plt.xlabel('Pseudonym Change Rate')
plt.ylabel('Time in milliseconds')
plt.title('Experiment 4 Time Analysis')
plt.show()

# #all test time plot
timeData = [[test1MeanTSQ, test1MeanTPR, test1MeanTQR], [test2MeanTSQ, test2MeanTPR, test2MeanTQR], [test3MeanTSQ, test3MeanTPR, test3MeanTQR], [test4MeanTSQ, test4MeanTPR, test4MeanTQR]]

df = pantelis.DataFrame(timeData, columns = ['TSQ', 'TPR', 'TQR'])
df.plot.bar(stacked=True)
print(df)

objects = ['Test 1', 'Test 2', 'Test 3', 'Test 4']
plt.xticks(y_pos, objects)
plt.xlabel('Pseudonym Change Rate')
plt.ylabel('Time in milliseconds')
plt.title('Mean time Analysis of the different experiments')

plt.show()