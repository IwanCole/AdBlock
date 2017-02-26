# AdBlock / Popup Blocker

Blocks domains by resolving a given URL to localhost. Made because certain streaming sites throw loads of Pop-Under ads when clicking any video controls. Normal Adlock doesn't seem to stop them sadly. Works for Windows and now Linux too(?).

Run in an Admin Command Prompt using, or use sudo on linux based systems:
```sh
python DNSBLocker.py X COMMAND ARGS
```
Where COMMAND = list | auto | add webaddress.com | remove webaddress.com

Also X is an unused argument that exists so that DNSBlocker.py can be run from batch scripts.
This is in case a batch script is set to accept multiple arguments.
You do not have to use X if you are running the python script directly.

The 'auto' command pulls a list of domains from my github, found at /blocklist.txt. When you run this command you are able to review the sites before they are blocked.

For example, to block google.com by running the script directly, use
```sh
python DNSBlocker.py add google.com
```
Or if you are running it from a batch script with args, you might setup the batch script as follows:
```sh
:: foo.bat
@echo off
if "%1" ==  "block" (
python DNSBlocker.py %*
)
```
Where you can then run as follows (admin/sudo), to maybe make running the python script easier
```sh
foo.bat block add google.com
foo.bat block remove google.com
```

This will block both 'google.com' and 'www.google.com'

Some example sites to block:
- terraclicks.com
- mediawhirl.net
- popmyads.com
- add-push.in
- adimo.in
- urfmobilya.net
- wrefsdf.com
- tororango.com
- onclkds.com
- britmethod.co
- addilite.com
- jolic2.com
- alibaba.com
- breitbart.com


Maybe backup your hosts file first, I don't wanna break it. Located in
```sh
C:\Windows\System32\drivers\etc\hosts
```
This project is licensed under the terms of the MIT license.
