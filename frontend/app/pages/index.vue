<template>
  <div class="min-h-screen bg-gray-100 flex">
    <!-- Sidebar -->
    <aside class="w-64 bg-white shadow-md flex flex-col">
      <div class="p-6 font-bold text-xl border-b">Dashboard</div>
      <nav class="flex-1 p-4">
        <ul>
          <li class="mb-2">
            <a href="#" class="block py-2 px-4 rounded hover:bg-gray-200">Inicio</a>
          </li>
          <li class="mb-2">
            <a href="#" class="block py-2 px-4 rounded hover:bg-gray-200">Usuarios</a>
          </li>
          <li class="mb-2">
            <a href="#" class="block py-2 px-4 rounded hover:bg-gray-200">Reportes</a>
          </li>
        </ul>
      </nav>
    </aside>
    <!-- Main Content -->
    <main class="flex-1 p-8">
      <h1 class="text-2xl font-semibold mb-6">Bienvenido al Dashboard</h1>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="bg-white p-6 rounded shadow">
          <h2 class="text-lg font-bold mb-2">Usuarios</h2>
          <p class="text-gray-600">Gestión de usuarios y permisos.</p>
        </div>
        <div class="bg-white p-6 rounded shadow">
          <h2 class="text-lg font-bold mb-2">Reportes</h2>
          <p class="text-gray-600">Visualiza estadísticas y reportes.</p>
        </div>
        <div class="bg-white p-6 rounded shadow">
          <h2 class="text-lg font-bold mb-2">Configuración</h2>
          <p class="text-gray-600">Ajusta las preferencias del sistema.</p>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
// No se requiere lógica para el layout básico
</script>