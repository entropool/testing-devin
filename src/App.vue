<template>
  <div id="app">
    <el-container>
      <el-header>
        <h1>Header</h1>
      </el-header>
      <el-container>
        <el-aside width="200px">
          <h2>Sidebar</h2>
        </el-aside>
        <el-main>
          <h2>Main Content</h2>
        </el-main>
      </el-container>
      <el-footer>
        <h2>Footer</h2>
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
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
  padding: 20px;
}

el-aside {
  background-color: #d3dce6;
  color: #333;
  text-align: center;
  line-height: 200px;
  padding: 20px;
}

el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 160px;
  padding: 20px;
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
