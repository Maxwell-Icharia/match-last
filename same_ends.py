def match_ends(words):
  count = 0
  for x in words:
    if len(x) >= 2 and x[0] == x[-1]:
      count = count + 1
  return count