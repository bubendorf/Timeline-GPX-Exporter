# Timeline-GPX-Exporter
Convert Google timeline new JSON format to daily GPX files

I created this because I needed an easy way to find time stamps from the last year of my raw timeline data, a function that irritatingly no longer exists since timeline went device only with the now very limited Android Maps Timeline interface.

Export timeline data from your Android device. 

To do this, on your Android device go to **settings > Location > Timeline > Export Timeline data**.  

Place the exported Timeline.json file into the same folder as Timeline-GPX-Exporter.py

Run Timeline-GPX-Exporter.py script. Daily GPX logs with be generated in ./GPX_Output with the format YYYY-MM-DD.gpx. 

Open the GPX logs in your veiewer of choice. 
GPXsee is a gppd option, however you may need to disable Elimiate GPS outliers from settings > Data > Filtering 
and disable pause dectection from settings > Data > Pause Detection.

Example: Place both Timeline-GPX-Exporter.py and Timeline.json in C:/Timeline

         Open command prompt
         >cd C:\Timeline
         >python Timeline-GPX-Exporter.py

The GPX log files produced are not perfect, some less forgiving viewers might regect them. However it does what I needed it to do perfectly, so as far as I'm concerned it's certified good enough. If this is good enough you then great, you're welcome, if it's not, well too bad, I have what I need from it and you're more than welcome to take it and adapt it to suit your needs.
