Cold Wallet Generator
=====================

Given one or more Bitcoin addresses with private keys, generates a TeX file suitable for printing and putting into cold storage.

Usage
=====

1. Get a file of Bitcoin addresses with private keys that you want to put into cold storage (i.e., offline, not on a computer). The addresses should be one per line, in Electrum format: `address:private_key`.
2. `cat my_keys.txt | gen_cold_wallet > my_keys.tex`
3. Run the TeX file through your favorite TeX processor and print the result.
4. Test the printed page with a QR-code scanner and make sure you can read the private keys.
5. Securely delete the input key file, the TeX file, and any intermediate files.
6. Put that piece of paper somewhere safe.
7. Use your addresses as you wish.

Notes
======

While developing this script, I used [keyfmt](https://github.com/bkkcoins/misc/blob/master/keyfmt/keyfmt) and piped its output straight to the wallet generator:

`$ { for i in {1..20} ; do hexdump -v -e '/1 "%02X"' -n 32 /dev/urandom | keyfmt "%a:%w" ; done } |
gen_cold_wallet > /tmp/keys.tex`

On Linux, you probably want to install texlive and then run `pdflatex --shell-escape keys.tex`. On Mac, install [MacTex](http://tug.org/mactex/). No idea what to do on Windows.

If you don't want to worry about files sticking around on Linux, avoid writing them in the first place with `mkdir /tmp/ramdisk; chmod 777 /tmp/ramdisk; sudo mount -t tmpfs -o size=256M tmpfs /tmp/ramdisk/` and then do your work in that directory. Then `umount /tmp/ramdisk/` when you're done.

FAQ
===

* **What's this about secure deletion?** On OSX, you want `srm file_I_never_want_to_see_again`. On Linux, it's `shred -u file_I_never_want_to_see_again`. I don't know how to do it on Windows.

* **This is just what I was looking for! I send you a tiny thank-you?** Sure! [1BUGzQ7CiHF2FUxHVH2LbUx1oNNN9VnuC1](https://blockchain.info/address/1BUGzQ7CiHF2FUxHVH2LbUx1oNNN9VnuC1)
