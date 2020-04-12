def estimator(data):
  output = {'data':data, 
            'impact': {}, 
            'severeImpact': {}
            }

  #CHALLENGE 1
  output['impact']['currentlyInfected'] = data['reportedCases'] * 10
  output['severeImpact']['currentlyInfected'] = data['reportedCases'] * 50

  #currentlyInfected = reportedCases * 10
  #impact = currentlyInfected
  #severeImpact = currentlyInfected * 5

  if data ['periodType'] == 'weeks':
        data['timeToElapse'] = data['timeToElapse'] * 7
  elif data ['periodType'] == 'months':
        data ['timeToElapse'] = data['timeToElapse'] * 30
  else:
    data ['timeToElapse'] = data['timeToElapse']
 
  #Given a certain number of days
  #factor = days//3

  #infectionsByRequestedTime = currentlyInfected * (2**factor)
  #impact = infectionsByRequestedTime
  #severeImpact = infectionsByRequestedTime * 5?

  output['impact']['infectionsByRequestedTime'] = output['impact']['currentlyInfected'] * (2 ** (data['timeToElapse']//3))
  output['severeImpact']['infectionsByRequestedTime'] = output['severeImpact']['currentlyInfected'] * (2 ** (data['timeToElapse']//3))

  #CHALLENGE 2
  #severeCasesByRequestedTime = 0.15*infectionsByRequestedTime
  #impact = severeCasesByRequestedTime
  #severeImpact = severeCasesByRequestedTime * 5

  output['impact']['severeCasesByRequestedTime'] = int(15/100 * (output['impact']['infectionsByRequestedTime']))
  output['severeImpact']['severeCasesByRequestedTime'] = int(15/100 * (output['severeImpact']['infectionsByRequestedTime']))
  
  #totalHospitalBeds = (severeCasesByRequestedTime/0.65)?
  #hospitalBedsByRequestedTime = totalHospitalBeds - severeCasesByRequestedTime
  #impact = hospitalBedsByRequestedTime
  #severeImpact = hospitalBedsByRequestedTime * 5

  output['impact']['hospitalBedsByRequestedTime'] = int((35/100 * (data['totalHospitalBeds'])) - output['impact']['severeCasesByRequestedTime'])
  output['severeImpact']['hospitalBedsByRequestedTime'] = int((35/100 * (data['totalHospitalBeds'])) - output['severeImpact']['severeCasesByRequestedTime'])

  #CHALLENGE 3
  #casesForICUByRequestedTime = 0.05 * infectionsByRequestedTime
  #impact = casesForICUByRequestedTime
  #severeImpact = casesForICUByRequestedTime * 5

  output['impact']['casesForICUByRequestedTime'] = int(5/100 * output['impact']['infectionsByRequestedTime'])
  output['severeImpact']['casesForICUByRequestedTime'] = int(5/100 * output['severeImpact']['infectionsByRequestedTime'])

  #casesForVentilatorsByRequestedTime = 0.02 * infectionsByRequestedTime
  #impact = casesForICUByRequestedTime
  #severeImpact = casesForVentilatorsByRequestedTime * 5

  output['impact']['casesForVentilatorsByRequestedTime'] = int(2/100 * output['impact']['infectionsByRequestedTime'])
  output['severeImpact']['casesForVentilatorsByRequestedTime'] = int(2/100 * output['severeImpact']['infectionsByRequestedTime'])
  
  #dollarsInFlight = (infectionsByRequestedTime * avgDailyIncomePopulation * avgDailyIncomeInUSD)/days

  output['impact']['dollarsInFlight'] = int((output['impact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomeInUSD'] * data['region']['avgDailyIncomePopulation']) /data['timeToElapse'])
  output['severeImpact']['dollarsInFlight'] = int((output['severeImpact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomeInUSD'] * data['region']['avgDailyIncomePopulation'])/data['timeToElapse'])

  return output


