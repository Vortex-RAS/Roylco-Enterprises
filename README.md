## R1 - Basic Templates

- **Homepage**: A basic template for the homepage.
- **Add Customer**: A template for adding new customers.
- **Order Entry**: A template for entering new orders.

## R2 - Customization and Refactoring

- **Custom Home.html**: A customized version of the homepage template.
- **Base.html**: Added a base template for consistent styling and layout across the application.
- **Template Splitting**: Refactored the templates to use the base template for better maintainability and structure.

## R3 - Models and Product/Customer Features

- **Updated Models**: Enhanced `models.py` to include the latest fields and relationships for the `Product` and `Customer` models.
- **Product Management**: Implemented features for listing products, viewing product details in a modal, and adding new products.
- **Customer Management**: Updated customer details management, including the addition of a customer edit view and the integration of modals for viewing and editing customer information.


## R4 - Order Management and PDF Generation

- **Order Management**: Developed functionalities for managing orders, including viewing order details and tracking ongoing orders.
- **Order PDF Generation**: Implemented a feature to generate and download a PDF preview of an order. This includes:
- A view (`order_preview_pdf`) that retrieves order details and related products.
- An HTML template (`order_preview_pdf.html`) with a styled layout for the PDF.
- Deployed in Vercel.
=======

