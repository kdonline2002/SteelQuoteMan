# Architecture Overview

## Application Flow

```text
Controllers
        │
        ▼
Service Layer
        │
        ▼
Entity Framework Core
        │
        ▼
SQL Server

```

---

## Architecture

Presentation Layer:
-    MVC Controllers
-    Razor Views
-    ViewModels

Business Layer:
-    Services
-    Business Rules
-    Calculations

Data Layer:
-    EF Core
-    SQL Server



### Design Decisions

Why ViewModels?

To prevent exposing EF entities to the presentation layer.

-----------------------------------------

Why Service Layer?

Centralises business rules and calculations.

-----------------------------------------

Why Soft Deletes?

Preserves historical quote data.

-----------------------------------------

Why Lookup Tables?

Allows administrators to maintain business values without code changes.

-----------------------------------------

Why Bootstrap?

Rapid, responsive UI development.
