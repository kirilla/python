# Python coursework 🤹🏻‍♂️

## What's in the box!?

- ARP network scanner
- MD5 hash cracker
- pickle revshell maker (+ vulnerable webserver)
- portscanner
- portscanner and vulnerability reporting toolchain
- SSH server based on paramiko (not working)
- SSH login bruteforcer
- Todo application
- Web directory enumerator
- Web file downloader
- web subdomain enumerator
- Web login bruteforcer
- Web login bruteforcer (wordpress)
- Web login curl2python (script generator)
- Webmin exploit (CVE-2012-2982)
- Wordlist maker (password fuzzer)

## Get started

```
git clone https://github.com/kirilla/python.git
cd ./python
python3 -m venv venv
source venv/bin/activate
```

## Develop

```
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Pandemonium. (Stay safe. Use vi.)

deactivate
```


## Install

```
$ pip install .

When doing a pip install in a virtual python environment, the venv,
executables will be installed in venv/bin.
If not using a venv you can add --user to force pip to install to a user-location.
(The default is a systemwide location, which could be a bad idea. It depends.)
```

## Usage

**ARP network scanner**
```
$ arp_network_scanner

NOTE: Hardcoded IP and network interface. Rewrite to use.
```

**MD5 hash cracker**
```
$ md5_hash_cracker [-h] hash wordlist

positional arguments:
  hash        the md5 hash string
  wordlist    the wordlist file path
```
**pickle revshell maker**
```
$ pickle_revshell_maker
prints a base64-encoded reverse shell in a pickle.

$ pickle_web_vuln
web server listens on http://127.0.0.1:5000 

Send the pickle to the webserver on /unpickle
$ curl -d "pickled=gASVbgAAAAAAAACMBX..." http://127.0.0.1:5000/unpickle

Does it work? I don't think so. Someting about truncation.
```

**portscanner**
```
$ portscanner (no arguments)

Harcoded IP 127.0.0.1 and port range 1 - 65535.
Edit the script to your heart's content.
```

**portscanner and vulnerability reporting toolchain**
```
$ ./scan -p 1-10000 | ./probe | ./report -s "Automatic port scanning"
```

**SSH server based on paramiko**
```
$ ssh_server_paramiko <port> <username> <password>

Work in progress. Untested.
```

**SSH login bruteforcer**
```
$ sshlogin [-h] [-t TARGET] [-p PORT] [-u USERNAME] [-w WORDLIST]

options:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        the host IP number
  -p PORT, --port PORT  the host portnumber
  -u USERNAME, --username USERNAME
                        the username
  -w WORDLIST, --wordlist WORDLIST
                        a password wordlist file
```

**Todo application**
```
$ todo (no arguments)

NOTE: Hardcoded filename "todolist.txt" in the current directory.
```

**Web directory enumerator**
```
$ web_directory_enumeration (no arguments)

Hardcoded arguments:
URL = "http://example.loc"
FILE = "wordlist.txt"

Edit before use.
```

**Web file downloader**
```
$ web_downloader [-h] -o OUTPUT url

positional arguments:
  url                   the url of a file or resource

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        the name of the file you want to create
```

**web subdomain enumerator**
```
$ web_subdomain_enumeration (no arguments)

Hardcoded arguments
DOMAIN = "example.loc"
FILE = "subdomains.txt"

Edit before use.
```

**Web login bruteforcer**
```
$ weblogin (no arguments)

Hardcoded values:
USERNAME, URL, PASSWORD_FILE_PATH, HEADERS, PARAMS

Edit before use.
```

**Web login bruteforcer (wordpress)**
```
$ weblogin_wordpress (no arguments)

Hardcoded values:
USERNAME, URL, PASSWORD_FILE_PATH, HEADERS, PARAMS

Edit before use.
```

**Web login curl2python (script generator)**
```
$ curl2python [-h] -X X [-H [HEADER ...]] --data-raw DATA_RAW url

positional arguments:
  url                   the url of the login form

options:
  -h, --help            show this help message and exit
  -X X                  the form method, get or post
  -H [HEADER ...], --header [HEADER ...]
                        an http header, in key:value format
  --data-raw DATA_RAW   the form data in raw form, urlencoded

EXAMPLE:
curl2python http://kirilla.com/login -X POST -H key:value--data-raw username=klaus&password=ichbinsanta

NOTE:
curl2python will take the same arguments as given to curl
to post to a login form on a webserver.

* Open a browser, e.g. Firefox, to a login page.
* Open the browser developer tools (F12)
* Switch to the network tab.
* Attempt a login
* Right-click the login page post-request, select "As Curl"
* Paste the command in a Terminal and replace "curl" with curl2python.
* Answer a few questions.

If all goes well, a script should be generated in the current directory. 
This script can be used for brute-force login attempts on the server.
```

**Webmin exploit (CVE-2012-2982)**
```
$ webmin_exploit (no arguments)

Hardcoded arguments:
REMOTE_HOST, REMOTE_PORT, USERNAME, PASSWORD, LOCAL_HOST, LOCAL_PORT

Edit before use.
```

**Wordlist maker (password fuzzer)**
```
$ wordlist_maker [-h] [-w WORDLISTS [WORDLISTS ...]] [-l LITERALS [LITERALS ...]] [-c CHARACTERS [CHARACTERS ...]] template

A template-based wordlist generator

positional arguments:
  template              a template for the generator

options:
  -h, --help            show this help message and exit
  -w WORDLISTS [WORDLISTS ...], --wordlists WORDLISTS [WORDLISTS ...]
                        the path to a wordlist
  -l LITERALS [LITERALS ...], --literals LITERALS [LITERALS ...]
                        a literal string
  -c CHARACTERS [CHARACTERS ...], --characters CHARACTERS [CHARACTERS ...]
                        a character set

The wordlist, literal and character set arguments should
be given in the order in which they are used in the template.
A colon is used to separate them.

w:w:w    wordlist 1, 2 and 3
w:c       wordlist 1, character set 1
l:w:c    literal string 1, wordlist 1, character set 1
```

### Fineprint
Look. About the code. Half of the code isn't mine. I nabbed it. Copy-pasted. ChatGPT wrote it. Does it matter? Sure it does. But who cares. Do YOU have a lawyer? 🕵🏻‍♂ 🚬 Yeah, I didn't think so.

I feel kinda stupid. 😩 But hey. At least the license is from MIT. 😏

And if the code don't work don't come running to me, babe. I'm just here for the good looks. So anyway, patches welcome. Works on my computer. Shrug emoji.
