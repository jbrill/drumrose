module.exports = {
  root: true,
  parser: 'babel-eslint',
  env: {
    browser: true,
    node: true,
  },
  extends: ['airbnb-base', 'prettier'],
  // required to lint *.vue files
  plugins: ['html'],
  ignorePatterns: ['node_modules/'],
  // add your custom rules here
  rules: {
    'prettier/prettier': ['error'],
  },
  globals: {},
};
