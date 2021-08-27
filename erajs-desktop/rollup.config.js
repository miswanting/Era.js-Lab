import multi from '@rollup/plugin-multi-entry';
export default {
  input: ['src/main.ts', 'src/preload.ts'],
  output: {
    dir: 'dist',
    format: 'cjs',
  },
  external: ['electron'],
  plugins: [multi()]
};
