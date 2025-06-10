# Note: This file is command using 
# raw SQL queries with Django's database connection
# it was created to fix the problem in migration, because the db is currently updating in prod.




from django.db import connection
with connection.cursor() as cursor:
    # Create Location Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clinic_location (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location VARCHAR(200) NOT NULL
        );
    """)

from django.db import connection
with connection.cursor() as cursor:
    # Create Gender Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clinic_gender (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gender VARCHAR(200) NOT NULL
        );
    """)

from django.db import connection
with connection.cursor() as cursor:
    # Create Company Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clinic_company (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company VARCHAR(200) NOT NULL
        );
    """)

from django.db import connection
with connection.cursor() as cursor:
    # Create Illness Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clinic_illness (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            illness VARCHAR(200) NOT NULL
        );
    """)

from django.db import connection
with connection.cursor() as cursor:
    # Create AMR Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clinic_amr (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amr VARCHAR(200) NOT NULL
        );
    """)

from django.db import connection
with connection.cursor() as cursor:
    # Create Demand Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clinic_demand (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            demand VARCHAR(30) NOT NULL
        );
    """)

from django.db import connection

with connection.cursor() as cursor:
    # Create MedCode Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clinic_medcode (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code VARCHAR(200) NULL,
            medicine VARCHAR(200) NULL,
            quantity INTEGER NULL,
            clinic_date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP NULL,
            critical INTEGER NULL,
            consumed INTEGER DEFAULT 0 NULL,
            demand_id INTEGER NULL,
            location_id INTEGER NULL, 
            FOREIGN KEY (demand_id) REFERENCES clinic_demand(id),
            FOREIGN KEY (location_id) REFERENCES clinic_location(id)
        );
    """)


#********************************************************************* modified medicine
from django.db import connection
with connection.cursor() as cursor:
    # Create New clinic_medicine Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clinic_medicine (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            medicine VARCHAR(200) NULL,
            quantity INTEGER NULL DEFAULT 0,
            clinic_date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP NULL,
            critical INTEGER NULL,
            consumed INTEGER DEFAULT 0 NULL,
            medcode_id INTEGER NULL,
            demand_id INTEGER NULL,
            location_id INTEGER NULL,
            FOREIGN KEY (medcode_id) REFERENCES clinic_medcode(id) ON DELETE SET NULL,
            FOREIGN KEY (demand_id) REFERENCES clinic_demand(id) ON DELETE SET NULL,
            FOREIGN KEY (location_id) REFERENCES clinic_location(id) ON DELETE SET NULL
        );
    """)
#*********************************************************************************



from django.db import connection
with connection.cursor() as cursor:
    # Create MedicineMovement Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clinic_medicinemovement (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code VARCHAR(200) NULL,
            medicine VARCHAR(200) NULL,
            quantity INTEGER NULL,
            clinic_date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP NULL,
            note TEXT NULL,
            location_id INTEGER NULL,
            FOREIGN KEY (location_id) REFERENCES clinic_location(id)
        );
    """)



from django.db import connection
with connection.cursor() as cursor:
    # Create MedicalServiceGiven Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clinic_medicalservicegiven (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            medical_given VARCHAR(100) NOT NULL
        );
    """)



from django.db import connection
with connection.cursor() as cursor:
    # Create Clinic_Record Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clinic_clinic_record (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location_id INTEGER NULL,
            employee_id VARCHAR(50) NULL,
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP NULL,
            first_name VARCHAR(200) NULL,
            last_name VARCHAR(200) NULL,
            gender_id INTEGER NULL,
            company_id INTEGER NULL,
            department VARCHAR(200) NULL,
            illness_id INTEGER NULL,
            amr_id INTEGER NULL,
            medcode_id INTEGER NULL,
            medicine VARCHAR(200) NULL,
            quantity INTEGER NULL,
            medical_given_id INTEGER NULL,
            note TEXT NULL,
            FOREIGN KEY (location_id) REFERENCES clinic_location(id),
            FOREIGN KEY (gender_id) REFERENCES clinic_gender(id),
            FOREIGN KEY (company_id) REFERENCES clinic_company(id),
            FOREIGN KEY (medcode_id) REFERENCES clinic_medicine(id),
            FOREIGN KEY (illness_id) REFERENCES clinic_illness(id),
            FOREIGN KEY (amr_id) REFERENCES clinic_amr(id),
            FOREIGN KEY (medical_given_id) REFERENCES clinic_medicalservicegiven(id)
        );
    """)


#-----------------------------------------------------------------------------------

#Fix: Update Foreign Key References to Use the Correct Table Names


#1️⃣ Drop the Incorrect Foreign Keys


from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("PRAGMA foreign_key_list('clinic_clinic_record');")  # Check FK references
    fk_list = cursor.fetchall()

print("Current Foreign Key References:", fk_list)



#2 Drop the correct Foreign Keys

from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("PRAGMA foreign_keys=OFF;")  # Temporarily disable FK constraints
    cursor.execute("""
        CREATE TABLE clinic_clinic_record_temp AS SELECT * FROM clinic_clinic_record;
    """)
    cursor.execute("DROP TABLE clinic_clinic_record;")
    cursor.execute("""
        CREATE TABLE clinic_clinic_record (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location_id INTEGER NULL,
            employee_id VARCHAR(50) NULL,
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP NULL,
            first_name VARCHAR(200) NULL,
            last_name VARCHAR(200) NULL,
            gender_id INTEGER NULL,
            company_id INTEGER NULL,
            department VARCHAR(200) NULL,
            illness_id INTEGER NULL,
            amr_id INTEGER NULL,
            medcode_id INTEGER NULL,
            medicine VARCHAR(200) NULL,
            quantity INTEGER NULL,
            medical_given_id INTEGER NULL,
            note TEXT NULL,
            FOREIGN KEY (location_id) REFERENCES clinic_location(id),
            FOREIGN KEY (gender_id) REFERENCES clinic_gender(id),
            FOREIGN KEY (company_id) REFERENCES clinic_company(id),
            FOREIGN KEY (medcode_id) REFERENCES clinic_medicine(id),
            FOREIGN KEY (illness_id) REFERENCES clinic_illness(id),
            FOREIGN KEY (amr_id) REFERENCES clinic_amr(id),
            FOREIGN KEY (medical_given_id) REFERENCES clinic_medicalservicegiven(id)
        );
    """)
    cursor.execute("""
        INSERT INTO clinic_clinic_record SELECT * FROM clinic_clinic_record_temp;
    """)
    cursor.execute("DROP TABLE clinic_clinic_record_temp;")
    cursor.execute("PRAGMA foreign_keys=ON;")  # Enable FK constraints again
    connection.commit()

print("Foreign key references updated successfully!")





#3 Verify the Fix

with connection.cursor() as cursor:
    cursor.execute("PRAGMA foreign_key_list('clinic_clinic_record');")
    fk_list = cursor.fetchall()

print("Updated Foreign Key References:", fk_list)


#------------------------------------------------------------------------------



#*If error found:
#   rm -rf clinic/migrations/*.py  # ⚠️ Do NOT delete __init__.py!
#   python manage.py makemigrations clinic
#   python manage.py migrate --fake-initial
#   python manage.py migrate --fake clinic 0001_initial
#   python manage.py migrate clinic --fake


# Test view of tables

from django.db import connection

# Open a database connection and execute the query
with connection.cursor() as cursor:
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")  # Retrieve all table names
    tables = cursor.fetchall()  # Fetch all results

# Print the list of tables
for table in tables:
    print(table[0])  # Each 'table' is a tuple, so we use [0] to access the table name




#check fields
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("PRAGMA table_info(clinic_medcode);")  # Check table structure
    columns = cursor.fetchall()

for column in columns:
    print(column)  # Displays field name, type, etc.



#drop table
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("DROP TABLE IF EXISTS clinic_medicinemovement;")  # Safely drops the table
    connection.commit()

print("Table clinic_medcode dropped successfully!")





