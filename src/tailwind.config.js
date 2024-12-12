/** @type {import('tailwindcss').Config} */
module.exports = {
  // content: ["./src/pages/**/*.py", "./src/pages/mainpage.py"],
  content: ["./pages/**/*.py", "./pages/mainpage.py", "main.py"],
  theme: {
    extend: {
      fontFamily: {
        scp: ['Source Code Pro', 'monospace'],
      },
      fontWeight: {
    },
    fontSize: {
      // This will globally adjust the base text size
        base: ['1rem', { lineHeight: '1.2' }],// Increased from the default 16px
      // You can also specify line height separately
    },
    colors: {
      whi: '#cccccc',
      gre: '#009900',
      lgre: '#99ff99',
      yel: '#ffff66',
      ora: '#886655',
      grey: '#666666',
    },
  }
},
}
