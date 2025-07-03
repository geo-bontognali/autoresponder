# Basic Autoresponder

## Requirements

Install mitmproxy

```
sudo pacman -S mitmproxy
```

Trust proxy certificate

```
sudo cp ~/.mitmproxy/mitmproxy-ca-cert.pem /etc/ca-certificates/trust-source/anchors/mitmproxy-ca-cert.pem
sudo trust extract-compat
```

## Usage

1. Edit rules.conf
2. Run the proxy

```
mitmdump -s autoresponder.py
chromium --proxy-server=http://localhost:8080
``` 

