import { defineConfig } from 'windicss/helpers'

export default defineConfig({
  darkMode: 'class',
  safelist: [
    // Typography
    'text-center',
    // Sizing
    'w-max',
    'h-screen',
    // Flexbox
    'flex',
    'flex-col',
    'flex-grow',
    // Behaviors
    'cursor-pointer',
    'cursor-move',
    'overflow-x-visible',
    'overflow-x-scroll',
    'bg-light-800'
  ]
})
