
from bs4 import BeautifulSoup
import urllib.request
from time import sleep

print ('Xenomercys aka XxTrinityxXX Web Project')
print ('Version 1.0(Alpha Testing')
print ('Currently has a web scarper available')
# edited but not tested after this 


#end of edited text

print ('Type help for command listing:')
menudis = input('>>')
if (menudis =='help'):
    print('Xenoscarper - Allows usage of Scraper')
elif(menudis == 'xenoscraper'):
    print("Enter Target Url:")
    urlget = input('>>')
    #urlget = 'https://pythonprogramming.net/parsememcparseface/'
    sauce = urllib.request.urlopen(urlget).read()
    print("Acquiring target address......")
    #sleep(5)
    print("Copying Elements......")
    #sleep(5)
    print("Assessement Complete")
else:
    exit()
soup = BeautifulSoup(sauce,'lxml')
syscmd = input('>>')

if (syscmd == 'disp-title'):
    baseval = print(soup.title)
    quest = str(baseval)
    #for var in baseval: quest += str(var)
elif(syscmd == 'disp-page'):
    print(soup)

elif(syscmd == 'help'):
    print('disp-title  Gathers Title Tags')
    print('disp-page   Gathers All Tags')
    print('disp-para   Gathers Paragraph Tags')
    print('disp-para-all Gathers All Paragraph Tags')
    print('disp-all-hyper Gathers All Hyper Links')
    print('mod-spec-id   Modifies Specific id')
    print('grep-all      Gathers All text on Page')
    print('cp-file       Copies file to selected file')
    syscmd = input('>>')
    
elif(syscmd == 'disp-para'):
    print(soup.p)
    
elif(syscmd == 'disp-para-all'):
    print(soup.find_all('p'))
elif(syscmd == 'disp-all-hyper'):
    for url in soup.find_all('a'):

        print(url.get('href'))
elif(syscmd == 'grab-all'):
    #webcont =''
    print(soup.get_text())
    #for t in token: webcont += str(t)
    
elif(syscmd == 'mod-spec-id'):
    spec_id = input('>>')
    print('Locating id protocol....')
    sleep(3)
    print('Modifing id reference....')
    sleep(3)
    soup.find(id == spec_id)
    print('Modification Complete')
else:
    end()
 
syscmd = input('>>')
if (syscmd == 'cp-file'):
    #filec = input(">>")
    filesel= open("C:/Users/Enrique/Desktop/Py3Projects/Xeno-Web-Project-master/lok.txt","w")
    filesel.write(quest)
    print('Writing to file.....')
    print('Loading 50%')
    sleep(3)
    print('Loading 100%')
    sleep(2)
    filesel.close()
    print('File Saved')
# edited but not tested after this 


    
    



##for url in soup.find_all('a'):
##    print(url.get('href'))


