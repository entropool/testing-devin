<template>
  <div id="app">
    <el-container>
      <el-header>
        <div class="logo">
          <img src="@/assets/logo.png" alt="EntroPool Logo">
        </div>
        <nav>
          <ul>
            <li><a href="#">CODE SCAN</a></li>
            <li><a href="#">DOWNLOAD</a></li>
            <li><a href="#">DOCUMENT</a></li>
            <li><a href="#">SIGN IN</a></li>
          </ul>
        </nav>
      </el-header>
      <el-container>
        <el-aside width="150px">
          <h2>Sidebar</h2>
          <ul>
            <li><a href="#">Link 1</a></li>
            <li><a href="#">Link 2</a></li>
            <li><a href="#">Link 3</a></li>
          </ul>
        </el-aside>
        <el-main>
          <div class="banner">
            <h1>The AI Powered AppSec Expert</h1>
            <h2>Unique Cyber Security Based MoE LLM</h2>
            <button>Free Code Scan</button>
          </div>
          <div class="content">
            <h2>Why Oxpecker?</h2>
            <ul>
              <li><i class="icon"></i> False Positive - ZERO!</li>
              <li><i class="icon"></i> User Interaction - ZERO!</li>
            </ul>
          </div>
        </el-main>
      </el-container>
      <el-footer>
        <ul>
          <li><a href="#">SERVICES</a></li>
          <li><a href="#">CAREERS</a></li>
          <li><a href="#">PARTNER</a></li>
          <li><a href="#">ABOUT US</a></li>
        </ul>
        <div class="social-media">
          <a href="#"><i class="icon-twitter"></i></a>
          <a href="#"><i class="icon-facebook"></i></a>
          <a href="#"><i class="icon-youtube"></i></a>
          <a href="#"><i class="icon-linkedin"></i></a>
        </div>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

el-header, el-footer {
  background-color: #3e8ef7;
  color: white;
  text-align: center;
  line-height: 60px;
  padding: 20px;
}

el-footer {
  background-color: #2c3e50; /* Different background color for visual distinction */
  padding: 30px; /* Additional padding for better separation */
  border-top: 2px solid #ffffff; /* Add a border for better separation */
}

el-aside {
  background-color: #f5f5f5;
  color: #333;
  text-align: center;
  line-height: 200px;
  padding: 20px;
  height: 100vh; /* Ensure the sidebar extends the full height of the viewport */
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

el-main {
  background-color: #ffffff;
  color: #333;
  text-align: center;
  line-height: 160px;
  padding: 40px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

nav ul {
  list-style: none;
  padding: 0;
  display: flex;
  justify-content: center;
}

nav ul li {
  margin: 0 15px;
}

nav ul li a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

nav ul li a:hover {
  text-decoration: underline;
}

ul {
  list-style: none;
  padding: 0;
}

ul li {
  margin: 10px 0;
}

ul li a {
  color: #333;
  text-decoration: none;
}

ul li a:hover {
  text-decoration: underline;
}

button {
  background-color: #3e8ef7;
  color: white;
  border: none;
  padding: 15px 30px; /* Increased padding for better tap target */
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #2c3e50;
}

/* Responsive Design */
@media (max-width: 768px) {
  el-aside {
    display: none;
  }
  el-main {
    line-height: 200px;
  }
}

@media (min-width: 769px) and (max-width: 1024px) {
  el-aside {
    width: 150px;
  }
  el-main {
    line-height: 180px;
  }
}
</style>
