import datetime
import speak
import webbrowser
import weather
import os





def Action(send) :   
  
    data_btn  = send.lower()

    if "what is your name" in   data_btn :
      speak.speak("my name is virtual Assistant")  
      return "my name is virtual Assistant"

    elif "hello" in data_btn  or "hye" in data_btn  or "hay" in data_btn: 
        speak.speak("Hey sir, How i can  help you !")  
        return "Hey sir, How i can  help you !" 

    elif "how are you" in  data_btn :
            speak.speak("I am doing great these days sir") 
            return "I am doing great these days sir"   

    elif "thanku" in data_btn or "thank" in data_btn:
           speak.speak("its my pleasure sir to stay with you")
           return "its my pleasure sir to stay with you"      

    elif "good morning" in data_btn:
           speak.speak("Good morning sir, i think you might need some help")
           return "Good morning sir, i think you might need some help"   

    elif "time now" in data_btn or "time" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.strftime("%I:%M %p"))
          speak.speak(Time)
          return str(Time) 
    
    elif "what is the date" in data_btn or "date" in data_btn:
        current_date = datetime.datetime.now()
        formatted_date = current_date.strftime("%a %d %b %Y")
        Date = "Today's date is " + formatted_date
        speak.speak(Date)
        return str(Date)
    
    elif 'open wikipedia' in data_btn or 'wikipedia' in data_btn:
        query = data_btn.replace('open wikipedia ', '').replace('wikipedia ', '').strip()
        url = f'https://www.wikipedia.org/wiki/{query}'
        webbrowser.get(using='firefox').open(url)      
        webbrowser.open(url)
        speak.speak(f"Searching for {query} on Wikipedia...")
        return "Wikipedia Open"

    elif "shutdown" in data_btn or "quit" in data_btn:
            speak.speak("ok sir")
            return "ok sir"  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.get(using='firefox').open("https://spotify.com/")   
        webbrowser.get().open("https://spotify.com/")        
        webbrowser.open("https://spotify.com/")   
        speak.speak("spotify.com is now ready for you, enjoy your music")                   
        return "spotify.com is now ready for you, enjoy your music"


    elif 'open google' in data_btn or 'google'  in data_btn:
      query = data_btn.replace('open google ', '').replace('google ', '').strip()
      url = f'https://www.google.com/search?q={query}'
      webbrowser.get(using='firefox').open(url)     
      webbrowser.open(url)
      speak.speak(f"Searching for {query} on Google...")
      return "Google Open"  
      
      
    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        query = data_btn.replace('youtube ', '').replace('open youtube ', '').strip()
        url = f'https://youtube.com//search?q={query}'
        webbrowser.get(using='firefox').open(url)       
        webbrowser.open(url)
        speak.speak(f"Searching for {query} on Youtube...")
        return "YouTube open"  

    elif 'location' in data_btn or "route" in data_btn:
        query = data_btn.replace('location ', '').replace('route ', '').strip()
        url = f'https://www.google.com/maps/search/{query}/'
        webbrowser.get(using='firefox').open(url)       
        webbrowser.open(url)
        speak.speak(f"Searching for {query} on Google Maps...")   
    
    elif 'weather' in data_btn :
       ans   = weather.Weather()
       speak.speak(ans) 
       return ans

    elif 'music from my laptop' in data_btn:
        url = 'C:\\Users\\Mangi\\Music\\Hot Mixes'
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("songs playing...")
        return "songs playing..." 

    else :
        speak.speak( "I am not able to understand!")
        return "I am not able to understand!"       

