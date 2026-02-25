from flask import Flask, render_template_string

app = Flask(__name__)

portfolio = """
<!DOCTYPE html>
<html>
<head>
<title>Chinmay Khairnar | Cloud & DevOps Engineer</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body {
    margin:0;
    font-family: 'Segoe UI', sans-serif;
    background-color:#0f172a;
    color:#e2e8f0;
}
header {
    text-align:center;
    padding:60px 20px;
    background: linear-gradient(90deg,#0f172a,#1e293b);
}
header h1 {
    font-size:40px;
    margin:0;
}
header p {
    font-size:18px;
    color:#94a3b8;
}
section {
    padding:50px 10%;
}
h2 {
    color:#38bdf8;
    border-bottom:2px solid #38bdf8;
    padding-bottom:10px;
}
.card {
    background:#1e293b;
    padding:20px;
    margin:20px 0;
    border-radius:10px;
}
a {
    color:#38bdf8;
    text-decoration:none;
}
a:hover {
    color:#facc15;
}
footer {
    text-align:center;
    padding:20px;
    background:#1e293b;
}
</style>
</head>

<body>

<header>
<h1>Chinmay Khairnar</h1>
<p>Cloud | DevOps | AWS Engineer</p>
<p>Dhule, Maharashtra | 9075728034</p>
</header>

<section>
<h2>Professional Summary</h2>
<div class="card">
Cloud & DevOps Engineer Intern with hands-on experience in Linux administration,
Docker containerization, CI/CD pipeline implementation, and AWS cloud deployments.
Focused on automation, reliability, and modern deployment practices.
</div>
</section>

<section>
<h2>Technical Skills</h2>
<div class="card">
<b>Cloud & DevOps:</b> AWS (EC2, S3, IAM), Azure (VMs, Storage, IAM), CI/CD<br>
<b>Tools:</b> Linux, Docker, Git, GitHub Actions, Kubernetes<br>
<b>Programming:</b> Java, Python<br>
<b>Monitoring:</b> Log Analysis, Troubleshooting, Resource Optimization
</div>
</section>

<section>
<h2>Projects</h2>
<div class="card">
<b>Automated CI/CD Pipeline with Dockerized Nginx</b><br>
Implemented CI/CD workflow using GitHub Actions for automated build and deployment.
Integrated Docker Hub with secure token management.
</div>

<div class="card">
<b>AI-based Voice Assistant for Home Automation</b><br>
Built Flask backend services on Raspberry Pi with secure REST APIs.
</div>

<div class="card">
<b>Library Management System</b><br>
Developed Python-MySQL based full-stack application for library operations.
</div>
</section>

<section>
<h2>Internship Experience</h2>
<div class="card">
<b>Cloud & DevOps Intern – Skillected Institute, Pune</b><br>
Training in AWS, CI/CD, Docker, Kubernetes and cloud infrastructure management.
</div>
</section>

<section>
<h2>Contact</h2>
<div class="card">
Email: <a href="mailto:chinmaykhairnar182@gmail.com">chinmaykhairnar182@gmail.com</a><br>
GitHub: <a href="https://github.com/chinmay2003k" target="_blank">github.com/chinmay2003k</a><br>
LinkedIn: <a href="https://www.linkedin.com/in/chinmay-khairnar-5797a0248" target="_blank">linkedin.com/in/chinmay-khairnar-5797a0248</a>
</div>
</section>

<footer>
© 2026 Chinmay Khairnar | Cloud & DevOps Portfolio
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(portfolio)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)