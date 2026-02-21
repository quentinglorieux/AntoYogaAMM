<template>
  <nav class="bg-white/90 backdrop-blur-md shadow-sm sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <!-- Logo / Titre et switcher -->
        <div class="flex items-center gap-4 z-50 relative">
          <NuxtLink to="/" class="text-2xl font-light text-gray-800 hover:text-gray-600 transition-colors"
            @click="isOpen = false">
            Antonine Rochet
          </NuxtLink>

          <!-- Switcher Desktop -->
          <div class="hidden md:flex items-center gap-4">
            <!-- Switcher Yoga -> Montagne -->
            <NuxtLink v-if="isYogaSection" to="/mountain/sorties"
              class="text-gray-600 hover:text-blue-600 transition-colors flex items-center gap-1.5 px-2 py-1 rounded-lg hover:bg-blue-50"
              title="Aller vers la section Montagne">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M3 20h2l4-8 3 6 2-4 3 6h4L14 8l-3 6-3-6z" />
              </svg>
              <span class="text-xs font-medium">Montagne</span>
            </NuxtLink>

            <!-- Switcher Montagne -> Yoga -->
            <NuxtLink v-if="isMountainSection" to="/yoga/studio"
              class="text-gray-600 hover:text-orange-600 transition-colors flex items-center gap-1.5 px-2 py-1 rounded-lg hover:bg-orange-50"
              title="Aller vers la section Yoga">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
                <path
                  d="M12 2c-.6 0-1 .4-1 1v2c0 .6.4 1 1 1s1-.4 1-1V3c0-.6-.4-1-1-1zm-7 9H3c-.6 0-1 .4-1 1s.4 1 1 1h2c.6 0 1-.4 1-1s-.4-1-1-1zm16 0h-2c-.6 0-1 .4-1 1s.4 1 1 1h2c.6 0 1-.4 1-1s-.4-1-1-1zM12 8c-2.2 0-4 1.8-4 4 0 1.5.8 2.8 2 3.5V18c0 1.1.9 2 2 2s2-.9 2-2v-2.5c1.2-.7 2-2 2-3.5 0-2.2-1.8-4-4-4zm-1 9v1c0 .6-.4 1-1 1s-1-.4-1-1v-4.3c-.6-.5-1-1.3-1-2.2 0-1.4 1.1-2.5 2.5-2.5h1c1.4 0 2.5 1.1 2.5 2.5 0 .9-.4 1.7-1 2.2V17c0 .6-.4 1-1 1s-1-.4-1-1v-1h-1v1z" />
                <circle cx="8" cy="18" r="2" />
                <circle cx="16" cy="18" r="2" />
              </svg>
              <span class="text-xs font-medium">Yoga</span>
            </NuxtLink>
          </div>
        </div>

        <!-- Navigation Yoga Desktop -->
        <div v-if="isYogaSection" class="hidden md:flex items-center space-x-6">
          <NuxtLink to="/yoga/studio" class="text-gray-600 hover:text-orange-600 transition-colors"
            active-class="text-orange-600 font-medium">
            Le Studio
          </NuxtLink>
          <NuxtLink to="/yoga/cours" class="text-gray-600 hover:text-orange-600 transition-colors"
            active-class="text-orange-600 font-medium">
            Les Cours
          </NuxtLink>
          <NuxtLink to="/yoga/iyengar" class="text-gray-600 hover:text-orange-600 transition-colors"
            active-class="text-orange-600 font-medium">
            Le Yoga Iyengar
          </NuxtLink>
          <NuxtLink to="/yoga/enseignante" class="text-gray-600 hover:text-orange-600 transition-colors"
            active-class="text-orange-600 font-medium">
            L'Enseignante
          </NuxtLink>
          <NuxtLink to="/yoga/stages" class="text-gray-600 hover:text-orange-600 transition-colors"
            active-class="text-orange-600 font-medium">
            Les Stages
          </NuxtLink>
          <NuxtLink to="/blog" class="text-gray-600 hover:text-orange-600 transition-colors"
            active-class="text-orange-600 font-medium">
            Le Blog
          </NuxtLink>
        </div>

        <!-- Navigation Montagne Desktop -->
        <div v-if="isMountainSection" class="hidden md:flex items-center space-x-6">
          <NuxtLink to="/mountain/sorties" class="text-gray-600 hover:text-blue-600 transition-colors"
            active-class="text-blue-600 font-medium">
            Les Sorties
          </NuxtLink>
          <NuxtLink to="/mountain/accompagnatrice" class="text-gray-600 hover:text-blue-600 transition-colors"
            active-class="text-blue-600 font-medium">
            L'Accompagnatrice
          </NuxtLink>
          <!-- <NuxtLink to="/mountain/contact" class="text-gray-600 hover:text-blue-600 transition-colors"
            active-class="text-blue-600 font-medium">
            Contact
          </NuxtLink> -->
          <NuxtLink to="/blog" class="text-gray-600 hover:text-blue-600 transition-colors"
            active-class="text-blue-600 font-medium">
            Le Blog
          </NuxtLink>
        </div>

        <!-- Mobile Menu Button -->
        <div class="md:hidden flex items-center z-50 relative">
          <button @click="isOpen = !isOpen"
            class="text-gray-600 hover:text-gray-900 focus:outline-none p-2 rounded-md hover:bg-gray-100 transition-colors">
            <span class="sr-only">Open menu</span>
            <svg v-if="!isOpen" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
            <svg v-else class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Menu Overlay -->
    <Teleport to="body">
      <Transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 translate-y-full"
        enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-200 ease-in"
        leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-full">
        <div v-if="isOpen" class="fixed inset-0 z-40 bg-white md:hidden overflow-y-auto">
          <div class="flex flex-col min-h-[100dvh] pt-24 px-6 pb-12 space-y-8">

            <!-- Mobile Links Yoga -->
            <div v-if="isYogaSection" class="flex flex-col space-y-6 text-center">
              <NuxtLink to="/yoga/studio"
                class="text-2xl font-light text-gray-800 hover:text-orange-600 transition-colors"
                active-class="text-orange-600 font-medium" @click="isOpen = false">
                Le Studio
              </NuxtLink>
              <NuxtLink to="/yoga/cours" class="text-2xl font-light text-gray-800 hover:text-orange-600 transition-colors"
                active-class="text-orange-600 font-medium" @click="isOpen = false">
                Les Cours
              </NuxtLink>
              <NuxtLink to="/yoga/iyengar"
                class="text-2xl font-light text-gray-800 hover:text-orange-600 transition-colors"
                active-class="text-orange-600 font-medium" @click="isOpen = false">
                Le Yoga Iyengar
              </NuxtLink>
              <NuxtLink to="/yoga/enseignante"
                class="text-2xl font-light text-gray-800 hover:text-orange-600 transition-colors"
                active-class="text-orange-600 font-medium" @click="isOpen = false">
                L'Enseignante
              </NuxtLink>
              <NuxtLink to="/yoga/stages"
                class="text-2xl font-light text-gray-800 hover:text-orange-600 transition-colors"
                active-class="text-orange-600 font-medium" @click="isOpen = false">
                Les Stages
              </NuxtLink>
              <NuxtLink to="/blog" class="text-2xl font-light text-gray-800 hover:text-orange-600 transition-colors"
                active-class="text-orange-600 font-medium" @click="isOpen = false">
                Le Blog
              </NuxtLink>
            </div>

            <!-- Mobile Links Montagne -->
            <div v-if="isMountainSection" class="flex flex-col space-y-6 text-center">
              <NuxtLink to="/mountain/sorties"
                class="text-2xl font-light text-gray-800 hover:text-blue-600 transition-colors"
                active-class="text-blue-600 font-medium" @click="isOpen = false">
                Les Sorties
              </NuxtLink>
              <NuxtLink to="/mountain/accompagnatrice"
                class="text-2xl font-light text-gray-800 hover:text-blue-600 transition-colors"
                active-class="text-blue-600 font-medium" @click="isOpen = false">
                L'Accompagnatrice
              </NuxtLink>
              <NuxtLink to="/mountain/contact"
                class="text-2xl font-light text-gray-800 hover:text-blue-600 transition-colors"
                active-class="text-blue-600 font-medium" @click="isOpen = false">
                Contact
              </NuxtLink>
              <NuxtLink to="/blog" class="text-2xl font-light text-gray-800 hover:text-blue-600 transition-colors"
                active-class="text-blue-600 font-medium" @click="isOpen = false">
                Le Blog
              </NuxtLink>
            </div>

            <!-- Divider -->
            <div class="w-24 h-px bg-gray-200 mx-auto"></div>

            <!-- Mobile Switcher -->
            <div class="flex justify-center">
              <NuxtLink v-if="isYogaSection" to="/mountain/sorties"
                class="inline-flex items-center gap-2 text-lg text-gray-500 hover:text-blue-600 transition-colors py-2 px-4 rounded-xl hover:bg-blue-50"
                @click="isOpen = false">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M3 20h2l4-8 3 6 2-4 3 6h4L14 8l-3 6-3-6z" />
                </svg>
                <span>Passer à la Montagne</span>
              </NuxtLink>

              <NuxtLink v-if="isMountainSection" to="/yoga/studio"
                class="inline-flex items-center gap-2 text-lg text-gray-500 hover:text-orange-600 transition-colors py-2 px-4 rounded-xl hover:bg-orange-50"
                @click="isOpen = false">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
                  <path
                    d="M12 2c-.6 0-1 .4-1 1v2c0 .6.4 1 1 1s1-.4 1-1V3c0-.6-.4-1-1-1zm-7 9H3c-.6 0-1 .4-1 1s.4 1 1 1h2c.6 0 1-.4 1-1s-.4-1-1-1zm16 0h-2c-.6 0-1 .4-1 1s.4 1 1 1h2c.6 0 1-.4 1-1s-.4-1-1-1zM12 8c-2.2 0-4 1.8-4 4 0 1.5.8 2.8 2 3.5V18c0 1.1.9 2 2 2s2-.9 2-2v-2.5c1.2-.7 2-2 2-3.5 0-2.2-1.8-4-4-4zm-1 9v1c0 .6-.4 1-1 1s-1-.4-1-1v-4.3c-.6-.5-1-1.3-1-2.2 0-1.4 1.1-2.5 2.5-2.5h1c1.4 0 2.5 1.1 2.5 2.5 0 .9-.4 1.7-1 2.2V17c0 .6-.4 1-1 1s-1-.4-1-1v-1h-1v1z" />
                  <circle cx="8" cy="18" r="2" />
                  <circle cx="16" cy="18" r="2" />
                </svg>
                <span>Passer au Yoga</span>
              </NuxtLink>
            </div>

          </div>
        </div>
      </Transition>
    </Teleport>
  </nav>
</template>

<script setup lang="ts">
const route = useRoute()
const isOpen = ref(false)

// Close menu when route changes
watch(() => route.path, () => {
  isOpen.value = false
})

const isMountainSection = computed(() => {
  return route.path.startsWith('/mountain')
})

const isYogaSection = computed(() => {
  return !isMountainSection.value
})
</script>
