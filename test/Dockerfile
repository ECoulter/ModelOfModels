# our base image
FROM  library/ubuntu:20.04

# install OS dependencies
RUN apt-get update && \
apt-get install -y python3-pip liblapack-dev libopenblas-dev libgdal-dev libproj-dev libproj15 libghc-zlib-dev libzmq3-dev libxml2-dev libxslt-dev libhdf5-dev libnetcdf-dev libjpeg-dev

# install python libraries
RUN python --version && \
which pip && \
pip install cython && \
pip install pyproj==2.6.1 && \
pip install numpy && \
pip install scipy && \
pip install pywget && \
pip install pyyaml 

RUN pip install sendgrid geopandas matplotlib rasterio

RUN pip install requests wget

RUN pip install osgeo

RUN pip install ipywidgets lxml descartes flask gis_output ipyleaflet netCDF4 hdf5

RUN git clone https://github.com/ECoulter/ModelOfModels

CMD python ./ModelofModels/data/datatool.py --cron
