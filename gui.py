# GUI that queries the database created in my ebay_scraper project for the average sold price and the number of units sold by
# just inputing the product name inside of the GUI input box and clicking the button on the right 
from tkinter import *
import mysql.connector
from PIL import Image

# connects the python script to local mysql 8.0 database
mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'ebay_scraper'
    )
mycursor = mydb.cursor()

# application default window size
HEIGHT = 500
WIDTH = 600

def data_query():
    product_name = entry.get()
    # mysql queries to pull data from database, 'data' variable holds data
    avg_pull = "SELECT AVG(price_sold) FROM product_data WHERE product_id = (SELECT product_id FROM products WHERE product_name = "  + '"' + product_name + '"' +  ')' + ';' 
    mycursor.execute(avg_pull)
    data = '    Average Price Sold: ' + str(mycursor.fetchall()) + '\n'
    total_sold_pull = "SELECT count(price_sold) FROM product_data WHERE product_id = (SELECT product_id FROM products WHERE product_name = " + '"' + product_name + '"' + ')' + ';'
    mycursor.execute(total_sold_pull)
    data = '\n' + data + '\n    Amount Sold: ' + str(mycursor.fetchall()) + '\n'
    # takes the data variable and puts it inside of our output text box 
    label = Label(lower_frame)
    T = Text(lower_frame, height=40, width=60, font=15)
    T.pack()
    T.insert(END, data)

root = Tk()
# application title bar
root.title('SQL Database Query GUI --- By Austin Dobbins')

# applies the variables set at line 17 & 18 to tkinter window
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# creates the background color
background_label = Label(root, bg='#404040')
background_label.place(relwidth=1, relheight=1)

# creates an upper frame to place the input box and search button
frame = Frame(root, bg='#ff5d13', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# input box specs
entry = Entry(frame, font=15 )
entry.place(relwidth=0.65, relheight=1)

# search button specs
button = Button(frame, text="Pull Data", bg='#A0A0A0', fg='white', font=1000, command=entry.bind('<Return>', data_query) )
button.place(relx=0.7, relwidth=0.3, relheight=1)

# creates a second frame beneath first frame to house the data output statement
lower_frame = Frame(root, bg='#ff5d13', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(lower_frame)
label.place(relwidth=1, relheight=1)

# calls the tkinter window to open and continously run the script until window is exited
root.mainloop() 