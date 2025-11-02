🌐 Working with APIs

My continued journey into learning how to gather, process, and visualize data from web-based APIs using Python.

📚 About This Project

Welcome to my Working with APIs repository!
This project is part of my ongoing data visualization learning series — focused on retrieving real-world data automatically and turning it into visual insights.

In this chapter, I learned how to use the GitHub API and the Hacker News API to fetch live data, process it programmatically, and represent it visually using Plotly.

Through these exercises, I explored how APIs can be powerful tools for gathering dynamic information without manual downloads or local files.

🚀 What This Project Covers

This repository includes Python scripts that demonstrate how to make API calls, extract data, and visualize it effectively.

You’ll find examples such as:

🔗 API Calls with Requests: Sending HTTP requests to the GitHub and Hacker News APIs and retrieving structured data responses.

💾 Data Extraction: Parsing JSON responses to extract specific information like repository names, stars, and article links.

📊 Data Visualization: Creating bar charts and interactive visuals using Plotly to represent popularity and trends.

💡 Automating Data Retrieval: Writing programs that automatically gather and process data for analysis.

🎨 Custom Chart Styling: Applying advanced Plotly settings for better presentation and readability.

🧠 Concepts Learned

How to make API requests using the Requests library.

Parsing and handling JSON responses effectively.

Extracting and cleaning data for visualization.

Using Plotly for interactive chart generation.

Working with live web data instead of static files.

Creating self-contained programs that gather, process, and visualize information automatically.

🧰 Tools & Libraries

Python — Core programming language

Requests — For sending API calls and handling HTTP responses

JSON — For parsing structured data from APIs

Plotly — For generating interactive visualizations

📁 File Overview
working-with-apis/
│
├── hn_article.py              # Retrieves and displays top Hacker News articles
├── hn_submissions.py           # Extracts top submissions from Hacker News API
├── python_repos.py             # Fetches top-starred Python repositories via GitHub API
├── python_repos_visual.py      # Visualizes GitHub repository data using Plotly
├── readable_hn_data.json       # Stores processed Hacker News API data
├── .gitignore                  # Common exclusions for Python projects
└── README.md                   # Project documentation (this file)

🧭 Learning Reflection

In this part of my learning series, I moved from static data sources to dynamic, real-world data retrieval.
Using APIs like GitHub and Hacker News showed how data can be accessed, processed, and visualized — all within one automated workflow.

This project helped me understand how to interact with external services, parse complex JSON structures, and convert live data into meaningful visuals.

Learning API integration built a strong foundation for future projects that combine data analytics, automation, and visualization — essential skills for modern data science and software engineering workflows.

🤝 Note

This repository is intended purely for learning and sharing knowledge.
Feel free to explore the scripts, modify them, and experiment with other APIs to extend your own learning journey.
