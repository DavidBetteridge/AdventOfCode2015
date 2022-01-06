def expand(input: str) -> str:
  current = input[0]
  count = 1
  i = 1
  result = ""
  while i < len(input):
    if input[i] == current:
      count += 1
    else:
      result += f"{count}{current}"
      count = 1
      current = input[i]
    i += 1

  result += f"{count}{current}"
  return result



input = "1321131112"
for _ in range(50):
  input = expand(input)
print(len(input))
