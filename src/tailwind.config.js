/** @type {import('tailwindcss').Config} */
module.exports = {
  // content: ["./src/pages/**/*.py", "./src/pages/mainpage.py"],
  content: ["./pages/**/*.py", "./pages/mainpage.py", "main.py"],
  theme: {
    extend: {
      fontFamily: {
        'geist-mono': ['"Geist Mono"', 'monospace'],
        goudy: ['"Goudy Bookletter 1911"', 'serif'],
        geist: ['"Geist"', 'sans'],
        opti: ['OPTIEdgarBold-Extended', 'serif'], // 'custom' is the class name you'll use
        cinzel: ['Cinzel', 'serif'],
        ascent: ['ascentis', 'serif'],
        wot: ['Wotfard', 'Sans'],
        com: ['CommitMono-n', 'regular'],
        rh: ['Red Hat Mono, monospace', 'monospace'],
      },
      fontWeight: {
      //'geist-light': '100',
      //'geist-regular': '400',
      //'geist-bold': '700',
    },
  }
},
  plugins: [
    function({ addUtilities }) {
      const newUtilities = {
        '.hover-highlight': {
          'position': 'relative',
          'text-decoration': 'none',
          '&::before': {
            'content': '""',
            'position': 'absolute',
            'left': '-2px',
            'right': '-2px',
            'top': '-1px',
            'bottom': '-1px',
            'background-color': 'white',
            'opacity': '0',
            'transition': 'opacity 0.2s ease',
            'z-index': '-1',
          },
          '&:hover::before': {
            'opacity': '1',
          },
        },
      }
      addUtilities(newUtilities, ['hover']);
    }
  ],
layer: {
    utilities: {
      /* Hide scrollbar for Chrome, Safari and Opera */
      '.no-scrollbar::-webkit-scrollbar': {
        display: 'none',
      },
      /* Hide scrollbar for IE, Edge and Firefox */
      '.no-scrollbar': {
        '-ms-overflow-style': 'none',  /* IE and Edge */
        'scrollbar-width': 'none',  /* Firefox */
      },
    },
  },
}
