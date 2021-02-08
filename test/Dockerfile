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

CMD python3 /ModelofModels/data/datatool.py --cron
