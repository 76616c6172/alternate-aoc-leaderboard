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
    colors: {
      whi: '#cccccc',
      gre: '#009900',
      yel: '#ffff66',
      ora: '#886655',
      grey: '#666666',
    },
  }
},
}
