import copy
from Data_Structures_and_Algorithms.Chapter_9.AdaptableHeapPriorityQueue import AdaptableHeapPriorityQueue
from Data_Structures_and_Algorithms.Chapter_9.HeapPriorityQueue import HeapPriorityQueue

class Vertex:
    '''Lightweight vertex structure for a graph.'''
    __slots__ = '_element'

    def __init__(self, x):
        '''Do not call constructor directly. Use Grpah's insert_vertex(x).'''
        self._element = x

    def element(self):
        '''Return element associated with this vertex.'''
        return self._element

    def __hash__(self): # Will allow vertex to be a map/set key
        return hash(id(self))

class Edge:
    '''Lightweight edge structure for a graph.'''
    __slots__ = '_origin', '_destination', '_element'

    def __init__(self, u, v, x):
        '''Do not call constructor directly. Use Graph's insert_edge(u, v, x).'''
        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self):
        '''Return (u,v) tuple for verticies u and v.'''
        return (self._origin, self._destination)

    def opposite(self, v):
        '''Return the vertex that is opposite v on this edge.'''
        return self._destination if v is self._origin else self._origin

    def element(self):
        '''Return element associated with this edge.'''
        return self._element

    def __hash__(self): # Will allow edge to be a map/set key
        return hash((self._origin, self._destination))

class Partition:
    '''Union-find structure for maintaining disjoint sets.'''
    class Position:
        __slots__ = '_container', '_element', '_size', '_parent'

        def __init__(self, container, e):
            '''Create a new position that is the leader of its own group.'''
            self._container = container # Reference to Partition instance
            self._element = e
            self._size = 1
            self._parent = self # Convention for a group leader

        def element(self):
            '''Return element stored at this position.'''
            return self._element

    def make_group(self, e):
        '''Makes a new group containing element e, and returns its Position.'''
        return self.Position(self, e)

    def find(self, p):
        '''Finds the group containing p and return the position of its leader.'''
        if p._parent != p:
            p._parent = self.find(p._parent) # Overwrite p._parent after recursion 
        return p._parent
    
    def union(self, p, q):
        '''Merges the groups containing elements p and q (in distinct).'''
        a = self.find(p)
        b = self.find(q)
        if a is not b: # Only merge if different groups
            if a._size > b._size:
                b._parent = a
                a._size += b._size 
            else:
                a._parent = b
                b._size += a._size

class Graph:
    '''Representation of a simple graph using an adjacency map.'''

    def __init__(self, directed=False):
        '''Create an empty graph (undirected, by default). Graph is directed if optional parameter is set to True.'''
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing # Only create second map for directed graph; use alias for undirected.

    def is_directed(self):
        '''Return True if this is a directed graph; False if undirected. Property is based on the original declaration of the graph, not its contents.'''
        return self._incoming is not self._outgoing # Directed if maps are distinct

    def vertex_count(self):
        '''Return the number of vertices in the graph.'''
        return len(self._outgoing)

    def vertices(self):
        '''Return an iteration of all vertices of the graph.'''
        return self._outgoing.keys()

    def edge_count(self):
        '''Return the number of edges in the graph.'''
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2 # For undirected graphs, make sure not to double count edges.

    def edges(self):
        '''Return a set of all edges of the graph.'''
        result = set() # Avoid double-reporting edges of undirected graph.
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values()) # Add edges to resulting set.
        return result

    def get_edge(self, u, v):
        '''Return the edge from u to v, or None if not adjacent.'''
        return self._outgoing[u].get(v) # Returns None if v not adjacent.

    def degree(self, v, outgoing=True):
        '''Return number of (outgoing) edges incident to vertex v in the graph. If graph is directed, optional parameter used to count incoming edges.'''
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        '''Return all (outgoing) edges incident to vertex v in the graph. If graph is directed, optional parameter used to reqest incoming edges.'''
        adj = self._outgoing if outgoing else self._incoming

    def insert_vertex(self, x=None):
        '''Insert and return a new Vertex with element x.'''
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {} # Need distinct map for incoming edges
        return v

    def insert_edge(self, u, v, x=None):
        '''Insert and return a new Edge from u to v with auxiliary element x.'''
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

    def remove_vertex(self, v):
        '''Remove a vertex v'''
        if self._outgoing[v]: 
            self._outgoing[v] = None
            if self.is_directed():
                self._incoming[v] = None

    def remove_edge(self, u, v):
        '''Remove an edge from u to v, returning None if it does not exist.'''
        if self.isdirected():
            if self._outgoing[u][v] == self._incoming[v][u]: # Check if the edge exists
                self._outgoing[u][v] = None # Now we wait for garbage collection to eat this
                self._incoming[v][u] = None
        if self._outgoing[u][v]:
            self._outoging[u][v] == None

    def DFS(self, u, discovered):
        '''Perform DFS of the undiscovered portion of Graph g starting at Vertex u. 
        discovered is a dictionary mapping each vertex to the edge that was used to
        discover it during the DFS. (u should be "discovered" prior to the call.)
        Newly discovered vertices will be added to the dictionary as a result.'''

        for e in self.incident_edges(u): # For every outgoing edge from u
            v = e.opposite(u)
            if v not in discovered: # v is an unvisited vertex
                discovered[v] = e # e is the tree edge that discovered v
                DFS(self, v, discovered)

    def construct_path_DFS(self, u, v, discovered):
        '''Builds a path from vertex u to vertex v.'''
        path = [] # Empty path by default
        if v in discovered:
            path.append(v) # We build list from v to u and then reverse it at the end.
            walk = v
            while walk is not u:
                e = discovered[walk] # Find edge leading to walk
                parent = e.opposite(walk)
                path.append(parent)
                walk = parent
            path.reverse() # Reorient path from u to v
        return path

    def DFS_complete(self, g):
        '''Perform DFS for entire graph and result forest as a dictionary. 
        Result maps each vertex v to the edge that was used to discover it.
        (Vertices that are roots of a DFS tree are mapped to None.)'''
        forest = {}
        for u in g.vertices():
            if u not in forest:
                forest[u] = None # u will be the root of a tree
                DFS(g, u, forest)
        return forest

    def BFS(self, s, discovered):
        '''Perform BFS of the undiscovered portion of the Graph starting at Vertex s.
        discovered is a dictionary mapping each vertex to the edge that was used to
        discover it during the BFS (s should be mapped to None prior to the call). 
        Newly discovered vertices will be added to the dictionary as a result.'''
        level = [s] # First level includes only s
        while len(level) > 0:
            next_level = [] # Prepare to gather newly found vertices
            for u in level:
                for e in self.incident_edges(u): # For every outgoing edge from u
                    v = e.opposite(u)
                    if v not in discovered: # v is an unvisited vertex
                        discovered[v] = e # e is the tree edge that discovered v
                        next_level.append(v) # v will be further considered in next pass
            level = next_level # Relabel 'next' level to become current

    def floyd_warshall(self):
        '''Return a new graph that is the transitive closure of g.'''
        closure = copy.deepcopy(self) # Imported from copy module
        verts = list(closure.verticess()) # Make indexable list
        n = len(verts)
        for k in range(n):
            for i in range(n):
                # Verify that edge (i,k) exists in the partial closure
                if i != k and closure.get_edge(verts[i], verts[k]) is not None:
                    for j in range(n):
                        # Verify that edge (k,j) exists in the partial closure
                        if i != j != k and closure.get_edge(verts[k], verts[j]) is not None:
                            # if (i,j) not yet included, add it to the closure
                            if closure.get_edge(verts[i], verts[j]) is None:
                                closure.insert_edge(verts[i], verts[j])
        return closure

    def topological_sort(self):
        '''Return a list of vertices of directed acrylic graph in topological order. 
        If graph has a cycle, the result will be incomplete.'''
        topo = [] # A list of vertices places in topological order
        ready = [] # list of vertices that have no remaining constraints
        incount = {} # keep track of in-degree for each vertex
        for u in self.vertices():
            incount[u] = self.degree(u, False) # parameter requests incoming degree
            if incount[u] == 0: # If u has no incoming edges,
                ready.append(u) # It is free of constraints
        while len(ready) > 0:
            u = ready.pop() # u is free of constraints
            topo.append(u) # Add u to the topological order
            for e in self.incident_edges(u): # Consider all outgoing neighbors of u
                v = e.opposite(u)
                incount[v] -= 1 # v has one less contraint without u
                if incount[v] == 0:
                    ready.append(v)
        return topo

    def shortest_path_lengths(self, src):
        '''Compute shortest-path distances from src to reachable vertices of the graph.
        The graph can be directed or undirected, but must be weighted such that 
        e.element() returns a numeric weight for each edge e. Return dictionary mapping
        each reachable vertex to its distance from src, uising Dijkstra's Algorithm.'''

        d = {} # d[v] is upper bound from s to v
        cloud = {} # map reachable v to its d[v] value
        pq = AdaptableHeapPriorityQueue() # Vertex v will have key d[v]
        pqlocator = {} # Map from vertex to its pq locator

        # for each vertex v of the graph, add an entry to the priority queue, with
        # the source having distance 0 and all others having infinite distance.
        for v in self.vertices():
           if v is src:
               d[v] = 0
           else:
               d[v] = float('inf') # Syntax for positive infinity
           pqlocator[v] = pq.add(d[v], v) # Save locator for future updates

        while not pq.is_empty():
            key, u = pq.remove_min()
            cloud[u] = key # its correct d[u] value
            del pqlocator[u] # u is no longer in pq
            for e in self.incident_edges(u): # Outgoing edges (u,v)
                v = e.opposite(u)
                if v not in cloud:
                    # Perform relaxation step on edge (u,v)
                    wgt = e.element()
                    if d[u] + wgt < d[v]: # Better path to v?
                        d[v] = d[u] + wgt # Update the distance
                        pq.update(pqlocator[v], d[v], v) # Update the pq entry
        return cloud # Only includes reachable vertices

    def shortest_path_tree(self, s, d):
        '''Reconstruct shortest-path tree rooted at vertex s, given distance map d.
        Return tree as a map from eaech reachable vertex v (other than s) to the
        edge e=(u,v) that is used to reach v from its parent u in the tree.'''
        tree = {}
        for v in d:
            if v is not s:
                for e in self.incident_edges(v, False): # Consider INCOMING edges
                    u = e.opposite(v)
                    wgt = e.element()
                    if d[v] == d[u] + wgt:
                        tree[v] = e # Edge e is used to reach v
        return tree

    def MST_PrimJarnik(self):
        '''Compute a minimum spanning tree of weighted graph g. Return a list of
        edges that comprise the MST (in arbitrary order).'''
        d = {} # d[v] is bound on distance to tree
        tree = [] # list of edges in spanning tree
        pq = AdaptableHeapPriorityQueue() # d[v] maps to value (v, e=(u,v))
        pqlocator = {} # map from vertex to its pq locator

        # for each vertex v of the graph, add an entry to the priority queue, with
        # the source having distance 0 and all others having infinite distance
        for v in self.vertices():
            if len(d) == 0: # This is the first node
                d[v] = 0 # Make it the root
            else:
                d[v] = float('inf') # Positive infinity
            pqlocator[v] = pq.add(d[v], (v,None))

        while not pq.is_empty():
            key, value = pq.remove_min()
            u, edge = value # Unpack tuple from pq
            del pqlocator[u]  # u is no longer in pq
            if edge is not None: 
                tree.append(edge) # Add edge to tree
            for link in self.incident_edges(u):
                v = link.opposite(u)
                if v in pqlocator: # Thus v not yet in tree
                    # See if edge (u,v) better connects v to the growing tree
                    wgt = link.element()
                    if wgt < d[v]: # better edge to v?
                        d[v] = wgt # update the distance
                        pq.update(pqlocator[v], d[v], (v, link)) # Update the pq entry
        return tree

    def MST_Kruskal(self):
        '''Compute a minimum spanning tree of a graph using Kruskal's algorithm. Return
        a list of edges that comprise the MST. The elements of the graph's edges are
        assumed to be weights.'''
        tree = [] # list of edges in spanning tree
        pq = HeapPriorityQueue() # Entries are edges in G, with weights as key
        forest = Partition()
        position = {} # Map each node to its Partition entry

        for v in self.vertices():
            position[v] = forest.make_group(v)
        
        for e in self.edges():
            pq.add(e.element(), e) # edge's element is assumed to be its weight

        size = self.vertex_count()
        while len(tree) != size - 1 and not pq.is_empty():
            # Tree not spanning and unprocessed edges remain
            weight, edge = pq.remove_min()
            u, v = edge.endpoints()
            a = forest.find(position[u])
            b = forest.find(position[v])
            if a != b:
                tree.append(edge)
                forest.union(a,b)
        return tree