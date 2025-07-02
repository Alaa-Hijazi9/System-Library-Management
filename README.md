# Library Management System

## Project Overview

This is a simple **Library Management System** implemented in Python using Object-Oriented Programming (OOP) principles.  
The system allows managing library items (Books, DVDs, Magazines) and users, supporting operations like borrowing, reserving, and returning items.

## Features

- Add and manage multiple types of library items.
- User registration and management.
- Borrow and reserve items with proper availability checks.
- Persistent storage of data using JSON files.
- Custom exceptions for clear error handling.

## How to Run

### Prerequisites

- Python 3.8 or higher installed on your machine.
- No external packages required (uses Python’s built-in `json` module).

### Steps

1. Download and unzip the project files into a folder.

2. Open a terminal (Command Prompt) and navigate to the project directory

3. Run the main script:

```bash
   python main.py
```
4. Interact with the Program
Follow on-screen prompts to enter user ID, item ID, or other commands as requested.


## Notes
Make sure the data files (items.json and users.json) are present in the project folder or the specified path in the code.

You can edit these JSON files to add or modify users and items.

If any errors occur, verify your Python installation and the presence of all project files.

# Design Decisions

## Overview
The system is designed using Object-Oriented Programming (OOP) principles to ensure modularity, ease of maintenance, and scalability.

## Core Components
- Library: Manages collections of users and items and handles operations such as borrowing, reserving, and returning.

- LibraryItem (Abstract Class): Defines common properties and methods for all library items.

- Book, DVD, Magazine: Subclasses that inherit from LibraryItem representing specific item types.

- User: Stores user information and tracks borrowed and reserved items.

- Reservable (Abstract Interface): Defines the contract for reservable items.

## Key Decisions
Abstraction: Abstract base classes enforce implementation of core methods like display_info() across all item types.

Separation of Concerns: Each class has a single responsibility, improving code clarity and maintainability.

Custom Exceptions: Defined specific exceptions like ItemNotFoundError and UserNotFoundError for precise error handling.

Data Storage: Used JSON files for simplicity and easy modification of data.

ID-based Linking: Users and items are linked via unique IDs, facilitating efficient lookups.

Extensibility: The design allows easy addition of new item types with minimal changes to existing code.

## Challenges and Solutions
Handling user-item relationships by maintaining borrowed_items lists within users.

Resolving import issues by structuring the project as a package or adjusting import paths.

## Code Documentation
The codebase contains detailed comments explaining the purpose of classes, methods, and critical logic.

Naming conventions follow Python standards for clarity and readability.

## Project Structure
LibraryManagement/
│
├── main.py
├── models/
│   ├── Library.py
│   ├── LibraryItem.py
│   ├── Book.py
│   ├── DVD.py
│   ├── Magazine.py
│   ├── User.py
│   └── Reservable.py
|
|── items.json
|── users.json
├── exceptions.py
└── README.md

