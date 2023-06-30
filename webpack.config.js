const path = require('path');

module.exports = {
  entry: './static/assets/js/searchPage.js',
  output: {
    path: path.resolve(__dirname, 'static/dist/js'),
    filename: 'searchPage.js',
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-react', '@babel/preset-env'],
          },
        },
      },
    ],
  },
};
