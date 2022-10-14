docker pull ubuntu:18.04
xhost +
docker run -ti --net=host -e DISPLAY=$DISPLAY --name=wobottask2 -v ${PWD}:/datadrive ubuntu:18.04
cd datadrive
apt-get update
apt-get upgrade -y
apt-get install git -y
apt install software-properties-common -y
apt update
add-apt-repository ppa:deadsnakes/ppa
apt install python3.8 -y
python3.8 --version
apt-get install wget
wget --version
apt update
apt install python3-opencv -y
python3 -c "import cv2; print(cv2.__version__)"
apt update
apt install python3-pip -y
pip3 --version
pip3 install --upgrade pip
apt update apt install nano
pip3 install --upgrade opencv-python==4.2.0.34

