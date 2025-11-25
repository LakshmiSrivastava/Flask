FROM python:3.8-slim-buster
# small OS

# set working directory to /app
WORKDIR /flask.loan_app
# this is the working directory inside the container

RUN python3 -m pip install --upgrade pip

COPY artefacts/requirement.txt requirement.txt


RUN pip3 install -r requirement.txt

COPY . .
# Copy everything from current directory to working directory in container

CMD ["python3", "-m","flask", "--app", "app.py","run", "--host=0.0.0.0"]
# host can be any IP address

# if bash file, i can use RUN chmod +x filename.sh
#PWD- Present working directory
#ADD . /app
# COPY . /app
# COPY is preferred over ADD   
  

#docker tag local-image:tagname new-repo:tagname
#docker push new-repo:tagname

#docker tag image_jan flask1:latest

#docker push lakshmisrivastava1234/flask1:latest