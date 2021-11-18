from http import HTTPStatus
from flask import Flask,request, render_template
import json
from flask.wrappers import Response
import os

app=Flask(__name__)
host =  '0.0.0.0'
port = 9007
@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='GET':
        url = request.args.get('url')
        return render_template('index.html')  
    else:
        response_data = request.form.to_dict(flat=False)
        if 'jsresponse' not in response_data or not response_data['jsresponse'][0]:
          return Response(status=HTTPStatus.BAD_REQUEST,response={'no json provided'})

        with open('data.txt', 'w') as outfile:
          json.dump(response_data['jsresponse'], outfile)
        return Response(status=HTTPStatus.OK,response={'you can visit now <a href="/stub">url</a>'.format(host)})
        

@app.route("/stub",methods=['GET'])
def resp():
  if os.path.exists('./data.txt'):
    with open('data.txt') as json_file:
      data = json.load(json_file)
    return Response(status=HTTPStatus.OK,response=data)
  return 'no json provided'

if __name__ == '__main__':
    app.run(debug=True,host=host, port=port)