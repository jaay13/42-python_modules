# Python_Modules (WIP)

A progression of Python exercises, one theme per module, going from
basic syntax to decorators and functional tools. Each module lives in
its own directory; most exercises are individually runnable scripts
with their own docstrings and inline comments explaining the "why",
not just the "what".

## Table of Contents

- [Module 00 - Basics](#module-00---basics)
- [Module 01 - Object-Oriented Basics](#module-01---object-oriented-basics)
- [Module 02 - Exceptions](#module-02---exceptions)
- [Module 03 - CLI Args, Generators & Comprehensions](#module-03---cli-args-generators--comprehensions)
- [Module 04 - File I/O & Streams](#module-04---file-io--streams)
- [Module 05 - Polymorphism, ABCs & Protocols](#module-05---polymorphism-abcs--protocols)
- [Module 06 - Modules & Packages](#module-06---modules--packages)
- [Module 07 - Design Patterns (Factory, Mixins, Strategy)](#module-07---design-patterns-factory-mixins-strategy)
- [Module 08 - Environments & Dependency Management](#module-08---environments--dependency-management)
- [Module 09 - Data Validation with Pydantic](#module-09---data-validation-with-pydantic)
- [Module 10 - Functional Python](#module-10---functional-python)

## Module 00 - Basics

Garden-themed intro exercises covering `print`, `input`, arithmetic,
conditionals, loops vs. recursion, and function arguments.

| Exercise | File | Topic |
|---|---|---|
| ex0 | `ft_hello_garden.py` | `print` |
| ex1 | `ft_garden_name.py` | `input` + f-strings |
| ex2 | `ft_plot_area.py` | Arithmetic on user input |
| ex3 | `ft_harvest_total.py` | Summing multiple inputs |
| ex4 | `ft_plant_age.py` | `if` / `else` branching |
| ex5 | `ft_water_reminder.py` | Conditional logic |
| ex6 | `ft_count_harvest_iterative.py` / `ft_count_harvest_recursive.py` | Iteration vs. recursion |
| ex7 | `ft_seed_inventory.py` | Function parameters + `elif` chains |

## Module 01 - Object-Oriented Basics

Building up a `Plant` class step by step: attributes, methods,
encapsulation with private fields and getters/setters, inheritance
(`Flower`, `Tree`, `Vegetable`), and finally static/class methods with
a nested `Stats` class for analytics.

| Exercise | File | Topic |
|---|---|---|
| ex0 | `ft_garden_intro.py` | Plain variables and formatted output |
| ex1 | `ft_garden_data.py` | First class (`Plant`) |
| ex2 | `ft_plant_growth.py` | Methods that mutate state |
| ex3 | `ft_plant_factory.py` | Multiple instances / object creation |
| ex4 | `ft_garden_security.py` | Encapsulation (private attributes) |
| ex5 | `ft_plant_types.py` | Inheritance (`Flower`, `Tree`, `Vegetable`) |
| ex6 | `ft_garden_analytics.py` | Nested classes, `@staticmethod`, `@classmethod` |

## Module 02 - Exceptions

`try`/`except`/`finally`, raising built-in errors, and building a
custom exception hierarchy (`GardenError` → `PlantError` / `WaterError`).

| Exercise | File | Topic |
|---|---|---|
| ex0 | `ft_first_exception.py` | Catching `ValueError` |
| ex1 | `ft_raise_exception.py` | Raising exceptions manually |
| ex2 | `ft_different_errors.py` | Handling several error types |
| ex3 | `ft_custom_errors.py` | Custom exception classes |
| ex4 | `ft_finally_block.py` | `finally` for guaranteed cleanup |

## Module 03 - CLI Args, Generators & Comprehensions

Reading `sys.argv`, validating/parsing user input in a loop, random
data generation, lazy evaluation with generators, and list/dict/set
comprehensions.

| Exercise | File | Topic |
|---|---|---|
| ex0 | `ft_command_quest.py` | `sys.argv` basics |
| ex1 | `ft_score_analytics.py` | Parsing and filtering CLI args |
| ex2 | `ft_coordinate_system.py` | Validated input loop, `tuple` return |
| ex3 | `ft_achievement_tracker.py` | `random`, `set` |
| ex4 | `ft_inventory_system.py` | Parsing `key:value` args into a `dict` |
| ex5 | `ft_data_stream.py` | Generators (`yield`) |
| ex6 | `ft_data_alchemist.py` | List/dict comprehensions |

## Module 04 - File I/O & Streams

Opening, reading and writing files safely, `stdin`/`stdout`/`stderr`,
and using `with` for automatic resource cleanup.

| Exercise | File | Topic |
|---|---|---|
| ex0 | `ft_ancient_text.py` | Opening and reading a file, error handling |
| ex1 | `ft_archive_creation.py` | Creating/writing files |
| ex2 | `ft_stream_management.py` | `stdin` / `stdout` / `stderr` |
| ex3 | `ft_vault_security.py` | Context managers (`with`) for read/write |

## Module 05 - Polymorphism, ABCs & Protocols

The "Code Nexus" series: an abstract `DataProcessor` interface with
`NumericProcessor` / `TextProcessor` / `LogProcessor` implementations,
then a `DataStream` router that dispatches to whichever processor
accepts a given element without ever checking its concrete type, and
finally exporting through duck-typed `Protocol` plugins instead of
inheritance.

| Exercise | File | Topic |
|---|---|---|
| ex0 | `data_processor.py` | Abstract Base Classes (`ABC`), polymorphism |
| ex1 | `data_stream.py` | Routing to processors via a shared interface |
| ex2 | `data_pipeline.py` | Duck typing with `typing.Protocol` |

## Module 06 - Modules & Packages

An alchemy-themed tour of Python's import system: importing from a
single sibling module, from a package (`alchemy/`), from nested
subpackages (`alchemy/grimoire/`, `alchemy/transmutation/`), what
`__init__.py` exposes at each level, and what happens when an import
is broken (`ft_kaboom_*`).

| File | Topic |
|---|---|
| `ft_alembic_0.py` / `ft_alembic_1.py` | `import x` vs `from x import y` (sibling module) |
| `ft_alembic_2.py` … `ft_alembic_5.py` | Same, but reaching into the `alchemy` package at increasing levels of abstraction |
| `ft_distillation_0.py` / `ft_distillation_1.py` | Accessing `alchemy/potions.py` directly vs. via the package |
| `ft_kaboom_0.py` / `ft_kaboom_1.py` | A working nested import vs. one that raises on import |
| `ft_transmutation_0.py` … `ft_transmutation_2.py` | Importing from a sub-subpackage (`alchemy/transmutation/`) at increasing levels of abstraction |
| `alchemy/` | The package being imported from throughout this module |

## Module 07 - Design Patterns (Factory, Mixins, Strategy)

A `Creature` class hierarchy used to demonstrate three patterns:
abstract factories that build matched base/evolved families, mixins
that layer optional capabilities (healing, transforming) onto a
Creature independent of its class hierarchy, and a strategy pattern
that decouples battle behavior from Creature type. `battle.py`,
`capacitor.py` and `tournament.py` at the module root exercise each.

| Exercise | Topic |
|---|---|
| ex0 | Abstract Factory pattern (`factory.py`, `factories.py`, matched base/evolved `Creature` families) |
| ex1 | Capability mixins (`HealCapability`, `TransformCapability`) layered onto `Creature` |
| ex2 | Strategy pattern (`BattleStrategy` + `NormalStrategy`/`AggressiveStrategy`/`DefensiveStrategy`) decoupling behavior from type |

## Module 08 - Environments & Dependency Management

Working with virtual environments and dependency/configuration
tooling.

| Exercise | File | Topic |
|---|---|---|
| ex0 | `construct.py` | Detecting whether you're inside a virtual environment |
| ex1 | `loading.py` | Comparing `pip` vs. Poetry for dependency management |
| ex2 | `oracle.py` | Loading configuration from env vars and a `.env` file |

## Module 09 - Data Validation with Pydantic

Validating structured data with Pydantic models, from simple field
constraints to cross-field business rules and nested models.

| Exercise | File | Topic |
|---|---|---|
| ex0 | `space_station.py` | Basic Pydantic model validation |
| ex1 | `alien_contact.py` | Cross-field rules via `@model_validator` |
| ex2 | `space_crew.py` | Nested models (`SpaceMission` containing `CrewMember`s) |

## Module 10 - Functional Python

Lambdas, higher-order functions, closures, `functools`, and
decorators — building up to a `MageGuild` that casts validated,
timed, retryable spells.

| Exercise | File | Topic |
|---|---|---|
| ex0 | `lambda_spells.py` | `lambda` expressions |
| ex1 | `higher_magic.py` | Functions that take/return other functions |
| ex2 | `scope_mysteries.py` | Closures and `nonlocal` |
| ex3 | `functools_artifacts.py` | `functools` (`reduce`, `partial`, `lru_cache`, etc.) |
| ex4 | `decorator_mastery.py` | Decorators (`functools.wraps`, parameterized decorators) |
