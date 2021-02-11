# our base image
FROM  library/ubuntu:20.04

# install OS dependencies
RUN apt-get update && \
ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime && \
apt-get install -y python3-pip liblapack-dev libopenblas-dev libgdal26 libgdal-dev libproj-dev libproj15 libghc-zlib-dev libzmq3-dev libxml2-dev libxslt-dev libhdf5-dev libnetcdf-dev libjpeg-dev tzdata git vim

# install python libraries
RUN python3 --version && \
which pip3 && \
pip3 install cython && \
pip3 install pyproj==2.6.1 && \
pip3 install numpy && \
pip3 install scipy && \
pip3 install requests && \
pip3 install pywget && \
pip3 install wget && \
pip3 install pyyaml && \
pip3 install sendgrid && \
pip3 install geopandas && \
pip3 install matplotlib && \
pip3 install rasterio && \
pip3 install osgeo && \
pip3 install ipywidgets && \
pip3 install lxml && \
pip3 install descartes && \
pip3 install flask && \
pip3 install ipyleaflet && \
pip3 install gdal==3.0.4 && \
pip3 install netCDF4
#pip3 install hdf5

RUN git clone https://github.com/ECoulter/ModelOfModels

#Have to create an empty config file, to write over with a volume mount during 
# the actual run. Under k8s, this can be done via a ConfigMap.
# For now, just running under cron w/ docker
# datatool looks in pwd for the config.yml...
COPY watersheds.tar.gz /watersheds.tar.gz
RUN touch /config.yml &&\
tar xfz /watersheds.tar.gz 

RUN mv /Watersheds_032020/ ModelOfModels/data/ &&\
rm /watersheds.tar.gz
# This all needs to happen on the data dir because datatool doesn't handle missing dirs
#&&\
#mkdir -p /mom-data/rawdata/download &&\
#mkdir -p /mom-data/rawdata/gfms &&\
#mkdir -p /mom-data/cron_data/gfms &&\
#mkdir -p /mom-data/cron_data/glofas &&\
#mkdir -p /mom-data/cron_data/flood_severity &&\
#mkdir -p /mom-data/cron_data/gis_output
#

CMD python3 /ModelOfModels/data/datatool.py --cron
