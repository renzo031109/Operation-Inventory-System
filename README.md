Clinic & Inventory Management System
Overview
This project is a Django-based Clinic & Inventory Management System designed to handle patient records, medicine tracking, and stock management for clinic supplies. It features a structured database with well-defined relationships between entities like patients, medicine, medical services, inventory, and clinic staff.

Key Features
✅ Administration Inventory Records Management – Inventory Management of Operation supplies and equipments
✅ Patient Records Management – Store and organize patient details, medical history, and treatment records. 
✅ Medicine Inventory System – Track medicines, manage stock levels, monitor consumption trends, and set alerts for critical stock levels. 
✅ Medical Services Given – Record treatments and services provided to patients. 
✅ Foreign Key Relationships – Ensures proper linkage between tables for structured data retrieval. 
✅ Raw SQL Handling – Integrates direct SQL queries for advanced database management.

Technologies Used
🔹 Python & Django – Backend framework for robust web application handling 
🔹 SQLite – Database for managing clinic records efficiently 
🔹 Raw SQL Queries – Direct SQL execution for precise database control 
🔹 HTML, CSS, JavaScript – Frontend components for user interaction (if applicable)

Installation & Setup
1️⃣ Clone the repository:

bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Clinic-Inventory-Management.git
cd Clinic-Inventory-Management
2️⃣ Install dependencies:

bash
pip install -r requirements.txt
3️⃣ Run migrations:

bash
python manage.py migrate --fake  # Since tables exist already
4️⃣ Start the server:

bash
python manage.py runserver
Usage
Admins can add, edit, and delete patient records

Medicine inventory is auto-updated based on consumption

Clinics can track medical services given and ensure data consistency

Inventory Management allows clinics to monitor stock levels, detect shortages, and manage replenishment
