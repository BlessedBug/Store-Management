# InventoryCLI Manager

**InventoryCLI Manager** is a secure, command-line based inventory management system built in Python. It is designed for store owners and administrators who prefer lightweight terminal tools for daily inventory operations.

## Features

- 🔐 **Admin CURD Operations**
  - Add, update, delete, and view products (admin only)
  - Secure access with credentials
- 👤 **Customer Interface**
  - View available products with prices
  - Purchase products with quantity selection
  - Apply coupon codes for discounts
- 📦 **Stock Persistence**
  - Products stored in a local `stock.json` file
  - Admin actions logged to `timestamps.txt`
- 📊 **Logging**
  - Timestamps for all create, update, and delete operations

## Admin Credentials

Username: BlessedBug
Password: #Blessed404


| File             | Purpose                            |
| ---------------- | ---------------------------------- |
| `main.py`        | Main application script            |
| `stock.json`     | Stores product information         |
| `timestamps.txt` | Logs admin actions with timestamps |
| `.gitignore`     | Ignores unnecessary files for Git  |
| `README.md`      | Project documentation              |

