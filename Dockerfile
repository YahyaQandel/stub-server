FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
WORKDIR /var/www/
ADD ./templates /var/www/templates
COPY ./main.py /var/www/main.py
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
CMD ["python3" , "main.py"]