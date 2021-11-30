alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "j", "k", "m", "n", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def next_password(current_password: str) -> str:
  done = False
  offset = 1
  new_password = current_password
  while not done:
    replacement = alphabet[(alphabet.index(new_password[-offset]) + 1) % 23]
    new_password = new_password[:-offset] + replacement + new_password[ len(new_password) - offset + 1 :]
    if replacement == "a":
      offset += 1
    else:
      done = True

  return new_password


def valid_password(suggested_password: str) -> bool:

  rule1 = False
  for i in range(len(suggested_password)-2):
    i0 = alphabet.index(suggested_password[i])
    i1 = alphabet.index(suggested_password[i+1])
    if i0 + 1 == i1:
      i2 = alphabet.index(suggested_password[i+2])
      if i1 + 1 == i2:
        rule1 = True
        break
  if not rule1: return False


  rule2 = False
  pair1 = ""
  for i in range(len(suggested_password)-1):
    if suggested_password[i] == suggested_password[i+1]:
      if pair1 == "":
        pair1 = suggested_password[i]
      elif pair1 != suggested_password[i]:
        rule2 = True
        break

  return rule1 and rule2


input = next_password("cqjxxyzz")
while not valid_password(input):
  input = next_password(input)

print(input)  #cqkaabcc






