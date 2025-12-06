import { defineStore } from 'pinia'
import translations from '~/locales/translations'

export const useLanguageStore = defineStore('language', {
  state: () => ({
    currentLang: 'ru' as 'kz' | 'ru'
  }),
  
  getters: {
    t: (state) => {
      return translations[state.currentLang]
    },
    isKazakh: (state) => state.currentLang === 'kz',
    isRussian: (state) => state.currentLang === 'ru'
  },
  
  actions: {
    setLanguage(lang: 'kz' | 'ru') {
      this.currentLang = lang
      if (process.client) {
        localStorage.setItem('language', lang)
      }
    },
    
    toggleLanguage() {
      this.currentLang = this.currentLang === 'kz' ? 'ru' : 'kz'
      if (process.client) {
        localStorage.setItem('language', this.currentLang)
      }
    },
    
    init() {
      if (process.client) {
        const savedLang = localStorage.getItem('language') as 'kz' | 'ru'
        if (savedLang && (savedLang === 'kz' || savedLang === 'ru')) {
          this.currentLang = savedLang
        }
      }
    }
  }
})
