import pandas as pd

movies = pd.read_csv("netflix_titles.csv")
movies = movies.dropna(subset='cast')
costars = {}
for cast, title in movies[['cast', 'title']].itertuples(index=False):
    actors = cast.split(", ")
    for actor in actors:
        costars.setdefault(actor, [])
        for actor1 in actors:
            if not actor == actor1: costars[actor].append((actor1, title))

while True:
    actor = input("Choose an actor/actress: ")
    if actor not in costars.keys():
        print("Invalid name!")
    else:
        break

ans = []
queue = [[("Kevin Bacon", "")]]
for i in range(len(movies.index)):
    path = queue.pop(0)
    actor1 = path[-1][0]
    if actor1 == actor:
        ans = path
        break
    for adj in costars.get(actor1, []):
        queue.append(path + [adj])

if not ans:
    print("Actor/Actress not connected to Kevin Bacon\n\n")
else:
    ans = ans[::-1]
    print("\n\nSeparation Degree: " + str(len(ans)-1) + "\n\n")
    for actor1, title in ans:
        if actor1 == "Kevin Bacon":
            print(actor1.center(40))
        else:
            print(actor1.center(40) + "\n" + "was in".center(40) + "\n" + title.center(40) + "\n" + "with".center(40))