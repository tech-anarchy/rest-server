/** @type {import('tailwindcss').Config} */

const colors = require("tailwindcss/colors")

export default {
  content: [
    "./index.html", 
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/flowbite-vue/**/*.{js,jsx,ts,tsx,vue}",
    "./node_modules/flowbite/**/*.js",
    "./node_modules/vue-tailwind-datepicker/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        "vtd-primary": colors.sky, // Light mode Datepicker color
        "vtd-secondary": colors.gray, // Dark mode Datepicker color
      },
    },
  },
  plugins: [
    require('flowbite/plugin'),
    require("@tailwindcss/forms")
  ],
}

