module.exports = [
  {
    languageOptions: {
      parserOptions: {
        parser: '@babel/eslint-parser',
        ecmaVersion: 12,
        sourceType: 'module',
      },
      globals: {
        node: true,
        browser: true,
        es2021: true,
      },
    },
    rules: {
      'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
      'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    },
  },
  {
    files: ["*.vue"],
    languageOptions: {
      parser: 'vue-eslint-parser',
      parserOptions: {
        parser: '@babel/eslint-parser',
        ecmaVersion: 12,
        sourceType: 'module',
      },
    },
    plugins: {
      vue: 'eslint-plugin-vue',
    },
    rules: {
      'vue/no-unused-vars': 'error',
      'vue/no-multiple-template-root': 'off',
      'vue/require-default-prop': 'off',
      'vue/require-prop-types': 'off',
      'vue/no-v-html': 'off',
      'vue/valid-v-slot': 'error',
      'vue/valid-v-for': 'error',
      'vue/valid-v-if': 'error',
      'vue/valid-v-else-if': 'error',
      'vue/valid-v-else': 'error',
      'vue/valid-v-model': 'error',
      'vue/valid-v-bind': 'error',
      'vue/valid-v-on': 'error',
      'vue/valid-v-show': 'error',
      'vue/valid-v-pre': 'error',
      'vue/valid-v-cloak': 'error',
      'vue/valid-v-once': 'error',
    },
  },
];
