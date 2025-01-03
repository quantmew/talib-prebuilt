#!/bin/bash

# TALIB_C_VER=0.6.2
# TALIB_PY_VER=0.5.2

# Download TA-Lib C Library
curl -L -o talib-c.zip https://github.com/TA-Lib/ta-lib/archive/refs/tags/v${TALIB_C_VER}.zip
if [ $? -ne 0 ]; then
    echo "Failed to download TA-Lib C library"
    exit 1
fi

# Download TA-Lib Python
curl -L -o talib-python.zip https://github.com/TA-Lib/ta-lib-python/archive/refs/tags/TA_Lib-${TALIB_PY_VER}.zip
if [ $? -ne 0 ]; then
    echo "Failed to download TA-Lib Python library"
    exit 1
fi

# Unzip TA-Lib C
unzip -q talib-c.zip
if [ $? -ne 0 ]; then
    echo "Failed to extract TA-Lib C library"
    exit 1
fi

# Unzip TA-Lib Python
unzip -q talib-python.zip -d ta-lib-python
if [ $? -ne 0 ]; then
    echo "Failed to extract TA-Lib Python library"
    exit 1
fi

# cd to TA-Lib C
cd ta-lib-${TALIB_C_VER}

# Configure TA-Lib
./configure --prefix=/usr

# Compile TA-Lib
make

if [ $? -ne 0 ]; then
    echo "Build failed"
    exit 1
fi

# Copy the lib
sudo make install

cp /usr/local/lib/ta-lib/libta_lib.a ./ta-lib.a

echo "TA-Lib build completed successfully!"
