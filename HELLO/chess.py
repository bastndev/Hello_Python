# white = " "
# black = "⬛"

def main():
  for box in range(8):
      line = ""
      for col in range(8):
          if(box + col) % 2 == 0:
              line += "  "
          else:
              line += "⬛"
      print(line)

if __name__ == "__main__":
  main()