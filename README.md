# Convert-Image-Maps
Python scripts for converting instance maps/class tags to RGB semantic segmentation maps and vice-versa.

`rgb.py`: converts instance image maps to RGB segmentation maps. 

`inst.py`: converts RGB segmentation maps to instance image maps. 

'color' is a list of color labels for each class numerically arranged w.r.t each class number tag. Modify
	this in the scripts depending your requirements.
	
<td><img width="800px" src="demo/demo.png"></td>  
	
`video.py`: converts image frames to a video sequence at a specified fps rate.
	
<img src="demo/video.gif" width="800"/> 

## Install Requirements

Install python packages from requirements.txt
```
pip install -r requirements.txt
```
## Usage 
Instance maps to RGB maps
```
python rgb.py --path <datapath> --imagewidth <size> --imageheight <size> --savepath <datapath>

```
RGB Maps to Instance maps

```
python inst.py --path <datapath> --imagewidth <size> --imageheight <size> --savepath <datapath>

```
By default, the converted images are saved in './save/' folder and image size is 2048x1024. 

Disclaimer: You will not receive the same color masks if you try to convert back and forth. I think it's because the colors are not properly interpreted during this. Feel free to fix this and leave a PR.  

Image Frames to Video Sequence

```
python video.py --path <datapath> --fps <video fps>

```
