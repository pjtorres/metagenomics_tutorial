# Pull base image
FROM ubuntu:14.04

MAINTAINER Pedro J. Torres

#-------- Installing wget to be able to download the fastp QC program -------------
RUN apt update && \
	apt-get install -y build-essential wget unzip  git awscli curl

#----- Installing diamond software: --------------
# 1. wget http://opengene.org/fastp/fastp the program
# 2. activate it
# 3. Move binary file into our /usr/bin. 

RUN wget http://opengene.org/fastp/fastp \
&& mv fastp /usr/bin

#----- Execute the DIAMOND binary ---------------
RUN chmod a+x /usr/bin/fastp
