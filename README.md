# 🧬 Traveling Salesman Problem Using a Genetic Algorithm

This project solves the **Traveling Salesman Problem (TSP)** using a **Genetic Algorithm (GA)** approach in Python.  
It generates a set of random cities with coordinates and applies evolutionary principles — **selection, crossover, and mutation** — to find the shortest possible route that visits all cities and returns to the start.

---

## 🚀 Features

- Random generation of cities with 2D coordinates  
- Distance calculation between cities using Euclidean distance  
- Fitness evaluation based on total route distance  
- Genetic operations:
  - **Selection:** Top-performing routes are selected as parents  
  - **Crossover:** Combines parents to create offspring  
  - **Mutation:** Randomly swaps cities to maintain diversity  
- Returns the **best route** and its **total distance**

---

## 🧩 How It Works

1. A set of random cities is generated with `(x, y)` coordinates.  
2. An initial population of random routes (individuals) is created.  
3. The algorithm iterates through multiple **generations**, performing:
   - **Selection:** Keeps the top 20% shortest routes  
   - **Crossover:** Combines parents to produce new routes  
   - **Mutation:** Swaps two cities randomly in some offspring  
4. The best route and distance found so far are updated if a better one is discovered.

---

## 🧠 Genetic Algorithm Overview

| Concept | Description |
|----------|--------------|
| **Population** | A group of possible routes (solutions) |
| **Individual** | A single route (ordering of city visits) |
| **Fitness Function** | Negative total distance (shorter routes = higher fitness) |
| **Selection** | Best 20% of individuals survive to next generation |
| **Crossover** | Combines portions of two parent routes |
| **Mutation** | Randomly swaps cities to introduce variation |

---

