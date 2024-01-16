from bs4 import BeautifulSoup
import requests
import openpyxl

excel= openpyxl.Workbook()
sheet = excel.active
sheet.title= 'BookList'
sheet.append(['Book Name', 'Author', 'Rating','Number of voter'])


url = "https://www.goodreads.com/list/show/1.Best_Books_Ever"
   

try:
    source = requests.get(url)
    source.raise_for_status()
    soup = BeautifulSoup(source.text, 'html.parser')

    booklist= soup.find_all('tr', itemtype ='http://schema.org/Book')[:300] #takes 300 booksname/detail 
    for book in booklist:
        print()
        #print(book)
        bname = book.span.text
        print(bname)

        aname = book.find('div',class_='authorName__container').span.text
        print(aname)

        #split when there arise avg and split into two list and takes first index value and which is required rating for us.
        rating = book.find('span', class_= 'minirating').text.split('avg')[0]
        print(rating)

        
        #as there are multiple spans and a so first it selects span which i want and a tag under that
        a_tags = book.select('span.smallText.uitext a')
        # print(a_tags)

        if len(a_tags)>=2:   #in our case we need second a tag so 
            votercount = a_tags[1].text.strip().split()[0]   #second a tag so [1]
            print(votercount)

        
        
        print()

        sheet.append([bname,aname,rating,votercount])

    

except Exception as e:
    print(e)

excel.save("ListofBook.xlsx")