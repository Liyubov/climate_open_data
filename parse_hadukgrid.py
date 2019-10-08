import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# Start and end dates
start_date = '2001-01-01'
end_date = '2002-01-01'

# Configuration
variable_name = 'tas'
ds_name = 'hadukgrid'
area = 'uk'
horizontal_resolution = '60km'
frequency = 'mon'
file_fmt = 'nc'
date_fmt = '%Y%m'
proj_name = 'transverse_mercator'

# Define dates
start = pd.Timestamp(start_date)
end = pd.Timestamp(end_date)
dates = pd.date_range(start=start, end=end, freq='AS')

# Loop over years
ds = xr.Dataset()
for k, date in enumerate(dates[:-1]):
    # Define path to year of data
    date0_str = date.strftime(date_fmt)
    datef_str = (dates[k + 1] - pd.Timedelta('2 days')).strftime(date_fmt)
    filepath = '{}_{}_{}_{}_{}_{}-{}.{}'.format(
        variable_name, ds_name, area, horizontal_resolution, frequency,
        date0_str, datef_str, file_fmt)

    # Read data array
    ds_date = xr.open_dataset(filepath)

    # Add year to dataset
    ds = ds.merge(ds_date)

# Get data array
da = ds[variable_name]

# Get time mean
da_time_mean = da.mean('time')

# Get dataset projection
proj = ds[proj_name]
proj_params = dict(
    central_longitude=proj.attrs['longitude_of_central_meridian'],
    central_latitude=proj.attrs['latitude_of_projection_origin'],
    false_easting=proj.attrs['false_easting'],
    false_northing=proj.attrs['false_northing'],
    scale_factor=proj.attrs['scale_factor_at_central_meridian'])
crs = ccrs.TransverseMercator(**proj_params)

# Create axes for projection
fig = plt.figure()
ax = plt.axes(projection=crs)

# Plot mean
da_time_mean.plot(transform=crs)

# Draw coastlines
ax.coastlines()

# Show plots
plt.show(block=False)
