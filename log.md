
Solving Air Cargo Problem 1 using breadth_first_search...

# Actions   Expansions   Goal Tests   New Nodes
    20          43          56         178    

Plan length: 6  Time elapsed in seconds: 0.003903252014424652
Load(C1, P1, SFO)
Load(C2, P2, JFK)
Fly(P2, JFK, SFO)
Unload(C2, P2, SFO)
Fly(P1, SFO, JFK)
Unload(C1, P1, JFK)


Solving Air Cargo Problem 1 using depth_first_graph_search...

# Actions   Expansions   Goal Tests   New Nodes
    20          21          22          84    

Plan length: 20  Time elapsed in seconds: 0.002109251043293625
Fly(P1, SFO, JFK)
Fly(P2, JFK, SFO)
Load(C2, P1, JFK)
Fly(P1, JFK, SFO)
Fly(P2, SFO, JFK)
Unload(C2, P1, SFO)
Fly(P1, SFO, JFK)
Fly(P2, JFK, SFO)
Load(C2, P2, SFO)
Fly(P1, JFK, SFO)
Load(C1, P2, SFO)
Fly(P2, SFO, JFK)
Fly(P1, SFO, JFK)
Unload(C2, P2, JFK)
Unload(C1, P2, JFK)
Fly(P2, JFK, SFO)
Load(C2, P1, JFK)
Fly(P1, JFK, SFO)
Fly(P2, SFO, JFK)
Unload(C2, P1, SFO)


Solving Air Cargo Problem 1 using uniform_cost_search...

# Actions   Expansions   Goal Tests   New Nodes
    20          60          62         240    

Plan length: 6  Time elapsed in seconds: 0.0065577380009926856
Load(C2, P2, JFK)
Fly(P2, JFK, SFO)
Load(C1, P2, SFO)
Unload(C2, P2, SFO)
Fly(P2, SFO, JFK)
Unload(C1, P2, JFK)


Solving Air Cargo Problem 1 using greedy_best_first_graph_search with h_unmet_goals...

# Actions   Expansions   Goal Tests   New Nodes
    20          7           9           29    

Plan length: 6  Time elapsed in seconds: 0.001090473961085081
Load(C1, P1, SFO)
Load(C2, P2, JFK)
Fly(P2, JFK, SFO)
Unload(C2, P2, SFO)
Fly(P1, SFO, JFK)
Unload(C1, P1, JFK)


Solving Air Cargo Problem 1 using greedy_best_first_graph_search with h_pg_levelsum...

# Actions   Expansions   Goal Tests   New Nodes
    20          6           8           28    

Plan length: 6  Time elapsed in seconds: 0.27776889299275354
Load(C1, P1, SFO)
Fly(P1, SFO, JFK)
Unload(C1, P1, JFK)
Load(C2, P2, JFK)
Fly(P2, JFK, SFO)
Unload(C2, P2, SFO)


Solving Air Cargo Problem 1 using greedy_best_first_graph_search with h_pg_maxlevel...

# Actions   Expansions   Goal Tests   New Nodes
    20          6           8           24    

Plan length: 6  Time elapsed in seconds: 0.19442935899132863
Load(C1, P1, SFO)
Load(C2, P2, JFK)
Fly(P2, JFK, SFO)
Fly(P1, SFO, JFK)
Unload(C2, P2, SFO)
Unload(C1, P1, JFK)


Solving Air Cargo Problem 1 using greedy_best_first_graph_search with h_pg_setlevel...

# Actions   Expansions   Goal Tests   New Nodes
    20          13          15          53    

Plan length: 6  Time elapsed in seconds: 1.1674241700093262
Load(C1, P1, SFO)
Load(C2, P2, JFK)
Fly(P2, JFK, SFO)
Fly(P1, SFO, JFK)
Unload(C2, P2, SFO)
Unload(C1, P1, JFK)


Solving Air Cargo Problem 1 using astar_search with h_unmet_goals...

# Actions   Expansions   Goal Tests   New Nodes
    20          50          52         206    

Plan length: 6  Time elapsed in seconds: 0.0061697299825027585
Load(C2, P2, JFK)
Fly(P2, JFK, SFO)
Unload(C2, P2, SFO)
Load(C1, P2, SFO)
Fly(P2, SFO, JFK)
Unload(C1, P2, JFK)


Solving Air Cargo Problem 1 using astar_search with h_pg_levelsum...

# Actions   Expansions   Goal Tests   New Nodes
    20          28          30         122    

Plan length: 6  Time elapsed in seconds: 0.698256575036794
Load(C2, P2, JFK)
Fly(P2, JFK, SFO)
Unload(C2, P2, SFO)
Load(C1, P2, SFO)
Fly(P2, SFO, JFK)
Unload(C1, P2, JFK)


Solving Air Cargo Problem 1 using astar_search with h_pg_maxlevel...

# Actions   Expansions   Goal Tests   New Nodes
    20          43          45         180    

Plan length: 6  Time elapsed in seconds: 0.7149500470259227
Load(C2, P2, JFK)
Fly(P2, JFK, SFO)
Load(C1, P2, SFO)
Unload(C2, P2, SFO)
Fly(P2, SFO, JFK)
Unload(C1, P2, JFK)


Solving Air Cargo Problem 1 using astar_search with h_pg_setlevel...

# Actions   Expansions   Goal Tests   New Nodes
    20          46          48         192    

Plan length: 6  Time elapsed in seconds: 2.2212938320008107
Load(C2, P2, JFK)
Fly(P2, JFK, SFO)
Load(C1, P2, SFO)
Unload(C2, P2, SFO)
Fly(P2, SFO, JFK)
Unload(C1, P2, JFK)


Solving Air Cargo Problem 2 using breadth_first_search...

# Actions   Expansions   Goal Tests   New Nodes
    72         3343        4609       30503   

Plan length: 9  Time elapsed in seconds: 1.32031930598896
Load(C1, P1, SFO)
Load(C2, P2, JFK)
Load(C3, P3, ATL)
Fly(P2, JFK, SFO)
Unload(C2, P2, SFO)
Fly(P1, SFO, JFK)
Unload(C1, P1, JFK)
Fly(P3, ATL, SFO)
Unload(C3, P3, SFO)


Solving Air Cargo Problem 2 using depth_first_graph_search...

# Actions   Expansions   Goal Tests   New Nodes
    72         624         625         5602   

Plan length: 619  Time elapsed in seconds: 1.9629616820020601
Fly(P3, ATL, SFO)
Fly(P1, SFO, ATL)
Fly(P3, SFO, JFK)
Fly(P1, ATL, JFK)
Fly(P2, JFK, ATL)
Fly(P3, JFK, ATL)
Fly(P2, ATL, SFO)
Fly(P3, ATL, SFO)
Load(C2, P1, JFK)
Fly(P2, SFO, ATL)
Fly(P1, JFK, ATL)
Fly(P2, ATL, JFK)
Fly(P1, ATL, SFO)
Fly(P3, SFO, ATL)
Fly(P1, SFO, JFK)
Load(C3, P3, ATL)
Fly(P3, ATL, SFO)
Fly(P2, JFK, ATL)
Fly(P3, SFO, JFK)
Fly(P2, ATL, SFO)
Fly(P1, JFK, ATL)
Fly(P2, SFO, JFK)
Fly(P1, ATL, SFO)
Unload(C3, P3, JFK)
Fly(P1, SFO, JFK)
Fly(P3, JFK, ATL)
Fly(P2, JFK, ATL)
Fly(P3, ATL, SFO)
Fly(P2, ATL, SFO)
Fly(P1, JFK, ATL)
Fly(P3, SFO, ATL)
Fly(P1, ATL, SFO)
Unload(C2, P1, SFO)
Fly(P3, ATL, SFO)
Fly(P2, SFO, ATL)
Fly(P1, SFO, ATL)
Fly(P2, ATL, JFK)
Fly(P1, ATL, JFK)
Fly(P3, SFO, ATL)
Fly(P2, JFK, ATL)
Fly(P3, ATL, JFK)
Fly(P2, ATL, SFO)
Fly(P1, JFK, ATL)
Load(C3, P3, JFK)
Fly(P1, ATL, SFO)
Fly(P2, SFO, ATL)
Fly(P3, JFK, ATL)
Fly(P2, ATL, JFK)
Fly(P3, ATL, SFO)
Fly(P1, SFO, ATL)
Fly(P2, JFK, ATL)
Fly(P1, ATL, JFK)
Fly(P2, ATL, SFO)
Fly(P3, SFO, ATL)
Unload(C3, P3, ATL)
Fly(P3, ATL, SFO)
Fly(P2, SFO, ATL)
Fly(P3, SFO, JFK)
Fly(P2, ATL, JFK)
Fly(P1, JFK, ATL)
Fly(P3, JFK, ATL)
Fly(P2, JFK, ATL)
Load(C3, P2, ATL)
Fly(P3, ATL, SFO)
Fly(P2, ATL, SFO)
Fly(P1, ATL, SFO)
Fly(P3, SFO, ATL)
Fly(P2, SFO, JFK)
Fly(P3, ATL, JFK)
Fly(P1, SFO, JFK)
Fly(P2, JFK, SFO)
Unload(C3, P2, SFO)
Fly(P2, SFO, ATL)
Fly(P3, JFK, ATL)
Fly(P2, ATL, JFK)
Fly(P3, ATL, SFO)
Load(C2, P3, SFO)
Fly(P3, SFO, ATL)
Fly(P2, JFK, ATL)
Fly(P3, ATL, JFK)
Fly(P2, ATL, SFO)
Fly(P1, JFK, ATL)
Fly(P2, SFO, JFK)
Fly(P1, ATL, SFO)
Unload(C2, P3, JFK)
Fly(P1, SFO, JFK)
Fly(P3, JFK, ATL)
Fly(P2, JFK, ATL)
Fly(P3, ATL, SFO)
Fly(P2, ATL, SFO)
Fly(P1, JFK, ATL)
Fly(P3, SFO, ATL)
Fly(P1, ATL, SFO)
Load(C3, P2, SFO)
Fly(P3, ATL, SFO)
Fly(P2, SFO, ATL)
Fly(P1, SFO, ATL)
Fly(P2, ATL, JFK)
Fly(P1, ATL, JFK)
Fly(P3, SFO, ATL)
Load(C2, P2, JFK)
Fly(P3, ATL, JFK)
Fly(P2, JFK, ATL)
Fly(P1, JFK, ATL)
Fly(P2, ATL, SFO)
Fly(P1, ATL, SFO)
Unload(C3, P2, SFO)
Fly(P2, SFO, ATL)
Fly(P1, SFO, ATL)
Fly(P2, ATL, JFK)
Fly(P3, JFK, ATL)
Fly(P1, ATL, SFO)
Fly(P3, ATL, SFO)
Fly(P1, SFO, JFK)
Fly(P2, JFK, ATL)
Fly(P3, SFO, ATL)
Fly(P2, ATL, SFO)
Load(C1, P2, SFO)
Fly(P3, ATL, SFO)
Fly(P2, SFO, ATL)
Fly(P3, SFO, JFK)
Fly(P2, ATL, JFK)
Fly(P1, JFK, ATL)
Fly(P3, JFK, ATL)
Fly(P1, ATL, SFO)
Fly(P3, ATL, SFO)
Unload(C2, P2, JFK)
Fly(P1, SFO, ATL)
Fly(P2, JFK, ATL)
Fly(P1, ATL, JFK)
Fly(P3, SFO, ATL)
Fly(P2, ATL, SFO)
Fly(P3, ATL, JFK)
Fly(P1, JFK, ATL)
Load(C3, P2, SFO)
Fly(P1, ATL, SFO)
Fly(P2, SFO, ATL)
Fly(P1, SFO, JFK)
Fly(P2, ATL, JFK)
Fly(P3, JFK, ATL)
Fly(P1, JFK, ATL)
Fly(P3, ATL, SFO)
Fly(P1, ATL, SFO)
Unload(C3, P2, JFK)
Fly(P3, SFO, ATL)
Fly(P2, JFK, ATL)
Fly(P3, ATL, JFK)
Fly(P2, ATL, SFO)
Fly(P1, SFO, ATL)
Fly(P2, SFO, JFK)
Unload(C1, P2, JFK)
Fly(P1, ATL, SFO)
Fly(P2, JFK, ATL)
Fly(P1, SFO, JFK)
Fly(P2, ATL, SFO)
Fly(P3, JFK, ATL)
Fly(P2, SFO, JFK)
Fly(P3, ATL, SFO)
Load(C3, P2, JFK)
Fly(P2, JFK, ATL)
Fly(P3, SFO, ATL)
Fly(P2, ATL, SFO)
Fly(P3, ATL, JFK)
Fly(P1, JFK, ATL)
Fly(P2, SFO, ATL)
Fly(P1, ATL, SFO)
Unload(C3, P2, ATL)
Fly(P2, ATL, SFO)
Fly(P1, SFO, ATL)
Fly(P2, SFO, JFK)
Fly(P1, ATL, JFK)
Fly(P3, JFK, ATL)
Fly(P2, JFK, SFO)
Fly(P3, ATL, SFO)
Load(C2, P1, JFK)
Fly(P2, SFO, ATL)
Fly(P3, SFO, ATL)
Fly(P1, JFK, ATL)
Fly(P2, ATL, SFO)
Fly(P1, ATL, SFO)
Fly(P3, ATL, JFK)
Fly(P2, SFO, ATL)
Unload(C2, P1, SFO)
Fly(P2, ATL, JFK)
Fly(P1, SFO, ATL)
Fly(P3, JFK, ATL)
Fly(P1, ATL, JFK)
Fly(P3, ATL, SFO)
Fly(P2, JFK, ATL)
Fly(P1, JFK, ATL)
Fly(P2, ATL, SFO)
Fly(P1, ATL, SFO)
Load(C2, P3, SFO)
Fly(P3, SFO, ATL)
Fly(P2, SFO, ATL)
Fly(P1, SFO, ATL)
Fly(P3, ATL, JFK)
Fly(P1, ATL, JFK)
Fly(P2, ATL, SFO)
Load(C1, P3, JFK)
Fly(P2, SFO, JFK)
Fly(P3, JFK, ATL)
Fly(P2, JFK, ATL)
Fly(P3, ATL, SFO)
Fly(P1, JFK, ATL)
Fly(P2, ATL, SFO)
Fly(P1, ATL, SFO)
Fly(P3, SFO, ATL)
Unload(C2, P3, ATL)
Fly(P3, ATL, SFO)
Fly(P2, SFO, ATL)
Fly(P1, SFO, ATL)
Fly(P2, ATL, JFK)
Fly(P1, ATL, JFK)
Fly(P3, SFO, JFK)
Fly(P2, JFK, ATL)
Unload(C1, P3, JFK)
Fly(P2, ATL, SFO)
Fly(P3, JFK, ATL)
Fly(P2, SFO, JFK)
Fly(P3, ATL, SFO)
Fly(P1, JFK, ATL)
Fly(P3, SFO, JFK)
Fly(P1, ATL, SFO)
Load(C1, P2, JFK)
Fly(P1, SFO, JFK)
Fly(P2, JFK, ATL)
Fly(P3, JFK, ATL)
Fly(P2, ATL, SFO)
Fly(P3, ATL, SFO)
Fly(P1, JFK, ATL)
Fly(P2, SFO, ATL)
Fly(P1, ATL, SFO)
Unload(C1, P2, ATL)
Fly(P2, ATL, SFO)
Fly(P1, SFO, ATL)
Fly(P3, SFO, ATL)
Fly(P1, ATL, JFK)
Fly(P3, ATL, JFK)
Fly(P2, SFO, JFK)
Fly(P1, JFK, ATL)
Fly(P2, JFK, ATL)
Load(C3, P2, ATL)
Fly(P2, ATL, SFO)
Fly(P1, ATL, SFO)
Fly(P2, SFO, JFK)
Fly(P1, SFO, JFK)
Fly(P3, JFK, ATL)
Fly(P2, JFK, ATL)
Fly(P3, ATL, SFO)
Fly(P2, ATL, SFO)
Unload(C3, P2, SFO)
Fly(P3, SFO, ATL)
Fly(P2, SFO, ATL)
Fly(P3, ATL, JFK)
Fly(P2, ATL, JFK)
Fly(P1, JFK, ATL)
Fly(P3, JFK, ATL)
Fly(P1, ATL, SFO)
Fly(P3, ATL, SFO)
Fly(P2, JFK, ATL)
Fly(P1, SFO, ATL)
Load(C3, P3, SFO)
Fly(P2, ATL, SFO)
Fly(P1, ATL, SFO)
Fly(P3, SFO, ATL)
Fly(P2, SFO, ATL)
Fly(P3, ATL, JFK)
Fly(P2, ATL, JFK)
Fly(P1, SFO, ATL)
Fly(P3, JFK, ATL)
Fly(P1, ATL, JFK)
Load(C2, P3, ATL)
Fly(P3, ATL, SFO)
Fly(P2, JFK, ATL)
Fly(P3, SFO, JFK)
Fly(P2, ATL, SFO)
Fly(P1, JFK, ATL)
Fly(P2, SFO, JFK)
Fly(P1, ATL, SFO)
Unload(C3, P3, JFK)
Fly(P1, SFO, JFK)
Fly(P3, JFK, ATL)
Fly(P2, JFK, ATL)
Fly(P3, ATL, SFO)
Fly(P2, ATL, SFO)
Fly(P1, JFK, ATL)
Fly(P3, SFO, ATL)
Fly(P1, ATL, SFO)
Unload(C2, P3, ATL)
Fly(P3, ATL, SFO)
Fly(P2, SFO, ATL)
Fly(P1, SFO, ATL)
Fly(P2, ATL, JFK)
Fly(P1, ATL, JFK)
Load(C3, P1, JFK)
Fly(P3, SFO, ATL)
Fly(P2, JFK, ATL)
Fly(P3, ATL, JFK)
Fly(P2, ATL, SFO)
Fly(P1, JFK, ATL)
Load(C2, P1, ATL)
Fly(P1, ATL, SFO)
Fly(P2, SFO, ATL)
Fly(P1, SFO, JFK)
Fly(P2, ATL, JFK)
Fly(P3, JFK, ATL)
Fly(P1, JFK, ATL)
Fly(P3, ATL, SFO)
Fly(P1, ATL, SFO)
Unload(C3, P1, SFO)
Fly(P3, SFO, ATL)
Fly(P1, SFO, JFK)
Fly(P3, ATL, JFK)
Fly(P2, JFK, ATL)
Fly(P1, JFK, ATL)
Fly(P2, ATL, SFO)
Fly(P3, JFK, ATL)
Load(C3, P2, SFO)
Fly(P3, ATL, SFO)
Fly(P1, ATL, SFO)
Fly(P2, SFO, ATL)
Fly(P3, SFO, ATL)
Fly(P2, ATL, JFK)
Fly(P3, ATL, JFK)
Fly(P1, SFO, ATL)
Unload(C3, P2, JFK)
Fly(P3, JFK, ATL)
Fly(P2, JFK, ATL)
Fly(P1, ATL, SFO)
Fly(P3, ATL, SFO)
Fly(P2, ATL, SFO)
Fly(P1, SFO, ATL)
Load(C1, P1, ATL)
Fly(P1, ATL, SFO)
Fly(P2, SFO, ATL)
Fly(P3, SFO, ATL)
Fly(P2, ATL, JFK)
Fly(P1, SFO, JFK)
Fly(P3, ATL, SFO)
Load(C3, P2, JFK)
Fly(P3, SFO, JFK)
Fly(P2, JFK, ATL)
Fly(P3, JFK, ATL)
Fly(P2, ATL, SFO)
Fly(P1, JFK, SFO)
Fly(P3, ATL, SFO)
Fly(P2, SFO, ATL)
Fly(P1, SFO, ATL)
Unload(C3, P2, ATL)
Fly(P2, ATL, SFO)
Fly(P1, ATL, SFO)
Fly(P3, SFO, ATL)
Fly(P2, SFO, ATL)
Fly(P3, ATL, JFK)
Fly(P2, ATL, JFK)
Fly(P1, SFO, ATL)
Fly(P3, JFK, ATL)
Fly(P1, ATL, JFK)
Fly(P3, ATL, SFO)
Unload(C2, P1, JFK)
Fly(P2, JFK, ATL)
Fly(P3, SFO, ATL)
Fly(P1, JFK, ATL)
Fly(P2, ATL, SFO)
Fly(P3, ATL, SFO)
Fly(P1, ATL, SFO)
Fly(P3, SFO, JFK)
Fly(P2, SFO, ATL)
Load(C3, P2, ATL)
Fly(P2, ATL, SFO)
Fly(P1, SFO, ATL)
Fly(P2, SFO, JFK)
Fly(P3, JFK, ATL)
Fly(P1, ATL, SFO)
Fly(P3, ATL, SFO)
Unload(C3, P2, JFK)
Fly(P1, SFO, ATL)
Fly(P2, JFK, ATL)
Fly(P1, ATL, JFK)
Fly(P2, ATL, SFO)
Load(C3, P1, JFK)
Fly(P3, SFO, ATL)
Fly(P2, SFO, ATL)
Fly(P3, ATL, JFK)
Fly(P2, ATL, JFK)
Fly(P1, JFK, ATL)
Fly(P3, JFK, ATL)
Fly(P1, ATL, SFO)
Fly(P3, ATL, SFO)
Fly(P2, JFK, ATL)
Fly(P1, SFO, ATL)
Unload(C1, P1, ATL)
Fly(P2, ATL, SFO)
Fly(P1, ATL, SFO)
Fly(P3, SFO, ATL)
Fly(P2, SFO, ATL)
Fly(P3, ATL, JFK)
Fly(P2, ATL, JFK)
Unload(C3, P1, SFO)
Fly(P1, SFO, ATL)
Fly(P3, JFK, ATL)
Fly(P2, JFK, ATL)
Load(C1, P3, ATL)
Fly(P3, ATL, SFO)
Fly(P1, ATL, SFO)
Fly(P2, ATL, SFO)
Fly(P3, SFO, ATL)
Fly(P2, SFO, JFK)
Fly(P3, ATL, JFK)
Fly(P1, SFO, ATL)
Fly(P2, JFK, SFO)
Fly(P1, ATL, JFK)
Fly(P2, SFO, ATL)
Unload(C1, P3, JFK)
Fly(P2, ATL, JFK)
Fly(P3, JFK, ATL)
Fly(P1, JFK, ATL)
Fly(P2, JFK, ATL)
Fly(P3, ATL, SFO)
Fly(P2, ATL, SFO)
Fly(P1, ATL, SFO)
Fly(P3, SFO, ATL)
Load(C3, P1, SFO)
Fly(P3, ATL, JFK)
Fly(P2, SFO, ATL)
Fly(P1, SFO, ATL)
Fly(P3, JFK, ATL)
Fly(P2, ATL, JFK)
Fly(P3, ATL, SFO)
Fly(P1, ATL, SFO)
Load(C2, P2, JFK)
Fly(P3, SFO, ATL)
Fly(P1, SFO, JFK)
Fly(P3, ATL, JFK)
Fly(P2, JFK, ATL)
Fly(P1, JFK, ATL)
Fly(P2, ATL, SFO)
Fly(P1, ATL, SFO)
Unload(C3, P1, SFO)
Fly(P2, SFO, ATL)
Fly(P1, SFO, ATL)
Fly(P3, JFK, ATL)
Fly(P2, ATL, SFO)
Fly(P3, ATL, SFO)
Fly(P1, ATL, JFK)
Fly(P2, SFO, ATL)
Unload(C2, P2, ATL)
Fly(P2, ATL, SFO)
Fly(P3, SFO, ATL)
Fly(P2, SFO, JFK)
Fly(P3, ATL, JFK)
Fly(P1, JFK, ATL)
Fly(P3, JFK, SFO)
Fly(P1, ATL, SFO)
Load(C3, P3, SFO)
Fly(P3, SFO, ATL)
Fly(P1, SFO, ATL)
Fly(P3, ATL, JFK)
Fly(P1, ATL, JFK)
Fly(P2, JFK, ATL)
Fly(P3, JFK, ATL)
Load(C2, P3, ATL)
Fly(P3, ATL, SFO)
Fly(P2, ATL, SFO)
Fly(P3, SFO, JFK)
Fly(P2, SFO, JFK)
Fly(P1, JFK, ATL)
Fly(P2, JFK, ATL)
Fly(P1, ATL, SFO)
Load(C1, P3, JFK)
Fly(P2, ATL, SFO)
Fly(P1, SFO, ATL)
Fly(P3, JFK, ATL)
Fly(P1, ATL, JFK)
Fly(P3, ATL, SFO)
Fly(P2, SFO, ATL)
Fly(P1, JFK, ATL)
Fly(P2, ATL, JFK)
Fly(P1, ATL, SFO)
Fly(P3, SFO, ATL)
Unload(C2, P3, ATL)
Fly(P3, ATL, SFO)
Fly(P1, SFO, ATL)
Fly(P2, JFK, ATL)
Fly(P1, ATL, JFK)
Fly(P2, ATL, SFO)
Fly(P3, SFO, JFK)
Fly(P1, JFK, ATL)
Unload(C3, P3, JFK)
Fly(P1, ATL, SFO)
Fly(P2, SFO, ATL)
Fly(P1, SFO, JFK)
Fly(P2, ATL, JFK)
Fly(P3, JFK, ATL)
Fly(P1, JFK, ATL)
Fly(P3, ATL, SFO)
Fly(P1, ATL, SFO)
Unload(C1, P3, SFO)
Fly(P3, SFO, ATL)
Fly(P1, SFO, ATL)
Fly(P3, ATL, JFK)
Fly(P1, ATL, JFK)
Fly(P2, JFK, ATL)
Fly(P3, JFK, ATL)
Fly(P2, ATL, SFO)
Fly(P3, ATL, SFO)
Load(C3, P1, JFK)
Fly(P2, SFO, ATL)
Fly(P1, JFK, ATL)
Fly(P2, ATL, JFK)
Fly(P1, ATL, SFO)
Fly(P3, SFO, ATL)
Fly(P1, SFO, JFK)
Load(C2, P3, ATL)
Fly(P3, ATL, SFO)
Fly(P2, JFK, ATL)
Fly(P3, SFO, JFK)
Fly(P2, ATL, SFO)
Fly(P1, JFK, ATL)
Fly(P3, JFK, ATL)
Fly(P1, ATL, SFO)
Fly(P3, ATL, SFO)
Unload(C3, P1, SFO)
Fly(P2, SFO, ATL)
Unload(C2, P3, SFO)
Load(C3, P1, SFO)
Fly(P2, ATL, JFK)
Fly(P3, SFO, ATL)
Fly(P2, JFK, SFO)
Fly(P3, ATL, JFK)
Fly(P1, SFO, ATL)
Fly(P3, JFK, SFO)
Fly(P1, ATL, JFK)
Load(C2, P2, SFO)
Fly(P3, SFO, ATL)
Fly(P2, SFO, ATL)
Fly(P3, ATL, JFK)
Fly(P2, ATL, JFK)
Fly(P1, JFK, ATL)
Fly(P3, JFK, ATL)
Unload(C3, P1, ATL)
Fly(P1, ATL, JFK)
Fly(P3, ATL, SFO)
Fly(P2, JFK, ATL)
Fly(P1, JFK, ATL)
Fly(P2, ATL, SFO)
Fly(P1, ATL, SFO)
Fly(P3, SFO, ATL)
Fly(P2, SFO, ATL)
Fly(P3, ATL, JFK)
Fly(P2, ATL, JFK)
Load(C1, P1, SFO)
Fly(P1, SFO, ATL)
Fly(P3, JFK, ATL)
Fly(P1, ATL, JFK)
Fly(P2, JFK, ATL)
Fly(P3, ATL, SFO)
Fly(P2, ATL, SFO)
Fly(P3, SFO, JFK)
Unload(C2, P2, SFO)
Fly(P2, SFO, ATL)
Fly(P3, JFK, ATL)
Fly(P1, JFK, ATL)
Fly(P3, ATL, SFO)
Fly(P2, ATL, SFO)
Unload(C1, P1, ATL)
Fly(P1, ATL, SFO)
Fly(P3, SFO, ATL)
Fly(P2, SFO, ATL)
Fly(P3, ATL, JFK)
Fly(P2, ATL, JFK)
Fly(P1, SFO, ATL)
Fly(P3, JFK, ATL)
Fly(P1, ATL, JFK)
Fly(P3, ATL, SFO)
Fly(P2, JFK, ATL)
Load(C3, P2, ATL)
Fly(P2, ATL, SFO)
Fly(P3, SFO, ATL)
Fly(P2, SFO, JFK)
Fly(P3, ATL, JFK)
Fly(P1, JFK, ATL)
Fly(P2, JFK, ATL)
Fly(P3, JFK, ATL)
Load(C1, P3, ATL)
Fly(P2, ATL, SFO)
Fly(P1, ATL, SFO)
Fly(P3, ATL, JFK)
Fly(P2, SFO, ATL)
Fly(P1, SFO, JFK)
Fly(P2, ATL, JFK)
Fly(P1, JFK, ATL)
Fly(P3, JFK, SFO)
Fly(P1, ATL, SFO)
Unload(C3, P2, JFK)
Fly(P3, SFO, ATL)
Fly(P1, SFO, ATL)
Fly(P2, JFK, ATL)
Fly(P3, ATL, JFK)
Fly(P2, ATL, SFO)
Fly(P1, ATL, SFO)
Unload(C1, P3, JFK)
Fly(P2, SFO, ATL)
Fly(P1, SFO, JFK)
Fly(P2, ATL, JFK)
Fly(P3, JFK, ATL)
Fly(P1, JFK, ATL)
Fly(P3, ATL, SFO)
Fly(P1, ATL, SFO)
Load(C3, P2, JFK)
Fly(P3, SFO, ATL)
Fly(P2, JFK, ATL)
Fly(P1, SFO, ATL)
Fly(P2, ATL, SFO)
Fly(P3, ATL, SFO)
Fly(P1, ATL, JFK)
Fly(P3, SFO, JFK)
Unload(C3, P2, SFO)


Solving Air Cargo Problem 2 using uniform_cost_search...

# Actions   Expansions   Goal Tests   New Nodes
    72         5154        5156       46618   

Plan length: 9  Time elapsed in seconds: 2.2535902899689972
Load(C3, P3, ATL)
Fly(P3, ATL, SFO)
Load(C1, P3, SFO)
Load(C2, P2, JFK)
Fly(P2, JFK, SFO)
Unload(C3, P3, SFO)
Fly(P3, SFO, JFK)
Unload(C2, P2, SFO)
Unload(C1, P3, JFK)


Solving Air Cargo Problem 2 using greedy_best_first_graph_search with h_unmet_goals...

# Actions   Expansions   Goal Tests   New Nodes
    72          17          19         170    

Plan length: 9  Time elapsed in seconds: 0.015337149030528963
Load(C1, P1, SFO)
Load(C2, P2, JFK)
Load(C3, P3, ATL)
Fly(P2, JFK, SFO)
Unload(C2, P2, SFO)
Fly(P3, ATL, SFO)
Unload(C3, P3, SFO)
Fly(P1, SFO, JFK)
Unload(C1, P1, JFK)


Solving Air Cargo Problem 2 using greedy_best_first_graph_search with h_pg_levelsum...

# Actions   Expansions   Goal Tests   New Nodes
    72          9           11          86    

Plan length: 9  Time elapsed in seconds: 6.467117811029311
Load(C1, P1, SFO)
Fly(P1, SFO, JFK)
Unload(C1, P1, JFK)
Load(C2, P2, JFK)
Fly(P2, JFK, SFO)
Unload(C2, P2, SFO)
Load(C3, P3, ATL)
Fly(P3, ATL, SFO)
Unload(C3, P3, SFO)


Solving Air Cargo Problem 2 using greedy_best_first_graph_search with h_pg_maxlevel...

# Actions   Expansions   Goal Tests   New Nodes
    72          27          29         249    

Plan length: 9  Time elapsed in seconds: 12.11261985602323
Load(C1, P1, SFO)
Load(C2, P2, JFK)
Load(C3, P3, ATL)
Fly(P2, JFK, SFO)
Fly(P3, ATL, SFO)
Fly(P1, SFO, JFK)
Unload(C3, P3, SFO)
Unload(C2, P2, SFO)
Unload(C1, P1, JFK)
