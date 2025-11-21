<template>
  <nav class="bg-white shadow-sm">
    <div class="max-w-7xl mx-auto px-6">
      <div class="flex items-center justify-between h-16">
        <!-- Logo / Titre et switcher -->
        <div class="flex items-center gap-4">
          <NuxtLink 
            to="/" 
            class="text-2xl font-light text-gray-800 hover:text-gray-600 transition-colors"
          >
            Antonine Rochet
          </NuxtLink>
          
          <!-- Switcher Yoga -> Montagne -->
          <NuxtLink 
            v-if="isYogaSection"
            to="/mountain/sorties" 
            class="text-gray-600 hover:text-blue-600 transition-colors flex items-center gap-1.5 px-2 py-1 rounded-lg hover:bg-blue-50"
            title="Aller vers la section Montagne"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
              <path d="M3 20h2l4-8 3 6 2-4 3 6h4L14 8l-3 6-3-6z"/>
            </svg>
            <span class="text-xs font-medium">Montagne</span>
          </NuxtLink>
          
          <!-- Switcher Montagne -> Yoga -->
          <NuxtLink 
            v-if="isMountainSection"
            to="/yoga/studio" 
            class="text-gray-600 hover:text-teal-600 transition-colors flex items-center gap-1.5 px-2 py-1 rounded-lg hover:bg-teal-50"
            title="Aller vers la section Yoga"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 2c-.6 0-1 .4-1 1v2c0 .6.4 1 1 1s1-.4 1-1V3c0-.6-.4-1-1-1zm-7 9H3c-.6 0-1 .4-1 1s.4 1 1 1h2c.6 0 1-.4 1-1s-.4-1-1-1zm16 0h-2c-.6 0-1 .4-1 1s.4 1 1 1h2c.6 0 1-.4 1-1s-.4-1-1-1zM12 8c-2.2 0-4 1.8-4 4 0 1.5.8 2.8 2 3.5V18c0 1.1.9 2 2 2s2-.9 2-2v-2.5c1.2-.7 2-2 2-3.5 0-2.2-1.8-4-4-4zm-1 9v1c0 .6-.4 1-1 1s-1-.4-1-1v-4.3c-.6-.5-1-1.3-1-2.2 0-1.4 1.1-2.5 2.5-2.5h1c1.4 0 2.5 1.1 2.5 2.5 0 .9-.4 1.7-1 2.2V17c0 .6-.4 1-1 1s-1-.4-1-1v-1h-1v1z"/>
              <circle cx="8" cy="18" r="2"/>
              <circle cx="16" cy="18" r="2"/>
            </svg>
            <span class="text-xs font-medium">Yoga</span>
          </NuxtLink>
        </div>

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
