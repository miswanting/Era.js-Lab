import { defineConfig } from 'windicss/helpers'

export default defineConfig({
  darkMode: 'class',
  safelist: [
    // Typography
    'text-center',
    'text-gray-400',
    // Backgrounds
    'bg-black',
    'bg-white',
    'bg-gray-200',
    'bg-gray-300',
    'bg-gray-400',
    'bg-gray-600',
    'bg-gray-700',
    'bg-gray-800',
    'bg-red-200',
    'bg-red-300',
    // Borders
    'rounded',
    'rounded-t',
    'rounded-b',
    'border',
    'border-gray-300',
    // Spacing
    'p-1',
    'px-1',
    'p-2',
    'm-1',
    'mx-2',
    'm-2',
    // Sizing
    'w-full',
    'w-screen',
    'w-max',
    'h-full',
    'h-screen',
    // Display
    'inline-block',
    // Flexbox
    'flex',
    'flex-col',
    'flex-grow',
    // Grid
    'grid',
    // Positioning
    'items-center',
    'items-end',
    'place-items-center',
    'absolute',
    'relative',
    'z-1',
    'top-0',
    'bottom-0',
    'left-0',
    'right-0',
    // Effects
    'shadow',
    'shadow-gray-500',
    // Behaviors
    'cursor-pointer',
    'cursor-move',
    'overflow-x-visible',
    'overflow-x-scroll',
    'bg-light-800',
    'select-none'
  ]
})
