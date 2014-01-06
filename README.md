This is a repo for stuff related to [Cryptography I](https://class.coursera.org/crypto-009/) on Coursera. No full solutions here; I will only post things that I feel don't violate the honor code (and in fact not even anything that I wouldn't freely post on the course forums)

### HexMessage

This is a class to make it easier to convert between strings and hex representation of strings and things that can be xor'ed together. Right now it assumes all strings are UTF-8 because this is a quick thing I banged out in a hurry, but I could be persuaded to fix it.

I wrote it for Python 3, and Unicode is one place where Python isn't backward-compatible *at all*. If you're using Python 2 you might find inspiration but you'd also have to almost rewrite the thing. If you do, please give me a pull request and I'll add it.

#### Usage

The constructor can take either of:

* A bare UTF-8 string. (`HexMessage("hello world")`)
* A hex-encoded `bytes` object (`HexMessage(b'6c73d5240a948c86981bc294814d')`)

The `^` operator is overloaded (and really, the point of all this). You can xor with any of:

* A UTF-8 string (`a ^ "sup bro"`)
* A hex-encoded `bytes` object (`a ^ b'7375702062726f'`)
* Another `HexMessage` object (`a ^ b`)

In each case it returns a new `HexMessage`.

`__str__` and `__repr__` are overloaded differently to make it easy to look at the hex representation or the string representation as needed (`a` in the REPL will show the hex, while `print(a)` will show the string)
