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
  {
    files: ["*.vue"],
    languageOptions: {
      parser: require('vue-eslint-parser'),
      parserOptions: {
        parser: '@babel/eslint-parser',
        ecmaVersion: 12,
        sourceType: 'module',
      },
    },
    plugins: {
      vue: require('eslint-plugin-vue'),
    },
    rules: {
      ...require('eslint-plugin-vue/lib/configs/vue3-essential').rules,
    },
  },
];
