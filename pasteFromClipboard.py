import os
import urllib.parse
import urllib.request

class PastebinAPI(object):
    _api_url = "http://pastebin.com/api/api_post.php"

    def _init_(self):
        pass

    def paste(self, api_dev_key, api_paste_code):
        #Assignment of the API dev key
        argv = {'api_dev_key': str(api_dev_key)}
        #Assignment of the Code to be submitted
        argv['api_paste_code'] = str(api_paste_code)
        #Setting the Api-Option to "paste"
        argv['api_option'] = str("paste")
        #Setting the Expire Time to 10 Minutes
        argv['paste_expire_date'] = "10M"
        #give the list we just created to the pastebin api
        request_string = urllib.request.urlopen(self._api_url,bytes(urllib.parse.urlencode(argv),"utf-8"))
        response = request_string.read()
        return response

p = PastebinAPI()
p._init_()
clipboard = os.popen('xsel -b').read()
url = p.paste("""KEY GOES HERE""",clipboard)
os.popen('echo ' + str(str(url)[2:-1]) + '| xsel -bi')
