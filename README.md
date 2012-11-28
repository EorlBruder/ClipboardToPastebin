ClipoardtoPastebin
==================

A simple python  script to copy your current Clipboard to Pastebin, returning the link into the Clipboard.

Requires xsel to be installed. Therefore only works with OSes which use a xserver. 

BEFORE USING:

You need to register a Pastebin-Account and Paste the api_dev key to the part in the code. I have commented that part, it's at the end of the code. 
You also need a Pastebin User key, which can be generated here: http://pastebin.com/api/api_user_key.html
If you are a premium user, or want to keep your pastes for longer, change the 'paste_expiredate' in code and remove the call of the del method. 
