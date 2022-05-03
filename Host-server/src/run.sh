docker run --rm -it --net host --runtime=nvidia --gpus all --privileged  --device /dev/video0 -v `pwd`:/src course:latest bash -c 'cd /src/work; python3 web_server/flask_prj/server.py'