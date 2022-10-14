docker pull ubuntu:18.04
xhost +
docker run -ti --net=host -e DISPLAY=$DISPLAY --name=wobottask2 -v ${PWD}:/datadrive ubuntu:18.04