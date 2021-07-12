import colors from 'vuetify/es5/util/colors'

export default {
  customVariables: ['~/assets/variables.scss'],
  options: {
    customProperties: true
  },
  treeShake: true,
  theme: {
    options: {
      customProperties: true
    },
    themes: {
      light: {
        primary: '#007bff',
        secondary: colors.shades.white,
        invert: colors.shades.black,
        accent: colors.pink.lighten1,
        error: colors.red.accent3
      },
      dark: {
        primary: '#007bff',
        secondary: colors.shades.black,
        invert: colors.shades.white,
        accent: colors.pink.lighten1,
        error: colors.red.accent3
      }
    },
    treeShake: true,
    dark: false
  }
}
