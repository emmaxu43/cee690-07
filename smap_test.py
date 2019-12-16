import netCDF4 as nc
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import glob

strs= glob.glob("/stor/tyche/hydro/private/cx43/CEE675_2019Fall/project2/smap/data/*.h5")
files= sorted(strs)

var= 'sm_surface'
for file in files:
   fp_in = xr.open_dataset(file,group='Geophysical_Data' )
   data= fp_in[var][:] 
   new_data= np.array(data)  #(1624, 3856) -> y,x
   tmp= np.argwhere(new_data[~np.isnan(new_data)])
   tmp1= np.argwhere(~np.isnan(new_data))
   #print(tmp,tmp1) # [[   2 1111],[   2 1112],...,[1513 1635],[1513 1636]] -> y,x
   #plt.imshow(new_data)
   print(new_data[335,656])
   #plt.colorbar()
   #plt.show()
   fp_in.close()

""" total 1713 files: starting from  05/31
# 0-3, 3-6, 6-9,9-12, 12-15,15-18,18-21,21-0, total 8 files per day
minlon= -125.9100000
maxlon= -113.7060000
minlat= 32.1570000
maxlat= 43.2000000
xres =  0.0174532925199433
yres = 0.0174532925199433

#os.system('gdalwarp -r average -overwrite -t_srs EPSG:4326 -tr %f %f -te %f %f %f %f %s %s' % (xres,yres,minlon,minlat,maxlon,maxlat,file_in,file_out))

subprocess.call('gdalinfo file_in')
#os.system('gdal_translate -of NetCDF file_in file_out')"""
   

"""
print(fp[var])
Dimensions without coordinates: y, x
Attributes:
    long_name:         Top layer soil moisture (0-5 cm)
    valid_max:         0.9
    fmissing_value:    -9999.0
    DIMENSION_LABELS:  ['y', 'x']
    units:             m3 m-3
    grid_mapping:      EASE2_global_projection
    coordinates:       /cell_lat /cell_lon
    valid_min:         0.0
"""


"""
dimensions(sizes): x(3856), y(1624), phony_dim_2(1)
    variables(dimensions): |S1 EASE2_global_projection(phony_dim_2), uint32 cell_column(y,x), float32 cell_la       t(y,x), float32 cell_lon(y,x), uint32 cell_row(y,x), float64 time(phony_dim_2), float64 x(x), float64 y(y)
    groups: Geophysical_Data, Metadata
"""


"""
group: Geophysical_Data {
  variables:

float sm_surface(y, x) ;
                sm_surface:long_name = "Top layer soil moisture (0-5 cm)" ;
                sm_surface:valid_max = 0.9f ;
                sm_surface:_FillValue = -9999.f ;
                sm_surface:fmissing_value = -9999.f ;
                sm_surface:missing_value = -9999.f ;
                string sm_surface:DIMENSION_LABELS = "y", "x" ;
                sm_surface:units = "m3 m-3" ;
                sm_surface:grid_mapping = "EASE2_global_projection" ;
                sm_surface:coordinates = "/cell_lat /cell_lon" ;
                sm_surface:valid_min = 0.f ;

 float surface_temp(y, x) ;
                surface_temp:long_name = "Mean land surface temperature (incl. snow-covered land area). Excluding areas of                                     open water and permanent ice." ;
                surface_temp:valid_max = 350.f ;
                surface_temp:_FillValue = -9999.f ;
                surface_temp:fmissing_value = -9999.f ;
                surface_temp:missing_value = -9999.f ;
                string surface_temp:DIMENSION_LABELS = "y", "x" ;
                surface_temp:units = "K" ;
                surface_temp:grid_mapping = "EASE2_global_projection" ;
                surface_temp:coordinates = "/cell_lat /cell_lon" ;
                surface_temp:valid_min = 180.f ;

float windspeed_lowatmmodlay(y, x) ;
                windspeed_lowatmmodlay:long_name = "Surface wind speed at center height of lowest atmospheric model layer"                                     ;
                windspeed_lowatmmodlay:valid_max = 60.f ;
                windspeed_lowatmmodlay:_FillValue = -9999.f ;
                windspeed_lowatmmodlay:fmissing_value = -9999.f ;
                windspeed_lowatmmodlay:missing_value = -9999.f ;
                string windspeed_lowatmmodlay:DIMENSION_LABELS = "y", "x" ;
                windspeed_lowatmmodlay:units = "m s-1" ;
                windspeed_lowatmmodlay:grid_mapping = "EASE2_global_projection" ;
                windspeed_lowatmmodlay:coordinates = "/cell_lat /cell_lon" ;
                windspeed_lowatmmodlay:valid_min = -60.f ;
"""