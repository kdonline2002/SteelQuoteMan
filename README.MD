# STEEL QUOTE MANAGEMENT SYSTEM

A responsive steel quotation management system designed for a steel fabrication and engineering business using <span style="color: blue;">ASP.NET Core MVC (.NET 8), Entity Framework Core, SQL Server, ViewModels, and a service-layer architecture.</span>

The application can be accessed from any device with a modern web browser and provides quote, quote line, and manufacturing process management, automated pricing calculations, soft deletes, lookup-based statuses, reporting, quote previews, validation, and a mobile-friendly user interface.

---

## FEATURES

## Quote Management

-	Create, edit and delete customer quotations
-	Automatically generate internal quote numbers
-	Quote status management
-	Quote preview for customer presentation


---

## Quote Lines

Add multiple line items to a quotation:
-   Item description
-   Quantity
-   Material grade
-   Dimensions
-   Mass
-   Unit pricing

---

## Manufacturing Processes

Each quote line can contain multiple manufacturing processes such as:
-	Laser Cutting
-	Plasma Cutting
-	Drilling
-	Bending
-	Rolling
-	Welding
    -   Process costs are automatically included in the line total.


---

## Automatic Calculations

The application automatically calculates:

-   Mass Each (Kg)
    -   Based on Volume(Length * Width * Thickness) and steel density.
-   Price Each
    -   Based on Mass Each (Kg), Price per Kg, and Processing cost.
-	Processing Cost
    -   Sum of processing cost.
-	Line Price Total
-	Quote Total


---

## Reporting

-	Quote Register with filters
-	Quote Preview


---

<!-- ## Screenshots
### Quote Maintenance
<img src="docs/screenshots/QuoteMaintenance.png" alt="QuoteMaintenance" style="border: 1px solid black;">
### Quote Details
<img src="docs/screenshots/QuoteDetails.png" alt="QuoteDetails" style="border: 1px solid black;">
### Quote Preview
<img src="docs/screenshots/QuotePreview.png" alt="QuotePreview" style="border: 1px solid black;">
### Create Quote
<img src="docs/screenshots/CreateQuote.png" alt="CreateQuote" style="border: 1px solid black;">
### Add Quote Line
<img src="docs/screenshots/AddQuoteLine.png" alt="AddQuoteLine" style="border: 1px solid black;">
### Add Process
<img src="docs/screenshots/AddProcess.png" alt="AddProcess" style="border: 1px solid black;">
### Quote Register
<img src="docs/screenshots/QuoteRegister.png" alt="QuoteRegister" style="border: 1px solid black;"> -->

## Screenshots

### Quote Maintenance (Desktop/Tablet)
<img src="docs/screenshots/QuoteMaintenance02.png" alt="QuoteMaintenance" style="border: 1px solid black;">

### Quote Maintenance (Mobile)
<img src="docs/screenshots/QuoteMaintenance02M.png" alt="QuoteMaintenance" style="border: 1px solid black;">

---

### Quote Details (Desktop/Tablet)
<img src="docs/screenshots/QuoteDetails02.png" alt="QuoteDetails" style="border: 1px solid black;">

### Quote Details (Mobile)
<img src="docs/screenshots/QuoteDetails02M.png" alt="QuoteDetails" style="border: 1px solid black;">

---

### Quote Preview (Desktop/Tablet)
<img src="docs/screenshots/QuotePreview02.png" alt="QuotePreview" style="border: 1px solid black;">

### Quote Preview (Mobile)
<img src="docs/screenshots/QuotePreview02m.png" alt="QuotePreview" style="border: 1px solid black;">

---

### Create Quote (Desktop/Tablet)
<img src="docs/screenshots/CreateQuote.png" alt="CreateQuote" style="border: 1px solid black;">

---

### Add/Edit Quote Line (Desktop/Tablet)
<img src="docs/screenshots/AddEditQuoteLine02.png" alt="AddEditQuoteLine" style="border: 1px solid black;">

---

### Add/Edit Process (Desktop/Tablet)
<img src="docs/screenshots/AddEditProcess01.png" alt="AddEditProcess" style="border: 1px solid black;">

---

### Quote Register (Desktop/Tablet)
<img src="docs/screenshots/QuoteRegister02.png" alt="QuoteRegister" style="border: 1px solid black;">

### Quote Register (Mobile)
<img src="docs/screenshots/QuoteRegister02M.png" alt="QuoteRegister" style="border: 1px solid black;">

<!-- ## Screenshots
### Quote Maintenance
![QuoteMaintenance](docs/screenshots/QuoteMaintenance.png)
### Quote Details
![QuoteDetails](docs/screenshots/QuoteDetails.png)
### Quote Preview
![QuotePreview](docs/screenshots/QuotePreview.png)
### Create Quote
![CreateQuote](docs/screenshots/CreateQuote.png)
### Add Quote Line
![AddQuoteLine](docs/screenshots/AddQuoteLine.png)
### Add Process
![AddProcess](docs/screenshots/AddProcess.png)
### Quote Register
![QuoteRegister](docs/screenshots/QuoteRegister.png) -->

---

## Future Enhancements
Planned functionality includes:
-	Product Catalogue
-	Material Pricing
-	PDF Quote Generation
-	Email PDF Quotes
-	Quote Revision History
-	Sales Order Conversion
-	Inventory Integration
-	Dashboard & KPI Reporting

---

## Technologies

-	ASP.NET Core MVC (.NET 8)
-	Entity Framework Core
-	SQL Server
-	Bootstrap 5
-	LINQ
-	Dependency Injection
-	Razor Views

### Link
[Architecture Documentation](docs/architecture.md)

## License

MIT License
