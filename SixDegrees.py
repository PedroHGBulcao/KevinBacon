import pandas as pd

movies = pd.read_csv("netflix_titles.csv")
movies = movies.dropna(subset='cast')
costars = {}
titles = {}
vis = {}
for cast, title in movies[['cast', 'title']].itertuples(index=False):
    actors = cast.split(", ")
    for actor in actors:
        costars.setdefault(actor, set())
        for actor1 in actors:
            if not actor == actor1:
                costars[actor].add(actor1)
                titles[(actor, actor1)] = title

while True:
    actor = input("Choose an actor/actress: ")
    if actor not in costars.keys():
        print("Invalid name!")
    else:
        break

ans = []
queue = [["Kevin Bacon"]]
while queue:
    path = queue.pop(0)
    actor1 = path[-1]
    vis[actor1] = True
    for adj in costars.get(actor1, []):
        if adj == actor:
            ans = path + [adj]
            break
        if not vis.get(adj, False): queue.append(path + [adj])
    if ans:
        break

if not ans:
    print("Actor/Actress not connected to Kevin Bacon\n\n")
else:
    ans = ans[::-1]
    print("\n\nSeparation Degree: " + str(len(ans)-1) + "\n\n")
    for i in range(len(ans)):
        actor1 = ans[i]
        if actor1 == "Kevin Bacon":
            print(actor1.center(40))
        else:
            actor2 = ans[i+1]
            title = titles.get((actor1, actor2), "")
            print(actor1.center(40) + "\n" + "was in".center(40) + "\n" + title.center(40) + "\n" + "with".center(40))