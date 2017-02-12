# AdBlock / Popup Blocker

Blocks domains by resolving a given URL to localhost. Made because certain streaming sites throw loads of Pop-Under ads when clicking any video controls. Normal Adlock doesn't seem to stop them sadly. Works for Windows.

Run in an Admin Command Prompt using:
```sh
python DNSBLocker.py X COMMAND ARGS
```
Where COMMAND = list | add webaddress.com | remove webaddress.com
Also X is an unused argument that exists so that DNSBlocker.py can be run from batch scripts.

For example, to block google.com, use
```sh
python DNSBlocker.py X add google.com
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
- thevideo.me


Maybe backup your hosts file first, I don't wanna break it. Located in
```sh
C:\Windows\System32\drivers\etc\hosts
```
This project is licensed under the terms of the MIT license.
