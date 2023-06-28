/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/*.html'],
  theme: {
    extend: {
      colors: {
        clifford: '#da373d',
      },
    //   adding new font
    fontFamily:{
        Pacifico: ['Pacifico'],
    },

    // adding screen
    screens: {
      'xs':{'min':'10px', 'max':'639px'},
    },
    },
  },
  plugins: [],
}

