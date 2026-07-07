"""
====================================================
MAZE SEARCH FINAL
PART 1
Generator Labirin + Helper Function
====================================================
"""

import random
import time
import csv
import tracemalloc
from collections import deque

# ==================================================
# KONFIGURASI TAMPILAN
# ==================================================

WALL = "█"
PATH = "·"
START = "S"
GOAL = "E"
ROUTE = "★"

# ==================================================
# MAZE GENERATOR
# ==================================================

class MazeGenerator:

    def __init__(self, rows, cols, seed=None):

        if seed is not None:
            random.seed(seed)

        self.node_rows = rows
        self.node_cols = cols

        self.rows = rows * 2 - 1
        self.cols = cols * 2 - 1

        self.maze = [
            [1 for _ in range(self.cols)]
            for _ in range(self.rows)
        ]

    def _cell(self, node):
        return (node[0] * 2, node[1] * 2)

    def _neighbors(self, node, visited):

        r, c = node

        candidates = [
            (r - 1, c),
            (r + 1, c),
            (r, c - 1),
            (r, c + 1)
        ]

        valid = []

        for nr, nc in candidates:

            if 0 <= nr < self.node_rows and 0 <= nc < self.node_cols:

                if (nr, nc) not in visited:
                    valid.append((nr, nc))

        random.shuffle(valid)

        return valid

    def generate(self):

        visited = set()

        stack = [(0, 0)]

        visited.add((0, 0))

        r, c = self._cell((0, 0))
        self.maze[r][c] = 0

        while stack:

            current = stack[-1]

            nxt = self._neighbors(current, visited)

            if not nxt:
                stack.pop()
                continue

            nxt = nxt[0]

            visited.add(nxt)

            r1, c1 = self._cell(current)
            r2, c2 = self._cell(nxt)

            self.maze[(r1 + r2) // 2][(c1 + c2) // 2] = 0
            self.maze[r2][c2] = 0

            stack.append(nxt)

        start = (0, 0)
        goal = (self.rows - 1, self.cols - 1)

        return self.maze, start, goal


# ==================================================
# CETAK LABIRIN
# ==================================================

def print_maze(maze, start, goal, route=None):

    route = set(route or [])

    print()

    for r, row in enumerate(maze):

        line = []

        for c, value in enumerate(row):

            pos = (r, c)

            if pos == start:
                line.append(START)

            elif pos == goal:
                line.append(GOAL)

            elif pos in route:
                line.append(ROUTE)

            elif value == 1:
                line.append(WALL)

            else:
                line.append(PATH)

        print(" ".join(line))

    print()


# ==================================================
# HELPER FUNCTION
# ==================================================

def is_valid(maze, r, c):

    return (
        0 <= r < len(maze)
        and
        0 <= c < len(maze[0])
        and
        maze[r][c] == 0
    )


def get_neighbors(maze, pos):

    r, c = pos

    directions = [

        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)

    ]

    neighbors = []

    for dr, dc in directions:

        nr = r + dr
        nc = c + dc

        if is_valid(maze, nr, nc):
            neighbors.append((nr, nc))

    return neighbors


def reconstruct_path(parent, start, goal):

    if goal not in parent and goal != start:
        return []

    current = goal

    path = [current]

    while current != start:

        current = parent[current]

        path.append(current)

    path.reverse()

    return path


def overlay_route(maze, path):

    return set(path)


def print_statistics(name, result):

    print()

    print("=" * 40)
    print(name)
    print("=" * 40)

    print("Status              :", "Berhasil" if result["found"] else "Gagal")
    print("Panjang Jalur       :", len(result["path"]))
    print("Node Dieksplorasi   :", result["explored"])
    print("Waktu               : %.6f detik" % result["time"])
    print("Memori              : %.2f KB" % result["memory"])

    print("=" * 40)

"""
====================================================
PART 2
ALGORITMA BFS DAN DFS
====================================================
"""

# ==================================================
# BREADTH FIRST SEARCH (BFS)
# ==================================================

def bfs(maze, start, goal):

    tracemalloc.start()

    t0 = time.perf_counter()

    queue = deque([start])

    visited = {start}

    parent = {}

    explored = 0

    while queue:

        current = queue.popleft()

        explored += 1

        if current == goal:
            break

        for neighbor in get_neighbors(maze, current):

            if neighbor not in visited:

                visited.add(neighbor)

                parent[neighbor] = current

                queue.append(neighbor)

    if goal in visited:
        path = reconstruct_path(parent, start, goal)
    else:
        path = []

    current_memory, peak_memory = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return {

        "found": goal in visited,

        "path": path,

        "explored": explored,

        "time": time.perf_counter() - t0,

        "memory": peak_memory / 1024

    }


# ==================================================
# DEPTH FIRST SEARCH (DFS)
# ==================================================

def dfs(maze, start, goal):

    tracemalloc.start()

    t0 = time.perf_counter()

    stack = [start]

    visited = {start}

    parent = {}

    explored = 0

    while stack:

        current = stack.pop()

        explored += 1

        if current == goal:
            break

        neighbors = get_neighbors(maze, current)

        neighbors.reverse()

        for neighbor in neighbors:

            if neighbor not in visited:

                visited.add(neighbor)

                parent[neighbor] = current

                stack.append(neighbor)

    if goal in visited:
        path = reconstruct_path(parent, start, goal)
    else:
        path = []

    current_memory, peak_memory = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return {

        "found": goal in visited,

        "path": path,

        "explored": explored,

        "time": time.perf_counter() - t0,

        "memory": peak_memory / 1024

    }


# ==================================================
# PERBANDINGAN BFS DAN DFS
# ==================================================

def compare(maze, start, goal):

    bfs_result = bfs(maze, start, goal)

    dfs_result = dfs(maze, start, goal)

    print("\n========== HASIL PERBANDINGAN ==========\n")

    print("{:<22}{:>12}{:>12}".format(
        "Parameter",
        "BFS",
        "DFS"
    ))

    print("-" * 48)

    print("{:<22}{:>12}{:>12}".format(
        "Status",
        str(bfs_result["found"]),
        str(dfs_result["found"])
    ))

    print("{:<22}{:>12}{:>12}".format(
        "Panjang Jalur",
        len(bfs_result["path"]),
        len(dfs_result["path"])
    ))

    print("{:<22}{:>12}{:>12}".format(
        "Node Eksplorasi",
        bfs_result["explored"],
        dfs_result["explored"]
    ))

    print("{:<22}{:>12.6f}{:>12.6f}".format(
        "Waktu (detik)",
        bfs_result["time"],
        dfs_result["time"]
    ))

    print("{:<22}{:>12.2f}{:>12.2f}".format(
        "Memori (KB)",
        bfs_result["memory"],
        dfs_result["memory"]
    ))

    return bfs_result, dfs_result


# ==================================================
# BENCHMARK
# ==================================================

def benchmark(generator, configs, outfile="benchmark.csv"):

    with open(outfile, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Rows",
            "Cols",
            "Algoritma",
            "Status",
            "PanjangPath",
            "NodeEksplorasi",
            "Waktu",
            "Memori"
        ])

        for rows, cols in configs:

            maze, start, goal = generator(rows, cols)

            for nama, algoritma in [

                ("BFS", bfs),

                ("DFS", dfs)

            ]:

                hasil = algoritma(maze, start, goal)

                writer.writerow([

                    rows,

                    cols,

                    nama,

                    hasil["found"],

                    len(hasil["path"]),

                    hasil["explored"],

                    hasil["time"],

                    hasil["memory"]

                ])

                print(f"{nama} {rows}x{cols} selesai.")

    print("\nBenchmark selesai.")

    print("File tersimpan :", outfile)
    """
====================================================
PART 3
MENU UTAMA
====================================================
"""

maze = None
start = None
goal = None


# ==================================================
# GENERATE MAZE
# ==================================================

def generate_maze():

    global maze
    global start
    global goal

    print("\n=== GENERATE LABIRIN ===")

    rows = int(input("Jumlah node baris : "))
    cols = int(input("Jumlah node kolom : "))

    generator = MazeGenerator(rows, cols)

    maze, start, goal = generator.generate()

    print("\nLabirin berhasil dibuat!\n")

    print_maze(maze, start, goal)


# ==================================================
# PENCARIAN JALUR
# ==================================================

def search_maze():

    global maze
    global start
    global goal

    if maze is None:

        print("\nGenerate labirin terlebih dahulu!")

        return

    print("\n=== PILIH ALGORITMA ===")
    print("1. Breadth First Search (BFS)")
    print("2. Depth First Search (DFS)")

    pilihan = input("Pilihan : ")

    if pilihan == "1":

        hasil = bfs(maze, start, goal)

        print("\n=== HASIL BFS ===\n")

        print_maze(
            maze,
            start,
            goal,
            hasil["path"]
        )

        print_statistics("Breadth First Search", hasil)

    elif pilihan == "2":

        hasil = dfs(maze, start, goal)

        print("\n=== HASIL DFS ===\n")

        print_maze(
            maze,
            start,
            goal,
            hasil["path"]
        )

        print_statistics("Depth First Search", hasil)

    else:

        print("Pilihan tidak tersedia.")


# ==================================================
# PERBANDINGAN
# ==================================================

def compare_algorithm():

    global maze
    global start
    global goal

    if maze is None:

        print("\nGenerate labirin terlebih dahulu!")

        return

    compare(maze, start, goal)


# ==================================================
# BENCHMARK
# ==================================================

def run_benchmark():

    configs = [

        (5, 5),

        (8, 8),

        (10, 10),

        (15, 15),

        (20, 20)

    ]

    benchmark(

        lambda r, c: MazeGenerator(r, c).generate(),

        configs,

        "benchmark.csv"

    )


# ==================================================
# MENU
# ==================================================

def menu():

    while True:

        print("\n")
        print("=" * 45)
        print("      SISTEM PENCARIAN JALUR LABIRIN")
        print("=" * 45)

        print("1. Generate Labirin")
        print("2. Cari Jalur")
        print("3. Bandingkan BFS vs DFS")
        print("4. Benchmark")
        print("0. Keluar")

        pilih = input("\nMasukkan pilihan : ")

        if pilih == "1":

            generate_maze()

        elif pilih == "2":

            search_maze()

        elif pilih == "3":

            compare_algorithm()

        elif pilih == "4":

            run_benchmark()

        elif pilih == "0":

            print("\nTerima kasih telah menggunakan program ini.")

            break

        else:

            print("\nPilihan tidak valid.")


# ==================================================
# MAIN PROGRAM
# ==================================================

if __name__ == "__main__":

    menu()