# Use a base image that has the necessary build environment
FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

# Install build dependencies
RUN apt-get update && apt-get install -y \
    g++ \
    cmake \
    make \
    libssl-dev \
    git \
    libjsoncpp-dev \
    uuid-dev \
    zlib1g-dev

RUN git clone https://github.com/drogonframework/drogon.git \
    && cd drogon \
    && git submodule update --init \
    && mkdir build && cd build \
    && cmake .. \
    && make && make install

# Set the working directory in the container
WORKDIR /app

# Copy the application source code and configuration files into the container
COPY . /app

# Build your application
# Ensure the build directory exists, change to it, run cmake and make in a single RUN command
RUN mkdir -p build && cd build && cmake .. && make

# Expose the ports your application uses
EXPOSE 5555

# Command to run your application
CMD ["./build/shopping-backend"]