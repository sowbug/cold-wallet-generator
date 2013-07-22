Cold Wallet Generator
=====================

Given one or more Bitcoin addresses with private keys, generates a TeX or HTML file suitable for printing and putting into cold storage.

Requirements
============

Python and [jinja2](http://jinja.pocoo.org/docs/). For TeX: something that can render TeX files. For HTML: the Python libraries [PIL](http://www.pythonware.com/products/pil/) and [qrcode](https://github.com/lincolnloop/python-qrcode), as well as something that can render HTML (either your web browser or a direct-to-PDF tool like [wkhtmltopdf](https://code.google.com/p/wkhtmltopdf/)).

Usage
=====

1. Get a file of Bitcoin addresses with private keys that you want to put into cold storage (i.e., offline, not on a computer). The addresses should be one per line, in Electrum format: `address:private_key`.
2. `cat my_keys.txt | gen_cold_wallet > my_keys.tex`
3. Options include `--exclude-private-keys`, `--exclude-private-key-text`, and `--html`. Default is to print private keys, both as QR codes and as text, and to output as TeX.
4. Either run the TeX file through your favorite TeX processor and print the result, or print the HTML file.
5. Test the printed page with a QR-code scanner and make sure you can read the private keys. You might want to print another copy without the private keys so that you can easily send Bitcoin to the addresses later on.
6. Securely delete the input key file, the TeX/HTML file, and any intermediate files.
7. Put the printed paper somewhere safe.
8. Use your addresses as you wish.

Notes
======

While developing this script, I used [keyfmt](https://github.com/bkkcoins/misc/blob/master/keyfmt/keyfmt) and piped its output straight to the wallet generator:

`$ { for i in {1..20} ; do hexdump -v -e '/1 "%02X"' -n 32 /dev/urandom | keyfmt "%a:%w" ; done } |
gen_cold_wallet > /tmp/keys.tex`

(For real cold-storage addresses, if you're paranoid you'll use something other than /dev/urandom for your source of entropy.) On Linux, you probably want to install texlive and then run `pdflatex --shell-escape keys.tex`. On Mac, install [MacTex](http://tug.org/mactex/). No idea what to do on Windows.

If you don't want to worry about files sticking around on Linux, avoid writing them in the first place with `mkdir /tmp/ramdisk; chmod 777 /tmp/ramdisk; sudo mount -t tmpfs -o size=256M tmpfs /tmp/ramdisk/` and then do your work in that directory. Then `umount /tmp/ramdisk/` when you're done.

FAQ
===

* **What's this about secure deletion?** On OSX, you want `srm file_I_never_want_to_see_again`. On Linux, it's `shred -u file_I_never_want_to_see_again`. I don't know how to do it on Windows.

* **TeX? Seriously? If I wanted low tech I'd carve my addresses on rocks.** It's the best toolchain I could think of that gave good control over page layout but didn't involve a web browser (which you might not trust not to leave traces behind). There's probably a better command-line page-layout tool that will generate printable content, but I'm not familiar with it.

* **This is just what I was looking for! May I send you a tiny thank-you?** Sure! Here's my address: [1BUGzQ7CiHF2FUxHVH2LbUx1oNNN9VnuC1](https://blockchain.info/address/1BUGzQ7CiHF2FUxHVH2LbUx1oNNN9VnuC1)
