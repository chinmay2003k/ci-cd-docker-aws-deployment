from flask import Flask, render_template_string

app = Flask(__name__)

portfolio = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Chinmay Khairnar | DevOps Engineer</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:'Poppins',sans-serif;
scroll-behavior:smooth;
}

body{
background:linear-gradient(-45deg,#0f172a,#020617,#1e293b,#0f172a);
background-size:400% 400%;
animation:gradientBG 15s ease infinite;
color:#e2e8f0;
overflow-x:hidden;
}

@keyframes gradientBG{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

header{
text-align:center;
padding:120px 20px 80px 20px;
position:relative;
}

header h1{
font-size:50px;
background:linear-gradient(90deg,#38bdf8,#facc15);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.typing{
margin-top:15px;
font-size:20px;
color:#94a3b8;
}

section{
padding:70px 10%;
}

h2{
font-size:28px;
margin-bottom:25px;
color:#38bdf8;
position:relative;
display:inline-block;
}

.card{
background:rgba(30,41,59,0.6);
backdrop-filter:blur(15px);
padding:25px;
margin:20px 0;
border-radius:15px;
transition:0.4s;
box-shadow:0 10px 30px rgba(0,0,0,0.5);
}

.card:hover{
transform:translateY(-8px);
box-shadow:0 15px 40px rgba(56,189,248,0.4);
}

.skills{
margin-top:20px;
}

.skill{
margin-bottom:20px;
}

.bar{
height:8px;
background:#334155;
border-radius:10px;
overflow:hidden;
margin-top:5px;
}

.progress{
height:8px;
background:linear-gradient(90deg,#38bdf8,#facc15);
animation:fill 2s ease-in-out forwards;
}

@keyframes fill{
from{width:0;}
}

.aws{width:90%;}
.docker{width:85%;}
.k8s{width:75%;}
.cicd{width:88%;}

.project-grid{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
gap:20px;
}

.project{
padding:20px;
border-radius:15px;
background:rgba(30,41,59,0.6);
backdrop-filter:blur(15px);
transition:0.4s;
}

.project:hover{
transform:scale(1.05);
box-shadow:0 10px 30px rgba(250,204,21,0.4);
}

a{
color:#38bdf8;
text-decoration:none;
}

a:hover{
color:#facc15;
}

footer{
text-align:center;
padding:25px;
background:#1e293b;
margin-top:50px;
}

.float{
position:absolute;
width:200px;
height:200px;
background:#38bdf8;
border-radius:50%;
filter:blur(120px);
opacity:0.2;
animation:float 10s infinite alternate;
}

.float2{
background:#facc15;
right:0;
animation-duration:12s;
}

@keyframes float{
from{transform:translateY(0);}
to{transform:translateY(-80px);}
}

</style>
</head>

<body>

<div class="float"></div>
<div class="float float2"></div>

<header>
<h1>Chinmay Khairnar</h1>
<div class="typing" id="typing"></div>
</header>

<section>
<h2>Professional Summary</h2>
<div class="card">
Cloud & DevOps Engineer with hands-on experience in Linux administration,
Docker containerization, CI/CD automation, and AWS cloud deployments.
Passionate about scalable architecture, infrastructure automation, and modern DevOps practices.
</div>
</section>

<section>
<h2>Technical Skills</h2>
<div class="card skills">

<div class="skill">AWS
<div class="bar"><div class="progress aws"></div></div>
</div>

<div class="skill">Docker
<div class="bar"><div class="progress docker"></div></div>
</div>

<div class="skill">Kubernetes
<div class="bar"><div class="progress k8s"></div></div>
</div>

<div class="skill">CI/CD
<div class="bar"><div class="progress cicd"></div></div>
</div>

</div>
</section>

<section>
<h2>Projects</h2>
<div class="project-grid">

<div class="project">
<b>CI/CD Automated Pipeline</b><br><br>
GitHub Actions integrated with DockerHub and EC2 for automated deployment.
</div>

<div class="project">
<b>AI Voice Assistant</b><br><br>
Flask backend services integrated with Raspberry Pi for home automation.
</div>

<div class="project">
<b>Library Management System</b><br><br>
Python & MySQL full-stack application for managing book operations.
</div>

</div>
</section>

<section>
<h2>Contact</h2>
<div class="card">
Email: <a href="mailto:chinmaykhairnar182@gmail.com">chinmaykhairnar182@gmail.com</a><br><br>
GitHub: <a href="https://github.com/chinmay2003k" target="_blank">github.com/chinmay2003k</a><br><br>
LinkedIn: <a href="https://linkedin.com/in/chinmay-khairnar-5797a0248" target="_blank">linkedin.com/in/chinmay-khairnar-5797a0248</a>
</div>
</section>

<footer>
© 2026 Chinmay Khairnar | DevOps Portfolio
</footer>

<script>
const text = "Cloud | DevOps | AWS Engineer 🚀";
let i = 0;
function typing(){
if(i < text.length){
document.getElementById("typing").innerHTML += text.charAt(i);
i++;
setTimeout(typing,80);
}
}
typing();
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(portfolio)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)