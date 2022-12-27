from pickle import TRUE
import tkinter as tk
from urllib import response 
import requests 
from tkinter import font






#from tkinter import Menu 
HEIGHT = 600
WIDTH = 700

#def test_function(entry):
  #  print('Button Clicked!',entry)
root = tk.Tk()
#api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
#aa0f4cbe26535ec6917f1cf76bcd9aa3
def get_weather(city):
    weather_key = 'aa0f4cbe26535ec6917f1cf76bcd9aa3'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key,'q':city,'units':'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)
    

def format_response(weather):
    try:
        name = weather['name']
        description =weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name,description,temp)
    except:
        final_str = 'there was a promblem retrieving that information'

    return final_str



   

canvas = tk.Canvas(root, height=HEIGHT,width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='fcde946d572f8968cde14b688527021b.png')
background_label= tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)
#how to center it 
frame = tk.Frame(root, bg='black',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry = tk.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame, text = 'Get Weather',command=lambda: get_weather(entry.get()),bg='#BBB4B1')
button.place(relx=0.7,relheight=1,relwidth=0.3)

lower_frame = tk.Frame(root, bg='#BBB4B1',bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label = tk.Label(lower_frame,bg='#B5DCED',font=("Courier", 20))
label.place(relwidth=1,relheight=1)





#menubar= Menu(root)


root.mainloop()