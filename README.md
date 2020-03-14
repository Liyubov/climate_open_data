# Climate open data
This is folder for downloaded open data for analysis and some tests for other open software for time-series analysis.
We use several sources for open data on temperature:
1. reanalysis data from GES DISC MERRA from https://disc.gsfc.nasa.gov/
2. observational data: folder for downloading http://data.ceda.ac.uk/badc/ukmo-hadobs/data/insitu/MOHC/HadOBS/HadUK-Grid/v1.0.0.0/60km/  and downloadable data link url = 'http://dap.ceda.ac.uk/thredds/fileServer/badc/ukmo-hadobs/data/insitu/MOHC/HadOBS/HadUK-Grid/v1.0.0.0/60km/tas/mon/v20181126/tas_hadukgrid_uk_60km_mon_188401-188412.nc' and https://services.ceda.ac.uk/cedasite/myceda/user/ 

# How to download the data 
You must be logged in to download data, e.g. for 2010 taxmax: http://dap.ceda.ac.uk/thredds/fileServer/badc/ukmo-hadobs/data/insitu/MOHC/HadOBS/HadUK-Grid/v1.0.0.0/60km/tas/mon/v20181126/tas_hadukgrid_uk_60km_mon_201001-201012.nc



Downloaded data can be found here 
https://drive.google.com/drive/folders/1hGHdgXF5CHkLagCw9YEj-7gCKDCQoFiY?usp=sharing

https://drive.google.com/open?id=11-7B9pBwiM-6E9aLwNMYm1prgyxO4N3h

Main variables are: 

    surface_air_temperature 

    surface_layer_height 

    surface_pressure 

    surface_specific_humidity 

    surface_wind_speed

# Licence 
Data are distributed under Open Government Licence: 
https://help.ceda.ac.uk/article/235-climate-data-in-ceda-archives

# Code for parcing data 

For parcing data one needs to install ´xarray´ python package.

Alternative way of parcing data on climate is to use command line via the command:
*ncdump -t tasmax_hadukgrid_uk_60km_mon_188601-188612.nc*


