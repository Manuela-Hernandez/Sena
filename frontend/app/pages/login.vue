<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="bg-white p-8 rounded shadow-md w-full max-w-md">
      <h2 class="text-2xl font-bold mb-6 text-center">Iniciar sesión</h2>
      <form @submit.prevent="login">
        <div class="mb-4">
          <label class="block text-gray-700 mb-2" for="email">Correo electrónico</label>
          <input v-model="email" id="email" type="email" required class="w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500" />
        </div>
        <div class="mb-6">
          <label class="block text-gray-700 mb-2" for="password">Contraseña</label>
          <input v-model="password" id="password" type="password" required class="w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500" />
        </div>
        <button type="submit" class="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition">Entrar</button>
      </form>
      <p v-if="error" class="mt-4 text-red-500 text-center">{{ error }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

definePageMeta({
  layout: false
})

const email = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()

const login = async () => {
  error.value = ''
  try {
    const response = await fetch('http://0.0.0.0:8001/security/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: email.value,
        password: password.value
      })
    })
    if (!response.ok) {
      throw new Error('Credenciales incorrectas')
    }
    const data = await response.json()

    localStorage.setItem('sena_token', data.token)
    router.push('/')
  } catch (err) {
    error.value = err.message || 'Error al iniciar sesión'
  }
}
</script>
