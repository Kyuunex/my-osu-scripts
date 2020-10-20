# command line usage:

**pass in no arguments:** the script assume you called it from your songs folder and will treat every subfolder as a mapset, 
and convert the .osu files inside  

**pass in `MAPSET` as an argument:** the script assumes you called it from the mapset folder and 
will check for .osu files in it and convert them  

**pass in anything that ends with `.osu`:** the script assumes that is the specific .osu file you want to convert and 
will convert it  

**pass in anything else:** the script assumes that you are passing in a path to a specific mapset folder and 
will check for .osu files in it and convert them all

# note
converted mapsets have a version of 5, and all mapsets 5 or lower are not gonna be converted.  
so, it's not possible to run this twice and break an already converted set.  
you can run this on your whole songs folder after you add stuff time to time if you want basically  
all conversions overwrite the current .osu files  

## example use on windows:

you need python installed and in PATH  

open cmd, and type  
```
python C:/beatmapbackporter.py C:/osu/Songs/1224803 Rita - Destination/
```  
this assumes you put the script literally in `C:/`  
(make sure there are no spaces in path where you put the script itself 
if you are not running it from the folder it is in)  
this will convert and override all .osu files that are in that mapset folder
