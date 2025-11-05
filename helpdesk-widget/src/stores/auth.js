import { reactive } from 'vue'

const state = reactive({
  user: null, // { id, username }
  isAuthenticated: false,
})

export function setUser(user) {
  state.user = user
  state.isAuthenticated = !!user
}

export function clearUser() {
  state.user = null
  state.isAuthenticated = false
}

export default state
