import hashlib
from typing import Final


secret_key : Final = "iwrupvqb"

i = 0
while True:
  result = hashlib.md5((secret_key + str(i)).encode()).hexdigest()
  if result.startswith("000000"):
    print(i)
    break
  i += 1