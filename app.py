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
    'https://www009.vipanicdn.net/streamhls/0b594d900f47daabc194844092384914/ep.1.1677592419.m3u8':{
        'status':'',
        'created':'02:00 PM June 23',
        'failed_dt':''
    },
    'https://delivery238.akamai-video-content.com/hls2/01/02979/3pf7o29i349d_,l,n,h,.urlset/master.m3u8?t=Dzvl6MVOdqdspu4Mr4AF5tn7C3DHSm7JHxZnmGHY54g&s=1687500188&e=10800&f=14898541&srv=sto225':{
        'status':'',
        'created':'02:03 PM June 23',
        'failed_dt':''
    },
    'https://tc-1.moocdn.net/_v6/daa1b0f081a8d4fe589619f7ab99f1567b3c666c95e9ee62ecf34d7f48101aca4021f5676ce7795285562b26a48a457d5c979a536e6cee29307198926bc60673914a5be80f5c2907f5620c810f7abaa48d0378a8cb4f8f3e5879c74ff816cd30c882ec66b1e76130bc63aae2f9da50619d40863a3c0b3eaaa282b89600c29176/master.m3u8':{
        'status':'',
        'created':'02:13 PM June 23',
        'failed_dt':''
    },
    'https://tc-1.boocdn.net/_v6/daa1b0f081a8d4fe589619f7ab99f1567b3c666c95e9ee62ecf34d7f48101aca4021f5676ce7795285562b26a48a457d5c979a536e6cee29307198926bc60673914a5be80f5c2907f5620c810f7abaa48d0378a8cb4f8f3e5879c74ff816cd30c882ec66b1e76130bc63aae2f9da50619d40863a3c0b3eaaa282b89600c29176/master.m3u8':{
        'status':'',
        'created':'02:15 PM June 23',
        'failed_dt':''
    },
    'https://c-an-ca4.betterstream.cc:2223/hls-playback/daa1b0f081a8d4fe589619f7ab99f1567b3c666c95e9ee62ecf34d7f48101aca4021f5676ce7795285562b26a48a457d593fe3a0a91be642006fb1735b9c723a5c3cd0404cec66430d4ce4f8351a12fb7046652193d6d641833ccc005575934f125e038e20c54be236db37fdc6978a6e83a413812da32f0f943d2ca4569207f14055c10f3553ce4d145b03b1802b2213/master.m3u8':{
        'status':'',
        'created':'02:15 PM June 23',
        'failed_dt':''
    }
}




@app.route('/debug')
def debug_url():
    try:
        with open('samplefile', 'r')as file:
            return file.read()
    except Exception as e:
        return 'Error: '+str(e)


@app.route('/check')
def check_url():
    return_content = "--------------------<br>"
    for url in url_dict:
        is_response = False
        if not url_dict[url]['status'] == 'failed':
            print(" Checking:",url[0:50])
            try:
                start_ts = time.time()
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    is_response = True
                    #print(url,response.status_code)
                    return_content += 'URL: '+url+'<br>Status: Success.<br>'
                    return_content += 'Response Time: '+str(time.time()-start_ts)+'<br>'
                    return_content += '--------------------<br>'
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
