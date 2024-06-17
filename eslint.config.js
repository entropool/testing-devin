module.exports = [
  {
    languageOptions: {
      globals: {
        node: true,
        browser: true,
        es2021: true,
      },
    },
    parserOptions: {
      parser: '@babel/eslint-parser',
      ecmaVersion: 12,
      sourceType: 'module',
    },
    rules: {
      'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
      'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    },
  },
  require('eslint/conf/eslint-recommended'),
  require('eslint-plugin-vue/lib/configs/vue3-essential'),
];
