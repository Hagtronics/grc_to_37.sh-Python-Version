# A Pythonic Version of the GNU Radio Companion script grc_to_37.sh  
  
This is a pythonic version of the GNU Radio companion 3.6 to 3.7 (or 3.8, 3.9 and 3.10) updater script as described here,    
  
  https://wiki.gnuradio.org/index.php/Move_3-6_to_3-7#Restructure_of_GRC_Category_Names_to_Help_Transition   
    
This script above works, but is not Windows friendly.  
  
## Usage:  
  
Say you have an old GNU Radio companion flowgraph named: "my_radio.grc"  
  
Run the script as,  
  
`python.exe grc_to_37.py my_radio.grc`  
  
* A file named: "my_radio.grc" will be created, this is the converted file.  
  
* A file named: "my_radio.grc.bak" will be created, this is a copy of the original file.   
  
Note: This script will convert block names but don't expect the converted flowgraph to run without further rework. What you will get is blocks where you at least read the parameters, etc. which will help you in the conversion work.  
  
Also WX GUI controls no longer exist, so these will need to be converted to QT GUI controls.  

You can read more about the process at this blogpost,  
  
  https://gnuradio-cookbook.blogspot.com/2024/07/updating-old-gnuradio-companion.html

Enjoy :-)  
