# Warden
Named for the Wardenclyffe tower.

Install nginx, git and nikola.

Download https://github.com/stanhu/git-webhook-ninja

Copy then edit the nginx file, link the settings file in to gwn.

Run gwn


```
export WARDEN_CHECKOUT_DIR=/path/to/git/checkout/dir &&
export WARDEN_NIKOLA_CMD=/path/to/nikola/cmd &&
export WARDEN_SITE_DIR=/path/to/final/html/dir &&
export WARDEN_DOMAIN=.your_tld.com &&
./main.py
```


If NATed run this to tunnel out
`ssh user@ext.porthost.tld -R 0.0.0.0:8888:localhost:6666 -v`
