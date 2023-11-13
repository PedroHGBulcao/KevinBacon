import pandas as pd
import networkx as nx

movies = pd.read_csv("netflix_titles.csv")
movies = movies.dropna(subset='cast')
costars = []
titles = {}
actor_names = set()
G = nx.Graph()
for cast, title in movies[['cast', 'title']].itertuples(index=False):
    actors = cast.split(", ")
    for actor in actors:
        actor_names.add(actor)
        for actor1 in actors:
            if not actor == actor1:
                costars.append([actor, actor1])
                titles[(actor, actor1)] = title

G.add_edges_from(costars)

while True:
    actor = input("Choose an actor/actress: ")
    if actor not in actor_names:
        print("Invalid name!")
    else:
        break

ans = nx.shortest_path(G, source="Kevin Bacon", target=actor)
print(ans)
queue = [[("Kevin Bacon", "")]]

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
            title = titles[(actor1, actor2)]
            print(actor1.center(40) + "\n" + "was in".center(40) + "\n" + title.center(40) + "\n" + "with".center(40))