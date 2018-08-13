# Generates a basic bar graph

numItems = int(input("How many items? "))

bars = ""
for i in range(1, numItems + 1):
    # 1. Get input
    line = input("Enter quantity and item description separated by comma:")
    commaPos = line.find(',')
    qty = int(line[0:commaPos])
    descr = line[commaPos + 1:]

    bars += "<img src='green.png' height='50' width='" + str(qty*2) + "'> " + descr + "<br>\n";

# Assemble HTML page into one string

htmlPage = '''<html>
    <body>
    <h1>Bar Graph Example</h1>
    ''' + bars + '''
    </body>
    </html>'''

# Write HTML to file named output.html

outFile = open("output.html", "w")
outFile.write(htmlPage)
outFile.close()

print("Output saved to output.html")