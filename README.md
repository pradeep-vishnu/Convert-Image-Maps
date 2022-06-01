# Convert-Image-Maps
For converting instance maps to RGB semantic segmentation maps or vice-versa.

inst_to_rgb.py : converts instance image maps to RGB segmentation maps. 'color' array in the script is a list of colour labels for each class 
                 arranged numerically w.r.t each class number tag. 

## Install Requirements

Install python packages from requirements.txt
```
pip install -r requirements.txt
```
## Usage 
```
python inst_to_rgb.py --path <datapath> --imagewidth <size> --imageheight <size> --savepath <datapath>

```
