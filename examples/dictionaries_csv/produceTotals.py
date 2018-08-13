

produceFile = open("produceSales.csv")

produceFile.readline()  # discard first line
lines = produceFile.readlines() # read rest of lines

produceTotals = {}
for line in lines:
  [produceType, costPerPound, poundsSold, total] = line.split(',')
  if produceType in produceTotals:
    produceTotals[produceType] = produceTotals[produceType] + float(total)
  else:
    produceTotals[produceType] = float(total)

for produceType in sorted(produceTotals):
  print('{0} - ${1:.2f}'.format(produceType, produceTotals[produceType]))

  
