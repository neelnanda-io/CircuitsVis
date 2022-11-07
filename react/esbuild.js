const esbuild = require('esbuild')
const { externalGlobalPlugin } = require("esbuild-plugin-external-global");

/**
 * CDN Build
 */
esbuild.build({
  entryPoints: ['src/index.ts'],
  outfile: 'dist/cdn.umd.js',
  bundle: true,
  globalName: 'CircuitsVis',
  plugins: [
    externalGlobalPlugin({
      'react': 'window.React',
      'react-dom': 'window.ReactDOM',
    })
  ]
});

