import os
import sys
import urllib.parse
import urllib.request

class PastebinAPI(object):
    _api_url = "http://pastebin.com/api/api_post.php"

    def _init_(self):
        pass

    def paste(self, api_dev_key, api_user_key, api_paste_code):
        #Assignment of the API dev key
        argv = {'api_dev_key': str(api_dev_key)}
        #Assignment of the API user key
        argv['api_user_key'] = str(api_user_key)
        #Assignment of the Code to be submitted
        argv['api_paste_code'] = str(api_paste_code)
        #Setting the Api-Option to "paste"
        argv['api_option'] = str("paste")
        #Setting the Expire Time to 10 Minutes
        argv['paste_expire_date'] = "10M"
        #give the list we just created to the pastebin api
        request_string = urllib.request.urlopen(self._api_url,bytes(urllib.parse.urlencode(argv),"utf-8"))
        response = request_string.read()
        url = str(response)[2:-1]
        return url

    def list_by_user(self, api_dev_key, api_user_key):
        #Mostly the same as above with other options
        argv = {'api_dev_key': str(api_dev_key)}
        argv['api_user_key'] = str(api_user_key)
        argv['api_option'] = str("list")
        request_string = urllib.request.urlopen(self._api_url,bytes(urllib.parse.urlencode(argv),"utf-8"))
        response = request_string.read()
        a = str(response)[1:]
        out = []
        #cut the paste_keys out of the HUGE amount of text in response
        for i in range(len(a)):
            if a[i] == '>':
                if a[i-len('<paste_key>')+1:i+1] == '<paste_key>':
                    b = ""
                    j=i+1
                    while not a[j]=='<':
                        b=b+a[j]
                        j=j+1
                    out = out + [b]
        return out

    def del_all_pastes_by_user(self, api_dev_key, api_user_key):
        all = self.list_by_user(api_dev_key, api_user_key)
        responses = []
        for i in all:
            argv = {'api_dev_key': str(api_dev_key)}
            argv['api_user_key'] = str(api_user_key)
            argv['api_paste_key'] = str(i)
            argv['api_option'] = 'delete'
            request_string = urllib.request.urlopen(self._api_url,bytes(urllib.parse.urlencode(argv),"utf-8"))
            responses = responses + [str(request_string.read())[1:]]
        return responses

p = PastebinAPI()
p._init_()
#I call this to keep my pastebin tidy, you can also remove it 
p.del_all_pastes_by_user("""DEV_KEY_GOES_HERE""","""GENERATED USER KEY""")
#CODE FOR CLIPBOARD TO PASTEBIN
clipboard = os.popen('xsel -b').read()
url = p.paste("""DEV_KEY_GOES_HERE""","""GENERATED USER KEY""")
os.popen('echo ' + str(url) + '| xsel -bi')
