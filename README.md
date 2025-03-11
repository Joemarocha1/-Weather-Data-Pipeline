# -Weather-Data-Pipeline
This project builds an automated pipeline to collect, process, and store real-time weather data using Python, Weatherbit API, and MySQL. Scheduled with Task Scheduler, it ensures continuous data ingestion. 

Overview

This project builds an automated ETL pipeline to collect, process, and store real-time weather data. The pipeline fetches weather information using the Weatherbit API, processes it with Python and Pandas, stores it in a MySQL database, and visualizes insights using Metabase or Tableau Public.

Features

Automated data ingestion from the Weatherbit API.

Data transformation using Pandas (cleaning, formatting, handling missing values).

Storage in MySQL using SQLAlchemy.

Scheduled execution via Microsoft Task Scheduler.

Dashboard visualization using Metabase or Tableau.

Optional enhancements: Dockerization, error handling, and cloud deployment.

Tools & Technologies

Python (for scripting & ETL)

APIs (Weatherbit API for weather data)

MySQL (database storage)

Pandas (data transformation)

SQLAlchemy (database interaction)

Metabase / Tableau Public (data visualization)

Microsoft Task Scheduler (for automation)

Docker (optional for containerization)
