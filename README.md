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

```bash
git clone https://github.com/kirilla/python.git
cd ./python
python3 -m venv venv
source venv/bin/activate
```

## Develop

```bash
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Pandemonium. (Stay safe. Use vi.)

deactivate
```


## Install

```bash
pip install .

# When doing a pip install in a virtual python environment, the venv,
# executables will be installed in venv/bin.
# If not using a venv you can add --user to force pip to install to a user-location.
# (The default is a systemwide location, which could be a bad idea. It depends.)
```

## Usage

**ARP network scanner**
```bash
arp_network_scanner

# NOTE: Hardcoded IP and network interface. Rewrite to use.
```

**MD5 hash cracker**
```bash
md5_hash_cracker [-h] hash wordlist

positional arguments:
  hash        the md5 hash string
  wordlist    the wordlist file path
```
**pickle revshell maker**
```bash
$ pickle_revshell_maker
# prints a base64-encoded reverse shell in a pickle.

$ pickle_web_vuln
# web server listens on http://127.0.0.1:5000 

# Send the pickle to the webserver on /unpickle
$ curl -d "pickled=gASVbgAAAAAAAACMBX..." http://127.0.0.1:5000/unpickle

# Does it work? I don't think so. Someting about truncation.
```

**portscanner**
```bash
$ portscanner (no arguments)

# Harcoded IP 127.0.0.1 and port range 1 - 65535.
# Edit the script to your heart's content.
```

**portscanner and vulnerability reporting toolchain**
```bash
$ ./scan -p 1-10000 | ./probe | ./report -s "Automatic port scanning"
```

**SSH server based on paramiko**
```bash
$ ssh_server_paramiko <port> <username> <password>

# Work in progress. Untested.
```

**SSH login bruteforcer**
```bash
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
```bash
Baaaar
```

**Web directory enumerator**
```bash
$ todo (no arguments)

NOTE: Hardcoded filename "todolist.txt" in the current directory.
```

**Web file downloader**
```bash
$ web_downloader [-h] -o OUTPUT url

positional arguments:
  url                   the url of a file or resource

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        the name of the file you want to create
```

**web subdomain enumerator**
```bash
TODO
```

**Web login bruteforcer**
```bash
TODO
```

**Web login bruteforcer (wordpress)**
```bash
TODO
```

**Web login curl2python (script generator)**
```bash
TODO
```

**Webmin exploit (CVE-2012-2982)**
```bash
TODO
```

**Wordlist maker (password fuzzer)**
```bash
TODO
```

### Fineprint
Look. About the code. Half of the code isn't mine. I nabbed it. Copy-pasted. ChatGPT wrote it. Does it matter? Sure it does. But who cares. Do YOU have a lawyer? 🕵🏻‍♂ 🚬 Yeah, I didn't think so.

I feel kinda stupid. 😩 But hey. At least the license is from MIT. 😏

And if the code don't work don't come running to me, babe. I'm just here for the good looks. So anyway, patches welcome. Works on my computer. Shrug emoji.
