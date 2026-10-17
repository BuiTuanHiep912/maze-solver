# Maze Solver

## Mục tiêu

Hoàn thiện các hàm `solve_bfs()`, `solve_dfs()` và `solve_astar()` trong
`solver.py`. Mỗi hàm nhận vị trí `start`, `goal` và trả về một đường đi hợp lệ
dưới dạng danh sách tọa độ.

## Cấu trúc dữ liệu

### Mê cung

Mê cung được lưu trong dictionary:

```python
maze: dict[tuple[int, int], int]
```

- Key là tọa độ `(row, column)`, ví dụ `(1, 2)`.
- Value là trạng thái của ô:
  - `MazeGenerator.EMPTY` (`0`): có thể đi qua.
  - `MazeGenerator.WALL` (`1`): tường, không được đi qua.

Kích thước mê cung được lấy từ `self.height` và `self.width`.

### Vị trí và đường đi

Một vị trí có dạng:

```python
tuple[int, int]  # (row, column)
```

Đường đi có dạng:

```python
list[tuple[int, int]]
```

Ví dụ:

```python
[(1, 1), (1, 2), (2, 2)]
```

### Các cấu trúc hỗ trợ

- `get_neighbors(pos)`: trả về các ô trống kề với `pos` theo bốn hướng
  Bắc, Nam, Tây, Đông. Khi thêm hàng xóm, phải dùng
  `neighbors.append((nx, ny))`.
- `visited`: `set` lưu các ô đã duyệt, giúp tránh duyệt lặp.
- `came_from`: `dict` lưu ô trước đó của mỗi ô, dùng để dựng lại đường đi
  bằng `reconstruct_path()`.
- BFS dùng `queue` (`collections.deque`).
- DFS dùng `stack` (`list`).
- A* dùng `heapq`, cùng với `g_score` và khoảng cách Manhattan từ
  `heuristic()`.

## Yêu cầu triển khai

- Nếu `start` hoặc `goal` là tường/không tồn tại, trả về `[]`.
- Tái sử dụng `get_neighbors()`, `heuristic()` và `reconstruct_path()`.

## Kiểm tra

Sau khi hoàn thiện, bỏ `@unittest.skip` của các test tương ứng rồi chạy:

```powershell
python -m unittest -v
```
## References
[Must-read: Maze data structure](https://l.facebook.com/l.php?u=https%3A%2F%2Finventwithpython.com%2Frecursion%2Fchapter11.html%3Ffbclid%3DIwZXh0bgNhZW0CMTAAcGRvZgVicmlkETFrbU16akhhRVlQS1RJUjEyc3J0YwZhcHBfaWQQMjIyMDM5MTc4ODIwMDg5MgABHpHhc5lKgT_33UNkUeIQsuew9uXBSXhnFbJ-PADMJG0bIJ2trLEjCsCuv7Wb_aem_5iYhF09vq4SJc2Ij3icYrQ&h=AUDtJliyq3t0VevRarivAYTT5BZPEtlqe1Z-H4N4nEcd6cFCFor9UzNilkMkaFSnpYs9G4KKQlSFYvOCsuzTnqeAQ3CsYqkUnjBFX6ml9-SYpQnJS7h6WdMPapKQRJeThoj9EA)

[Wikipedia](https://l.facebook.com/l.php?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMaze_generation_algorithm%3Ffbclid%3DIwZXh0bgNhZW0CMTAAcGRvZgVicmlkETFrbU16akhhRVlQS1RJUjEyc3J0YwZhcHBfaWQQMjIyMDM5MTc4ODIwMDg5MgABHiiHh-XzgUsWkwJaAW3o7MxTtGKCy9hcMtmd1RJopyKl8lbrtOdC9EzHTNS2_aem__O29BXxQ1uL8GrjZgsw88A%23Recursive_backtracker&h=AUDtJliyq3t0VevRarivAYTT5BZPEtlqe1Z-H4N4nEcd6cFCFor9UzNilkMkaFSnpYs9G4KKQlSFYvOCsuzTnqeAQ3CsYqkUnjBFX6ml9-SYpQnJS7h6WdMPapKQRJeThoj9EA)

[LMS](https://lms.hust.edu.vn/pluginfile.php/87772/mod_resource/content/1/L4-Tim%20kiem%20voi%20tri%20thu%20bo%20sung.pdf)
