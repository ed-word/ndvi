# NDVI Predictor
<p>
The normalized difference vegetation index (NDVI) is a simple graphical indicator that can be used 
to analyze remote sensing measurements, typically, but not necessarily, from a space platform, 
and assess whether the target being observed contains live green vegetation or not.
</p>

Datasets obtained from the following websites under ISRO were used for training the neural network: 
  - <a href="https://www.mosdac.gov.in/" target='_blank'>MOSDAC</a> (Meteorological & Oceanographic Satellite Data Archival Centre) and 
  - <a href="https://vedas.sac.gov.in/vedas/" target='_blank'>VEDAS</a> (Visualisation of Earth observation Data and Archival System)

Features extracted were:
  - Rainfall
  - Soil Moisture
  - Soil Temperature
  - Air Temperature
  
These features were used to predict the NDVI value of a piece of farmland in the approaching month based on the input latitude and longitude.  
