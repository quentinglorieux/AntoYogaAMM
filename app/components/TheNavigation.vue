<template>
  <nav class="bg-white shadow-sm">
    <div class="max-w-7xl mx-auto px-6">
      <div class="flex items-center justify-between h-16">
        <!-- Logo / Titre -->
        <NuxtLink 
          to="/" 
          class="text-2xl font-light text-gray-800 hover:text-gray-600 transition-colors"
        >
          Antonine Rochet
        </NuxtLink>

        <!-- Navigation Yoga -->
        <div v-if="isYogaSection" class="flex items-center space-x-6">
          <NuxtLink 
            to="/yoga/studio" 
            class="text-gray-600 hover:text-teal-600 transition-colors"
            active-class="text-teal-600 font-medium"
          >
            Le Studio
          </NuxtLink>
          <NuxtLink 
            to="/yoga/cours" 
            class="text-gray-600 hover:text-teal-600 transition-colors"
            active-class="text-teal-600 font-medium"
          >
            Les Cours
          </NuxtLink>
          <NuxtLink 
            to="/yoga/iyengar" 
            class="text-gray-600 hover:text-teal-600 transition-colors"
            active-class="text-teal-600 font-medium"
          >
            Le Yoga Iyengar
          </NuxtLink>
          <NuxtLink 
            to="/yoga/enseignante" 
            class="text-gray-600 hover:text-teal-600 transition-colors"
            active-class="text-teal-600 font-medium"
          >
            L'Enseignante
          </NuxtLink>
          <NuxtLink 
            to="/yoga/stages" 
            class="text-gray-600 hover:text-teal-600 transition-colors"
            active-class="text-teal-600 font-medium"
          >
            Les Stages
          </NuxtLink>
        </div>

        <!-- Navigation Montagne -->
        <div v-if="isMountainSection" class="flex items-center space-x-6">
          <NuxtLink 
            to="/mountain/sorties" 
            class="text-gray-600 hover:text-blue-600 transition-colors"
            active-class="text-blue-600 font-medium"
          >
            Les Sorties
          </NuxtLink>
          <NuxtLink 
            to="/mountain/accompagnatrice" 
            class="text-gray-600 hover:text-blue-600 transition-colors"
            active-class="text-blue-600 font-medium"
          >
            L'Accompagnatrice
          </NuxtLink>
          <NuxtLink 
            to="/mountain/contact" 
            class="text-gray-600 hover:text-blue-600 transition-colors"
            active-class="text-blue-600 font-medium"
          >
            Contact
          </NuxtLink>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
const route = useRoute()

const isYogaSection = computed(() => {
  return route.path.startsWith('/yoga')
})

const isMountainSection = computed(() => {
  return route.path.startsWith('/mountain')
})
</script>
