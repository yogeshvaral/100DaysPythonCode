import pandas

squirrels = pandas.read_csv("Squirrel_Count.csv")
# print(squirrels)
squirrels_with_colours = squirrels["Primary Fur Color"]
# print(squirrels_with_colours)
gray_squirrels = squirrels[squirrels["Primary Fur Color"] == "Gray"]["Primary Fur Color"]
print(gray_squirrels.count())
print(squirrels.head(2))
