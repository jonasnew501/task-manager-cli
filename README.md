# Task Manager CLI — SOLID Practice Project

## About this project
The purpose of this project is to practice **writing maintainable, extendable software** in Python by applying two SOLID principles:

- **Single Responsibility Principle (SRP)** — each component has one clear reason to change  
- **Open–Closed Principle (OCP)** — easily extend the program without modifying existing code

This project implements a **command-line Task Manager application**.  
Users can add, list, filter, and modify tasks through CLI commands.

Additionally, this project reinforces:

- Clean folder and module structure  
- Separation of concerns between **CLI / core logic / data layer**  
- Packaging Python applications  
- Writing basic tests for core functionality  

A key goal is to build **architecture thinking** — not just code that works, but code that scales in clarity and maintainability.

> Future versions may extend this to other SOLID principles, but the current iteration focuses **deliberately** on SRP + OCP.


## Features

- Adding tasks (with category & completion flag)  
- Listing tasks  
- Filtering tasks (e.g., by category, by completion state)  
- Marking tasks as complete  
- Saveing & loading tasks from disk  
- Modular design for future extensions (e.g., JSON storage, due-dates, priorities)

## Structure of this project
### Folder-structure
The folderstructure of this project follows a **src-based structure/-layout**.  
A clear separation is done between
 - Core logic (not tied to the interface)
 - CLI interface
 - Tests

 The general structure looks like this:
```plaintext
project-root/
├── src/
│   └── package-name/
│       ├── core/                      # contains domain logic (models + business rules)
│       │   ├── task.py                # Task model
│       │   ├── taskRepository.py      # TaskRepository (SRP)
│       │   └── taskManager.py         # Core logic / coordination layer
│       │   └── filters.py
│       ├── cli/                       # handles parsing input & printing output
│       │   ├── main.py                # CLI entry point, argument parsing

├── tests/                             # contains Unittests
│       ├── core/
│       │   ├── test_task.py
│       │   ├── test_taskRepository.py
│       │   └── test_taskManager.py
│       │   └── test_filters.py

├── dist/
│   └── task_manager_cli.exe           # Built executable output
├── pyproject.toml
└── README.md
└── requirements.txt
└── .gitignore
```

## Tech stack
**Language**  
![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)  

**Programming Paradigm**  
![OOP](https://img.shields.io/badge/OOP-Object%20Oriented%20Programming-4CAF50)  
![SOLID](https://img.shields.io/badge/Architecture-SOLID%20Principles-2E86C1)   

**Tools & Workflow**  
![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?logo=git&logoColor=white)  
![GitHub](https://img.shields.io/badge/GitHub-Repos-181717?logo=github&logoColor=white)  
![CLI](https://img.shields.io/badge/UI-Command%20Line-000000?logo=windows-terminal&logoColor=white)  

**Testing & CI**  
![PyTest](https://img.shields.io/badge/Testing-PyTest-46375B?logo=pytest&logoColor=white)  
![Pytest-Mock](https://img.shields.io/badge/Testing-Pytest--Mock-6A5ACD?logo=pytest&logoColor=white)  

**Packaging & Deployment**  
![PyInstaller](https://img.shields.io/badge/Build%20Tool-PyInstaller-3776AB?logo=python&logoColor=white)  

**Code Formatting**  
![Black](https://img.shields.io/badge/Auto%20Formatting-Black-000000?logo=python&logoColor=white)

**Other Topics Studied**  
![Clean Code](https://img.shields.io/badge/Reading-Clean%20Code-000000)  


## Learning Goals

### ✅ Single Responsibility Principle (SRP)

- Each class has **one purpose**
- Repository only stores tasks, **not** business logic  
- Service coordinates operations & validation  
- CLI only handles user interaction  

### ✅ Open–Closed Principle (OCP)

- System is **open for extension**  
- But **closed for modification** of core code  
- New filters, storage backends, or output formats can be added without editing existing logic

### ✅ Separation of Concerns (SoC)

- CLI ≠ business logic ≠ persistence logic  

### 🧠 Architectural Thinking

- Think in layers
- Design for growth and clarity
- Treat small programs like real software systems


## What I Learned

> This list will be updated while the project evolves

- SRP forces clearer code boundaries  
- OCP makes it easier to add features without breaking existing ones  
- Separating CLI from logic makes testing cleaner  
- Good architecture reduces complexity *before* it appears  


## Future Enhancements

- Add additional SOLID principles (LSP, ISP, DIP)  
- JSON or SQLite storage backend  
- Releaseing as executable (`.exe`) via PyInstaller  


## Running the Program

> Instructions will be added once the CLI is implemented