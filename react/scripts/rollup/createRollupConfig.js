/* eslint-disable import/no-extraneous-dependencies */
import commonjs from "@rollup/plugin-commonjs";
import external from "rollup-plugin-peer-deps-external";
import sourcemaps from "rollup-plugin-sourcemaps";
import { terser } from "rollup-plugin-terser";
import typescript from "rollup-plugin-typescript2";
import { nodeResolve } from "@rollup/plugin-node-resolve";

export function createRollupConfig(options) {
  const { name } = options;
  // A file with the extension ".mjs" will always be treated as ESM, even when pkg.type is "commonjs" (the default)
  // https://nodejs.org/docs/latest/api/packages.html#packages_determining_module_system
  const extName = options.format === "esm" ? "mjs" : "js";
  const outputName = `dist/${[name, options.format, extName].join(".")}`;

  const plugins = [
    external(),
    typescript({
      tsconfig: options.tsconfig,
      clean: true,
      exclude: [
        "**/__tests__",
        "**/*.test.ts",
        "**/*.stories.ts",
        "/scripts/**/*"
      ]
    }),
    sourcemaps(),
    nodeResolve({})
  ];

  if (options.format === "umd") {
    plugins.push(
      commonjs({
        include: "/node_modules/",
        defaultIsModuleExports: true
      })
    );
  }

  if (options.format === "esm") {
    plugins.push(
      terser({
        output: { comments: false },
        compress: {
          drop_console: true
        }
      })
    );
  }

  const config = {
    input: options.input,
    output: {
      file: outputName,
      format: options.format,
      name: "CircuitsVis",
      sourcemap: true,
      globals: { react: "React" },
      exports: "named"
    },
    plugins
  };

  return config;
}
