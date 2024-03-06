import xarray as xr
import os


## To download the original file, simply setup your netrc file with your earthdata login username and information
## and wget the following url https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/VNP14.002/VNP14.A2024057.0518.002.2024057132050/VNP14.A2024057.0518.002.2024057132050.nc
## wget https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/VNP14.002/VNP14.A2024057.0542.002.2024057132053/VNP14.A2024057.0542.002.2024057132053.nc
## wget https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/VNP14.002/VNP14.A2024057.0454.002.2024057132047/VNP14.A2024057.0454.002.2024057132047.nc

# iterate over all the files in our data directory.. if we have a lot of files, maybe we crawl the directory and run our processing on the results- more dynamic. 
filenames = ["VNP14.A2024057.0518.002.2024057132050.nc", "VNP14.A2024057.0542.002.2024057132053.nc", "VNP14.A2024057.0454.002.2024057132047.nc"]

for filename in filenames:
    ds = xr.open_dataset(f"data/{filename}")
    
    # Super complex processing...
    try:
        os.mkdir("outputs")
    except:
        pass
    
    with open(f'outputs/{filename}.txt', "w") as output_file:
        output_file.write(str(list(ds.keys())))

#that's it, we're done!
