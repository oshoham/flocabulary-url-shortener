var webpack = require('webpack');

var baseDir = __dirname + '/url_shortener/static/url_shortener/js';

module.exports = {
  context: baseDir,

  entry: './src/index',

  output: {
    path: baseDir + '/dist',
    filename: 'bundle.js'
  },

  plugins: [
    new webpack.ProvidePlugin({
      'fetch': 'imports?this=>global!exports?global.fetch!whatwg-fetch'
    })
  ],

  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        query: {
          presets: ['react', 'es2015']
        }
      }
    ]
  },

  resolve: {
    modulesDirectories: ['node_modules'],
    extensions: ['', '.js', '.jsx']
  }
};
