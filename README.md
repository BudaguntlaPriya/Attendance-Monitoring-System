# Attendance-Monitoring-System
<h3>1. Project Overview:</h3>
This project is a real-time Interactive Attendance Dashboard designed to monitor student attendance across various subjects. It features a modern, decoupled architecture with a FastAPI backend and an interactive Plotly Dash frontend, ensuring high performance and real-time data synchronization.<br>
<h3>2. Technology Stack</h3>
<ul>
<li>Backend Framework:</li> FastAPI (Python) for RESTful API development.

<li>Frontend Dashboard:</li> Plotly Dash for interactive data visualizations.

<li>Database:</li> MongoDB (NoSQL) for flexible document storage and student records.

<li>Data Processing:</li>Pandas for handling and filtering 50+ student records.</ul>
<h3>3. Core Features</h3>
<ul>
<li>CRUD Operations: Implemented RESTful endpoints for adding, fetching, and updating attendance records via PATCH requests.</li>

<li>Real-time Synchronization: The dashboard reflects database changes automatically every 2 seconds without manual page refreshes using dcc.Interval.</li>

<li>Multiple Visualizations: Includes Bar charts for subject-wise attendance, Pie charts for distribution, and Scatter plots for statistical insights.</li>

<li>Automated API Docs: Built-in Swagger UI documentation for testing all backend endpoints.</li></ul>
<h3>4. Setup & Installation</h3>
<ol><li>Install Libraries: pip install fastapi uvicorn pymongo pandas dash plotly.</li>

<li>Run Backend: python -m uvicorn main:app --reload (Runs on port 8000).</li>

<li>Run Dashboard: python dashboard.py (Runs on port 8050).</li></ol>
<h3>5. API Documentation</h3>
<ul>
<li>Access Swagger UI: Navigate to http://127.0.0.1:8000/docs to test the endpoints.</li>

<li>PATCH Endpoint: /update_attendance/{roll_no}/{subject_name} - Used to update specific attendance counts in real-time.</li></ul>
<h3>6.System Architecture</h3>

<ul>
<li>Data Layer (MongoDB): Stores student records in a flexible NoSQL document format, allowing for easy data manipulation of 50+ records.</li>

<li>Logic Layer (FastAPI): Acts as the bridge between the database and the UI. It implements RESTful CRUD operations with built-in error handling (e.g., 404 for missing records).</li>

<li>Presentation Layer (Dash & Plotly): A reactive frontend that polls the backend API every 2 seconds. It uses dcc.Interval to ensure the dashboard reflects database changes in real-time without a manual page refresh.</li></ul>







