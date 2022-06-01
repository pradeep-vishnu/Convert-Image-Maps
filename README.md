# Convert-Image-Maps
For converting instance maps/class tags to RGB semantic segmentation maps and vice-versa.

`inst_to_rgb.py`: converts instance image maps to RGB segmentation maps. 

'color' in the script is a list of color labels for each class numerically arranged w.r.t each class number tag. 

`rgb_to_inst.py`: converts RGB segmentation maps to instance image maps. 
               
<td><img width="800px" src="demo/demo.png"></td>


## Install Requirements

Install python packages from requirements.txt
```
pip install -r requirements.txt
```
## Usage 
Instance maps to RGB maps
```
python inst_to_rgb.py --path <datapath> --imagewidth <size> --imageheight <size> --savepath <datapath>

```
RGB Maps to Instance maps

```
python rgb_to_inst.py --path <datapath> --imagewidth <size> --imageheight <size> --savepath <datapath>

```


By default, the converted images are saved in './save/' folder and image size is 2048x1024. 

Disclaimer: You will not receive the same color masks if you try to convert back and forth. I think it's because the colors are not properly interpreted during this. Feel free to fix this and leave a PR.  
