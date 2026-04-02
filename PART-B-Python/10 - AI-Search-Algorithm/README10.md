# 🧠 AI Search Algorithm – Maze Navigation

## 📌 Problem Statement

Design a maze navigation system that finds the optimal path from a start point to a goal using AI search algorithms.

---

## 🚀 Features

* Solve maze using:

  * 🔹 Breadth First Search (BFS)
  * 🔹 A* Search Algorithm
* Supports **dynamic maze modification**
* Displays path visually using `*`
* Handles walls (`#`) and free paths (`.`)

---

## 🧠 Algorithms Used

### 🔹 BFS (Breadth First Search)

* Explores level-by-level
* Guarantees shortest path in unweighted grid

### 🔹 A* Search

* Uses heuristic (Manhattan Distance)
* Faster than BFS for large grids
* Finds optimal path efficiently

---

## 🧩 Maze Representation

| Symbol | Meaning    |
| ------ | ---------- |
| S      | Start      |
| G      | Goal       |
| #      | Wall       |
| .      | Free Path  |
| *      | Path Found |

---

## ▶️ How to Run

```bash
python ai_maze_solver.py
```

---

## 📝 Sample Input

```
Enter rows: 5
Enter cols: 5

Row 0: S....
Row 1: .##..
Row 2: ..#..
Row 3: .##..
Row 4: ....G
```

---

## 📈 Complexity

* BFS → O(V + E)
* A* → O(E log V)

---

## 🎯 Applications

* Robotics path planning
* Game AI
* Navigation systems
* Shortest path problems

---

## 👨‍💻 Author

Aditya Kulkarni
Second Year IT Engineering Student

---

⭐ This project demonstrates practical implementation of AI search techniques.
