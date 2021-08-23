import os, sys

if sys.version[0:3] != "3.9":
  sys.exit("[+] kamu harus menggunakan versi python 3.9, versi python kamu sekarang : "+sys.version[0:3])

if __name__ == "__main__":
  try:
    __import__("delta17")
  except Exception as e:
    exit(str(e))
