import telium

DATA1="../test/test1.teliumProject"

fIn = open(DATA1, "r")

tp1 = telium.teliumProject.parse(fIn.read())


print tp1.render(encoding="UTF-8", pretty=True)

