def all_variants(text):
  length = len(text)
  for x in range(length):
    for y in range(x,length):
      yield text[x:y + 1]

# Здесь подпоследовательности переданной строки выводятся перебором каждого символа строки в сочетании
# с последующей частью строки

a = all_variants("abc")
for i in a:
  print(i)