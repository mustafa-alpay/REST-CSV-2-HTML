import sys

for arg in sys.argv:
    fileName = arg

import csv
with open( fileName, "rb") as f:
    reader = csv.reader(f)
    headers = reader.next()

#create XML file
with open( fileName + ".html", 'w+') as the_file:
    the_file.write( '<html>\n' )
    the_file.write('<body>\n')
    the_file.write('<table>\n')

with open(fileName) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        with open( fileName + ".html", 'a') as the_file:
            the_file.write('\t<tr>\n')
        i = 0
        while i < len(headers):
            #print(headers[i])
            with open( fileName + ".html", 'a') as the_file:
                the_file.write( '\t\t<td>' + row[headers[i]] + '</td>\n' )
            i += 1
        with open( fileName + ".html", 'a') as the_file:
            the_file.write('\t</tr>\n')

#close XML file
with open( fileName + ".html", 'a') as the_file:
    the_file.write('</table>\n')
    the_file.write('</body>\n')
    the_file.write( '</html>\n' )


