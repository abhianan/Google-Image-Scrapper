# Google-Image-Scrapper

    Note : This is a forked project
    The original package was developed by Anthony Casagrande and can be obtained from https://github.com/BirdAPI .
    I used his approach and developed a clean project which will help you in Scraping https://images.google.com/  
    and will give you better result . 
    
    #Development is still going on . Trying to make every image downloadable.


    One Basic Example I used 

    # -*- coding: utf-8 -*-
    """
    Created on Tue May 24 22:35:12 2016

    @author: ananab06
    """

    import os

    os.chdir("C:\Users\AnanAb06\Documents\Python Scripts")
    from Google-Image-Scrapper import google
    s=raw_input("Enter Your Query ")
    results = google.search_images(s)
    for i in results:
        p=str(i).split(',')
        f=p[len(p)-1][:-1][6:]
        print f
    
    
    
    There is one more approach for acheiving this but this will grab only small size pic.  Here is the code :

    from bs4 import BeautifulSoup
    import mechanize


    def imget(si):
         try:
            br=mechanize.Browser()
            br.set_handle_robots(False)
            br.addheaders=[('User-Agent','Mozilla')]
            img=br.open("https://www.google.com/search?site=&tbm=isch&source=hp&biw=1280&bih=899&q="+si+"&oq="+si)
            soup=BeautifulSoup(img)
            result=soup.findAll('img')
        
            for i in result:
                print i["src"]
        
        except:
            print "No result"
        
    p=raw_input("Enter the name of object \n")
    imget(p)
