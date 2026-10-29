# Кейс-задача № 4 — юнит-тесты (GoogleTest)

Классы `Queue`, `Heap`, `BinaryTree` (`queue.hpp`, `heap.hpp`, `binary_tree.hpp`) и юнит-тесты для их методов `push`/`pop` (и `search` для дерева) на фреймворке GoogleTest.

## Сборка и запуск

Требуется компилятор с поддержкой C++17 и установленный GoogleTest.

### CMake

```bash
cmake -S . -B build
cmake --build build
./build/run_tests
```

### Напрямую через g++ (Ubuntu/Debian, `apt install libgtest-dev`)

```bash
g++ -std=c++17 -O2 tests_queue.cpp tests_heap.cpp tests_binary_tree.cpp \
    -lgtest_main -lgtest -lpthread -o run_tests
./run_tests
```

## Состав

| Класс | Методы | Файл |
|---|---|---|
| `Queue` | `push`, `pop`, `front`, `empty`, `size` | `queue.hpp` |
| `Heap` (max-heap) | `push`, `pop`, `top`, `empty`, `size` | `heap.hpp` |
| `BinaryTree` (BST) | `push`, `pop`, `search`, `empty` | `binary_tree.hpp` |

19 тестов в 3 test suites: FIFO-порядок и исключения при пустой очереди — для `Queue`; порядок извлечения по убыванию и исключения при пустой куче — для `Heap`; поиск, вставка и удаление узла-листа/с одним потомком/с двумя потомками/корня — для `BinaryTree`.
