<template>
  <div class="relative h-screen overflow-hidden">
    <div class="flex h-full w-full">
      <!-- Yoga Panel -->
      <div
        class="relative transition-all duration-700 ease-in-out cursor-pointer overflow-hidden flex items-center justify-center shrink-0"
        :class="activeSection === 'yoga' ? 'basis-[90%]' : 'basis-[10%]'"
        @click="setActiveSection('yoga')"
      >
        <NuxtImg src="/images/yoga-bg.jpg" alt="Yoga" class="absolute inset-0 w-full h-full object-cover" />
        <div class="absolute inset-0 bg-linear-to-br from-purple-900/15 to-pink-900/15"></div>

        <div v-if="activeSection === 'yoga'" class="relative z-10 w-full h-full flex flex-col items-center justify-between py-16 px-8 animate-fade-in">
          <div></div>
          <div class="text-center space-y-6">
            <h1 class="text-7xl font-light text-white drop-shadow-lg">Yoga Iyengar</h1>
            <p class="text-xl text-white/90 max-w-2xl mx-auto drop-shadow">
              Découvrez la pratique du yoga Iyengar avec Antonine Rochet
            </p>
            <div class="flex gap-4 justify-center mt-8">
              <UButton to="/yoga/studio" size="xl" color="primary" variant="solid">
                Découvrir le studio
              </UButton>
              <UButton to="/yoga/cours" size="xl" color="primary" variant="subtle" class="bg-white/10 backdrop-blur">
                Les cours
              </UButton>
            </div>
          </div>
          <div class="inline-block bg-white/60 rounded-lg px-4 py-1 shadow">
            <p class="text-xl text-teal-900 font-medium">
              Larchant, La Chapelle-la-Reine, Nemours, Le Vaudoué, Fontainebleau
            </p>
          </div>
        </div>
        <div v-else class="vertical-text text-3xl font-light text-white relative z-10 drop-shadow">
          Yoga
        </div>
      </div>

      <!-- Mountain Panel -->
      <div
        class="relative transition-all duration-700 ease-in-out cursor-pointer overflow-hidden flex items-center justify-center shrink-0"
        :class="activeSection === 'mountain' ? 'basis-[90%]' : 'basis-[10%]'"
        @click="setActiveSection('mountain')"
      >
        <NuxtImg src="/images/mountain4.jpeg" alt="Montagne" class="absolute inset-0 w-full h-full object-cover" />
        <div class="absolute inset-0 bg-linear-to-br from-blue-900/15 to-green-900/15"></div>

        <div v-if="activeSection === 'mountain'" class="relative z-10 w-full h-full flex flex-col items-center justify-between py-16 px-8 animate-fade-in">
          <div></div>
          <div class="text-center space-y-6">
            <h1 class="text-6xl font-light text-white drop-shadow-lg">Accompagnatrice en Montagne</h1>
            <p class="text-xl text-white/90 max-w-2xl mx-auto drop-shadow">
              Explorez les montagnes avec une accompagnatrice diplômée
            </p>
            <div class="flex gap-4 justify-center mt-8">
              <UButton to="/mountain/sorties" size="lg" color="primary" variant="solid">
                Les sorties
              </UButton>
              <UButton to="/mountain/accompagnatrice" size="lg" color="primary" variant="outline" class="bg-white/10 backdrop-blur">
                L'accompagnatrice
              </UButton>
            </div>
          </div>
          <div class="inline-block bg-white/60 rounded-lg px-4 py-1 shadow">
            <p class="text-xl text-teal-900 font-medium">
              Fontainebleau, Jura, Vosges, Massif Central, Belledonne
            </p>
          </div>
        </div>
        <div v-else class="vertical-text text-3xl font-light text-white relative z-10 drop-shadow">
          Montagne
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const activeSection = ref<'yoga' | 'mountain'>('yoga')
const setActiveSection = (section: 'yoga' | 'mountain') => {
  activeSection.value = section
}
</script>

<style scoped>
.vertical-text {
  writing-mode: vertical-rl;
  text-orientation: mixed;
  letter-spacing: 0.05em;
}

@keyframes fade-in {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in { animation: fade-in 500ms ease-out both; }
</style>