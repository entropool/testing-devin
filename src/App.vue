<template>
  <div id="app">
    <el-container>
      <el-header>
        <h1>Header</h1>
        <nav>
          <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Contact</a></li>
          </ul>
        </nav>
      </el-header>
      <el-container>
        <el-aside width="200px">
          <h2>Sidebar</h2>
          <ul>
            <li><a href="#">Link 1</a></li>
            <li><a href="#">Link 2</a></li>
            <li><a href="#">Link 3</a></li>
          </ul>
        </el-aside>
        <el-main>
          <h2>Main Content</h2>
          <p>This is the main content area.</p>
        </el-main>
      </el-container>
      <el-footer>
        <h2>Footer</h2>
        <p>Additional information or links can go here.</p>
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

el-aside {
  background-color: #f5f5f5;
  color: #333;
  text-align: center;
  line-height: 200px;
  padding: 20px;
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
  padding: 10px 20px;
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
