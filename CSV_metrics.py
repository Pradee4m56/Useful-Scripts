import csv


def writetestcsv():
    with open('test.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
    
def readtestcsv():
    with open('test.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
        for row in spamreader:
            #html_table(row)
            print(', '.join(row))
    x=0

def html_table(lol):
  print('lo is'  , lol)
  with open('build_mtr.html','a') as bmt :
      bmt.write( '<table>')
      bmt.write('  <tr><td>')
      bmt.write( '    </td><td>'+str(lol))
      bmt.write( '  </td></tr>')
      bmt.write( '</table>')



def main():
    writetestcsv()
    readtestcsv()
    

if __name__ == "__main__":
    main()
