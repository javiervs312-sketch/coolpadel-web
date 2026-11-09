/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './index.html',
    './assets/**/*.js',
    './paises/**/*.html',
    './ciudades/**/*.html'
  ],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        outfit: ['Outfit', 'sans-serif'],
        jakarta: ['Plus Jakarta Sans', 'sans-serif'],
      },
      colors: {
        cool: {
          navy: '#091322',
          dark: '#0e1d33',
          card: '#132845',
          blue: '#0284c7',
          cyan: '#76d3f6',
          orange: '#f2920b',
          amber: '#d97706'
        }
      },
      animation: {
        'ticker-slow': 'tickerSlow 30s linear infinite',
        'ticker-trusted': 'tickerSlow 45s linear infinite',
      },
      keyframes: {
        tickerSlow: {
          '0%': { transform: 'translateX(0%)' },
          '100%': { transform: 'translateX(-50%)' }
        }
      }
    }
  },
  plugins: [],
}
