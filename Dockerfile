FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# install system dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common \
    build-essential \
    cmake \
    python3.1- \
    python3.10-dev \
    python3.10-distutils \
    wget curl git \
    libgtest-dev \
    python3-pip \
&& apt-get clean

# Optional: Set Python 3.10 as default
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1

#install python dependencies

RUN python -m pip install --upgrade pip
RUN pip install pybind11 numpy matplotlib scipy pytest argparse

# Copy source to the container

WORKDIR /app
COPY . .

# Build

RUN cmake -B build -S.
RUN cmake --build build

CMD ["pytest", "Python/test.py"]
