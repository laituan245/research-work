
'''
The data (in short) will be in json format as follows.

{
   "nodes":
       [ { "id": "1", "label": "Cities", "value": 35}, {}, ...]

   "edges":
       [ { "id": "1", "source": "5", "target": "3", "value": 12}, {}, ...]
}
 The task:
   + Create a random data with 500 nodes and 300 edges within them
   + Print out average number of in-links and out-links per node?
'''

import random
import json
random.seed(2405)

nouns = []
f = open('nounlist.txt', 'r')
for noun in f:
    if len(noun.strip()) > 0:
        nouns.append(noun.strip())
random.shuffle(nouns)
f.close()

nodes = []
for i in range(500):
    newNode = {}
    newNode["id"] = i + 1
    newNode["label"] = nouns[i]
    newNode["value"] = random.randint(1,2000)
    nodes.append(newNode)


pairs = []
for i in range(500):
    for j in range(500):
        pairs.append((i,j))
random.shuffle(pairs)

edges = []
while len(edges) != 300:
    edges = []
    inDegree = {}
    outDegree = {}
    for i in range(500):
        inDegree[i+1] = 0
        outDegree[i+1] = 0

    edgeId = 0;
    for i, j in pairs:       
        if len(edges) == 300:
            break
        if i != j:
            if random.randint(1,1000) % 2:
                edgeId = edgeId + 1
                newEdge = {}
                newEdge["id"] = edgeId
                newEdge["source"] = i + 1
                newEdge["target"] = j + 1
                inDegree[j+1] += 1
                outDegree[i+1] += 1
                newEdge["value"] = random.randint(1,2000)
                edges.append(newEdge)

f = open('randomdata.txt', 'w')
f.write(json.dumps({"nodes": nodes, "edges": edges}))
f.close()
