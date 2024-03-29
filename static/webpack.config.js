module.exports = {
    mode: 'production',
    performance: {
      hints: false,
      maxEntrypointSize: 512000,
      maxAssetSize: 512000
    },
    devtool: "inline-source-map",
    entry: {
        main: "./typescript/main.tsx"
    },
    output: {
      path: __dirname,
      filename: "[name]-bundle.js"
    },
    resolve: {
      extensions: [".ts", ".tsx", ".js"]
    },
    module: {
            rules: [
              {
                test: /\.tsx?$/,
                use: 'ts-loader',
                exclude: /node_modules/,
              },
              {
                test: /\.css$/i,
                use: [
                 {
                  loader: 'css-loader', options:{
                    url: false
                  }
                }
                ]
              }
            ],
    },
  };