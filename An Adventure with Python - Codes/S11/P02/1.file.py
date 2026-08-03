with open("filename", "mode") as f:
    f.write("Hello")
    f.write("World")


with open("filename", "mode") as f:
    f.write("Hello\n")
    f.write("World")