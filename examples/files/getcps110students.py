f = open('C:\\Users\\sschaub\\Documents\\teaching\\tools\\cpsenroll.txt','r')

#data = f.read()
#lines = data.split('\n')

lines = f.readlines()
for line in lines:
  fields = line.split(',')
  if fields[0] == '110' and fields[1] == '01':
    print(fields)
  [courseNum, sectNum, firstName, lastName, username] = line.split(',')
  if courseNum == '110' and sectNum == '01':
    print(firstName, lastName)
f.close()
