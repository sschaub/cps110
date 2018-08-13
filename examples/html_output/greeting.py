#
# greeting.py
# 
# This example demonstrates how to create a web page using Python
#

name = input('What is your name? ')

# Create web page in a file named output.html

outfile = open('output.html', 'w')
outfile.write("""
   <html>
   <body>
     <h1>Greetings</h1>
     <p>Hello, """ + name + """!</p>
   </body>
   </html>
   """)
outfile.close()
