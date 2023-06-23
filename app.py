from flask import Flask
import os, requests, time

from datetime import datetime
import pytz

format = "%I:%M %p %B %d, %Y "


#print('Datetime:', dt_res)


def convert_datetime(timestamp):
    dt = datetime.fromtimestamp(time.time())
    now_manila = dt.astimezone(pytz.timezone("Asia/Manila"))
    return now_manila.strftime(format)

app = Flask(__name__)

url_dict = {
    'https://google.com':{
        'status':'',
        'created':'',
        'failed_dt':''
    },
    'http://gagukabatanga.com/':{
        'status':'',
        'created':'',
        'failed_dt':''
    }
}




@app.route('/check')
def check_url():
    return_content = "--------------------<br>"
    for url in url_dict:
        is_response = False
        if not url_dict[url]['status'] == 'failed':
            print(" Checking:",url)
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    is_response = True
                    #print(url,response.status_code)
                    return_content += 'URL: '+url+'<br>Status: Success.<br>--------------------<br>'
            except Exception as e:
                pass
            if not is_response:
                url_dict[url]['status'] = 'failed'
                url_dict[url]['failed_dt'] = convert_datetime(int(time.time()))
        if not is_response:
            return_content += 'URL: '+url+'<br>'
            return_content += 'Status: Failed.<br>'
            return_content += 'Created: '+url_dict[url]['created']+'<br>'
            return_content += 'Failed Time: '+str(url_dict[url]['failed_dt'])+'<br>'
            return_content += '--------------------<br>'

    return return_content



@app.route('/')
def hello_world():
    return 'Hello, world!'































#
