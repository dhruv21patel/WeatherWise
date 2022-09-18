from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title('weather app')

labelroot = Label(root, text="Enter Country ")
labelroot.grid(row=0,column=0,padx=10,pady=20)
zip = Entry(root)
zip.grid(row=0,column=1)

#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=~zipCode~&distance=5&API_KEY=E694BE53-3459-485C-A2BE-AED619A69967

#image1 = ImageTk.PhotoImage(Image.open(r"C:\Users\dp992\Desktop\luffy\1014221.jpg").resize((root.winfo_screenwidth(), root.winfo_screenheight() )))
#lb = Label(image = image1)
#lb.pack()


def getinfo():
    print("in")
    apikey = "http://api.weatherapi.com/v1/current.json?key=95761b5a81174a6c83a123713221809&q=" + str(
        zip.get()) + "&aqi=no"
    apireq = requests.get(apikey)
    try:
        api = json.loads(apireq.content)
    except Exception as e:
        api = "Eroor"
    frame = LabelFrame(root,padx=20,pady=20)
    frame.grid(row=2,columnspan=2)
    mylable1 = Label(frame, text =str(api["location"]['name']), font=("Helvetica",20) )
    mylable2 = Label(frame, text =str(api["location"]['region']), font=("Helvetica",10))
    mylable3 = Label(frame, text =str(api["location"]['country']), font=("Helvetica",10))
    mylable1.grid(row=0, column=0, padx=2, pady=2,sticky="NW")
    mylable2.grid(row=1, column=0, padx=2, pady=2)
    mylable3.grid(row=1, column=1, padx=2, pady=2)


    frame1 = Frame(root,padx=2,pady=2,width=root.winfo_screenwidth())
    frame1.grid(row=3,column=0)
    mylable4 = Label(frame1, text = " C : " + str(api["current"]['temp_c']), fg ="red")
    mylable5 = Label(frame1, text = " F : " + str(api["current"]['temp_f']), fg ="Green")
    mylable6 = Label(frame1, text = " Condition : " + str(api["current"]['condition']['text']))
    mylable6.grid(row=0, column=0, padx=2, pady=2, sticky="NW")
    mylable4.grid(row=1, column=0, padx=2)
    mylable5.grid(row=2, column=0, padx=2)



    frame2 = Frame(root,padx=2,pady=2,width=root.winfo_screenwidth())
    frame2.grid(row=3,column=1, sticky="W")
    mylable7 = Label(frame2, text = " wind_mph : " + str(api["current"]['wind_mph']),font=("Helvetica",10))
    mylable8 = Label(frame2, text = " wind_kph : " + str(api["current"]['wind_kph']) ,font=("Helvetica",10))
    mylable9 = Label(frame2, text = " wind_degree : " + str(api["current"]['wind_degree']) ,font=("Helvetica",10))
    mylable7.grid(row=0, column=0, padx=2, pady=2, sticky="NW")
    mylable8.grid(row=1, column=0, padx=2, sticky="NW")
    mylable9.grid(row=2, column=0, padx=2, sticky="NW")


    frame3 = Frame(root,padx=2,pady=10,width=root.winfo_screenwidth())
    frame3.grid(row=4,column=0,columnspan=2)
    mylable10 = Label(frame3, text = " HUMIDITY : " + str(api["current"]['humidity']),font=("Helvetica",10))
    mylable11 = Label(frame3, text = " cloud : " + str(api["current"]['cloud']),font=("Helvetica",10))
    mylable12 = Label(frame3, text = " gust_mph : " + str(api["current"]['gust_mph']),font=("Helvetica",10))
    mylable13 = Label(frame3, text = " gust_Kph : " + str(api["current"]['gust_kph']),font=("Helvetica",10))
    mylable10.grid(row=0, column=0, padx=2, pady=2, sticky="NW")
    mylable11.grid(row=1, column=0, padx=2)
    mylable12.grid(row=2, column=0, padx=2)
    mylable13.grid(row=2, column=0, padx=2)

btn = Button(root,text="get info",command=getinfo)
btn.grid(row=1,columnspan=2,pady=20)
root.mainloop()