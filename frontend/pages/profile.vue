<template>
  <NuxtLayout>
    <div class="p-8">
      <!-- Header -->
      <div class="mb-6">
        <h1 class="text-3xl font-bold text-gray-900 mb-2">{{ t.profile.title }}</h1>
        <p class="text-gray-600">{{ t.profile.subtitle }}</p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- Left Column - Profile Card -->
        <div class="lg:col-span-1">
          <div class="rounded-lg bg-white p-6 shadow">
            <div class="text-center">
              <div class="mx-auto mb-4 h-24 w-24 rounded-full bg-gradient-to-br from-blue-500 to-blue-700 flex items-center justify-center">
                <span class="text-4xl font-bold text-white">{{ userInitials }}</span>
              </div>
              <h2 class="text-xl font-bold text-gray-900">{{ profileData.fullName }}</h2>
              <p class="text-sm text-gray-600">{{ profileData.position }}</p>
              <p class="text-xs text-gray-500 mt-1">{{ profileData.department }}</p>
              
              <div class="mt-6 space-y-3 text-sm text-left">
                <div class="flex items-center gap-3">
                  <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                  </svg>
                  <span class="text-gray-900">{{ profileData.email }}</span>
                </div>
                <div class="flex items-center gap-3">
                  <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                  </svg>
                  <span class="text-gray-900">{{ profileData.phone }}</span>
                </div>
              </div>

              <div class="mt-6 pt-6 border-t border-gray-200">
                <div class="flex items-center justify-between text-xs text-gray-600">
                  <span>{{ t.profile.lastLogin }}:</span>
                  <span class="font-medium text-gray-900">{{ formatDate(profileData.lastLogin) }}</span>
                </div>
                <div class="flex items-center justify-between text-xs text-gray-600 mt-2">
                  <span>{{ t.profile.accountCreated }}:</span>
                  <span class="font-medium text-gray-900">{{ formatDate(profileData.accountCreated) }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Column - Settings -->
        <div class="lg:col-span-2 space-y-6">
          <!-- Personal Information -->
          <div class="rounded-lg bg-white p-6 shadow">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">{{ t.profile.personalInfo }}</h3>
            <form @submit.prevent="saveProfile" class="space-y-4">
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">{{ t.profile.fullName }}</label>
                  <input 
                    v-model="profileData.fullName" 
                    type="text" 
                    class="w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">{{ t.profile.emailAddress }}</label>
                  <input 
                    v-model="profileData.email" 
                    type="email" 
                    class="w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">{{ t.profile.phoneNumber }}</label>
                  <input 
                    v-model="profileData.phone" 
                    type="tel" 
                    class="w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">{{ t.profile.position }}</label>
                  <input 
                    v-model="profileData.position" 
                    type="text" 
                    class="w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">{{ t.profile.department }}</label>
                  <input 
                    v-model="profileData.department" 
                    type="text" 
                    class="w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                </div>
              </div>
            </form>
          </div>

          <!-- Account Settings -->
          <div class="rounded-lg bg-white p-6 shadow">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">{{ t.profile.accountSettings }}</h3>
            <div class="space-y-4">
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">{{ t.profile.language }}</label>
                  <select 
                    v-model="profileData.language" 
                    class="w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
                  >
                    <option value="ru">Русский</option>
                    <option value="kz">Қазақша</option>
                    <option value="en">English</option>
                  </select>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">{{ t.profile.timezone }}</label>
                  <select 
                    v-model="profileData.timezone" 
                    class="w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
                  >
                    <option value="Asia/Almaty">Asia/Almaty (UTC+6)</option>
                    <option value="Europe/Moscow">Europe/Moscow (UTC+3)</option>
                    <option value="UTC">UTC</option>
                  </select>
                </div>
              </div>

              <div class="flex items-center justify-between rounded-lg border border-gray-200 p-4">
                <div>
                  <p class="text-sm font-medium text-gray-900">{{ t.profile.emailNotifications }}</p>
                  <p class="text-xs text-gray-500">Получать уведомления о новых инцидентах</p>
                </div>
                <label class="relative inline-flex items-center cursor-pointer">
                  <input v-model="profileData.emailNotifications" type="checkbox" class="sr-only peer" />
                  <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
                </label>
              </div>
            </div>
          </div>

          <!-- Security Settings -->
          <div class="rounded-lg bg-white p-6 shadow">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">{{ t.profile.securitySettings }}</h3>
            <form @submit.prevent="changePassword" class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">{{ t.profile.currentPassword }}</label>
                <input 
                  v-model="passwordData.current" 
                  type="password" 
                  class="w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">{{ t.profile.newPassword }}</label>
                <input 
                  v-model="passwordData.new" 
                  type="password" 
                  class="w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">{{ t.profile.confirmPassword }}</label>
                <input 
                  v-model="passwordData.confirm" 
                  type="password" 
                  class="w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <button type="submit" class="rounded-lg bg-blue-600 px-4 py-2 text-sm font-semibold text-white hover:bg-blue-700 transition-colors">
                {{ t.profile.changePassword }}
              </button>
            </form>

            <div class="mt-6 pt-6 border-t border-gray-200">
              <div class="flex items-center justify-between">
                <div>
                  <p class="text-sm font-medium text-gray-900">{{ t.profile.twoFactorAuth }}</p>
                  <p class="text-xs text-gray-500">Дополнительная защита вашего аккаунта</p>
                </div>
                <button class="rounded-lg border border-gray-300 px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors">
                  {{ t.profile.enable2FA }}
                </button>
              </div>
            </div>
          </div>

          <!-- Save Button -->
          <div class="flex justify-end gap-3">
            <button type="button" class="rounded-lg border border-gray-300 px-6 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors">
              {{ t.common.cancel }}
            </button>
            <button @click="saveProfile" :disabled="saving" class="rounded-lg bg-blue-600 px-6 py-2 text-sm font-semibold text-white hover:bg-blue-700 transition-colors disabled:opacity-50">
              {{ saving ? t.common.loading : t.profile.updateProfile }}
            </button>
          </div>

          <!-- Success Message -->
          <div v-if="showSuccess" class="rounded-lg bg-green-50 border border-green-200 p-4 mt-6">
            <div class="flex items-center gap-3">
              <svg class="h-5 w-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <p class="text-sm font-medium text-green-800">{{ t.profile.profileUpdated }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useLanguageStore } from '~/stores/language'
import { useAuthStore } from '~/stores/auth'
import { getCurrentUser } from '~/api/users'

const langStore = useLanguageStore()
const authStore = useAuthStore()
const t = computed(() => langStore.t)

const loading = ref(true)
const saving = ref(false)
const showSuccess = ref(false)

const profileData = ref({
  fullName: '',
  email: '',
  phone: '',
  position: '',
  department: '',
  language: 'ru',
  timezone: 'Asia/Almaty',
  emailNotifications: true,
  lastLogin: '',
  accountCreated: ''
})

const passwordData = ref({
  current: '',
  new: '',
  confirm: ''
})

const fetchUserData = async () => {
  loading.value = true
  try {
    const user = await getCurrentUser(authStore.token)
    profileData.value.fullName = `${user.first_name || ''} ${user.last_name || ''}`.trim() || user.username
    profileData.value.email = user.email || ''
    // Остальные поля пока захардкожены, т.к. в User модели их нет
    profileData.value.phone = '+7 (727) 244-55-66'
    profileData.value.position = 'Системный администратор'
    profileData.value.department = 'Департамент информационных технологий'
    profileData.value.lastLogin = new Date().toISOString()
    profileData.value.accountCreated = new Date().toISOString()
  } catch (error) {
    console.error('Error fetching user:', error)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchUserData()
})

const userInitials = computed(() => {
  const names = profileData.value.fullName.split(' ')
  return names.map(n => n.charAt(0)).join('').toUpperCase().substring(0, 2)
})

const saveProfile = async () => {
  saving.value = true
  try {
    // TODO: Добавить API endpoint для обновления профиля
    await new Promise(resolve => setTimeout(resolve, 1000))
    showSuccess.value = true
    setTimeout(() => showSuccess.value = false, 3000)
  } catch (error) {
    console.error('Error saving profile:', error)
  } finally {
    saving.value = false
  }
}

const changePassword = async () => {
  if (passwordData.value.new !== passwordData.value.confirm) {
    alert(langStore.currentLang === 'ru' ? 'Пароли не совпадают' : 'Құпия сөздер сәйкес келмейді')
    return
  }
  saving.value = true
  try {
    // TODO: Добавить API endpoint для смены пароля
    await new Promise(resolve => setTimeout(resolve, 1000))
    passwordData.value = { current: '', new: '', confirm: '' }
    showSuccess.value = true
    setTimeout(() => showSuccess.value = false, 3000)
  } catch (error) {
    console.error('Error changing password:', error)
  } finally {
    saving.value = false
  }
}

const formatDate = (date) => {
  if (!date) return 'N/A'
  return new Date(date).toLocaleDateString('ru-RU', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}
</script>
