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
  }
},
}
