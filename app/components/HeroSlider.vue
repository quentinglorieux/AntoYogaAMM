<template>
  <div class="relative h-screen overflow-hidden">
    <div class="flex h-full w-full">
      <!-- Yoga Panel -->
      <div
        class="relative transition-all duration-700 ease-in-out cursor-pointer overflow-hidden flex items-center justify-center shrink-0"
        :class="activeSection === 'yoga' ? 'basis-[92%]' : 'basis-[8%]'"
        @click="setActiveSection('yoga')"
      >
        <NuxtImg src="/images/yoga-bg.jpg" alt="Yoga" class="absolute inset-0 w-full h-full object-cover" />
        <div class="absolute inset-0 bg-linear-to-br from-orange-900/10 to-pink-900/10"></div>

        <div v-if="activeSection === 'yoga'" class="relative z-10 text-center space-y-6 px-8 animate-fade-in">
          <h1 class="text-6xl font-light text-white drop-shadow-lg">Yoga Iyengar</h1>
          <p class="text-xl text-white/90 max-w-2xl mx-auto drop-shadow">
            Découvrez la pratique du yoga Iyengar® avec Antonine Rochet
          </p>
          <div class="flex gap-4 justify-center mt-8">
            <UButton to="/yoga/studio" size="lg" color="primary" variant="solid">
              Découvrir le studio
            </UButton>
            <UButton to="/yoga/cours" size="lg" color="primary" variant="outline" class="bg-white/10 backdrop-blur">
              Les cours
            </UButton>
          </div>
        </div>
        <div v-else class="vertical-text text-3xl font-light text-white relative z-10 drop-shadow">
          Yoga
        </div>
      </div>

      <!-- Mountain Panel -->
      <div
        class="relative transition-all duration-700 ease-in-out cursor-pointer overflow-hidden flex items-center justify-center shrink-0"
        :class="activeSection === 'mountain' ? 'basis-[92%]' : 'basis-[8%]'"
        @click="setActiveSection('mountain')"
      >
        <NuxtImg src="/images/mountain4.jpeg" alt="Montagne" class="absolute inset-0 w-full h-full object-cover" />
        <div class="absolute inset-0 bg-linear-to-br from-stone-800/10 to-stone-900/10"></div>

        <div v-if="activeSection === 'mountain'" class="relative z-10 text-center space-y-6 px-8 animate-fade-in">
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
</style><template>
  <div class="relative h-screen overflow-hidden">
    <div class="flex h-full w-full">
      <!-- Yoga Panel -->
      <div
        class="relative transition-all duration-700 ease-in-out cursor-pointer overflow-hidden flex items-center justify-center flex-shrink-0"
        :class="activeSection === 'yoga' ? 'basis-[90%]' : 'basis-[10%]'"
        @click="setActiveSection('yoga')"
      >
        <NuxtImg src="/images/yoga-bg.jpg" alt="Yoga" class="absolute inset-0 w-full h-full object-cover" />
        <div class="absolute inset-0 bg-gradient-to-br from-orange-900/40 to-pink-900/40"></div>

        <div v-if="activeSection === 'yoga'" class="relative z-10 text-center space-y-6 px-8 animate-fade-in">
          <h1 class="text-6xl font-light text-white drop-shadow-lg">Yoga Iyengar</h1>
          <p class="text-xl text-white/90 max-w-2xl mx-auto drop-shadow">
            Découvrez la pratique du yoga Iyengar® avec Antonine Rochet
          </p>
          <div class="flex gap-4 justify-center mt-8">
            <UButton to="/yoga/studio" size="lg" color="primary" variant="solid">
              Découvrir le studio
            </UButton>
            <UButton to="/yoga/cours" size="lg" color="primary" variant="outline" class="bg-white/10 backdrop-blur">
              Les cours
            </UButton>
          </div>
        </div>
        <div v-else class="vertical-text text-3xl font-light text-white relative z-10 drop-shadow">
          Yoga
        </div>
      </div>

      <!-- Mountain Panel -->
      <div
        class="relative transition-all duration-700 ease-in-out cursor-pointer overflow-hidden flex items-center justify-center flex-shrink-0"
        :class="activeSection === 'mountain' ? 'basis-[90%]' : 'basis-[10%]'"
        @click="setActiveSection('mountain')"
      >
        <NuxtImg src="/images/mountain4.jpeg" alt="Montagne" class="absolute inset-0 w-full h-full object-cover" />
        <div class="absolute inset-0 bg-gradient-to-br from-stone-800/40 to-stone-900/40"></div>

        <div v-if="activeSection === 'mountain'" class="relative z-10 text-center space-y-6 px-8 animate-fade-in">
          <h1 class="text-6xl font-light text-white drop-shadow-lg">Accompagnateur en Montagne</h1>
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
</style><template>
  <div class="relative h-screen overflow-hidden bg-gray-100">
    <!-- Yoga Section -->
    <div
      class="absolute top-0 left-0 h-full z-20 transition-all duration-700 ease-in-out flex items-center justify-center cursor-pointer"
      :class="activeSection === 'yoga' ? 'w-[90%]' : 'w-[10%]'"
      :style="{ background: 'linear-gradient(135deg, #a855f7 0%, #ec4899 100%)' }"
      @click="setActiveSection('yoga')"
    >
      <div v-if="activeSection === 'yoga'" class="text-center space-y-6 px-8 animate-fade-in">
        <h1 class="text-6xl font-light text-white">Yoga Iyengar</h1>
        <p class="text-xl text-white opacity-90 max-w-2xl mx-auto">
          Découvrez la pratique du yoga Iyengar® avec Antonine Rochet
        </p>
        <div class="flex gap-4 justify-center mt-8">
          <UButton
            to="/yoga/studio"
            size="lg"
            variant="solid"
            color="neutral"
          >
            Découvrir le studio
          </UButton>
          <UButton
            to="/yoga/cours"
            size="lg"
            variant="outline"
            class="text-white border-white hover:bg-white/10"
          >
            Les cours
          </UButton>
        </div>
      </div>
      <div v-else class="vertical-text text-3xl font-light text-white">
        Yoga
      </div>
    </div>

    <!-- Mountain Section -->
    <div
      class="absolute top-0 h-full z-10 transition-all duration-700 ease-in-out flex items-center justify-center cursor-pointer"
      :class="activeSection === 'mountain' ? 'w-[90%]' : 'w-[10%]'"
      :style="{ 
        background: 'linear-gradient(135deg, #2563eb 0%, #22c55e 100%)',
        left: activeSection === 'yoga' ? '90%' : '10%'
      }"
      @click="setActiveSection('mountain')"
    >
      <div v-if="activeSection === 'mountain'" class="text-center space-y-6 px-8 animate-fade-in">
        <h1 class="text-6xl font-light text-white">Accompagnateur en Montagne</h1>
        <p class="text-xl text-white opacity-90 max-w-2xl mx-auto">
          Explorez les montagnes avec une accompagnatrice diplômée
        </p>
        <div class="flex gap-4 justify-center mt-8">
          <UButton
            to="/mountain/sorties"
            size="lg"
            variant="solid"
            color="neutral"
          >
            Les sorties
          </UButton>
          <UButton
            to="/mountain/accompagnatrice"
            size="lg"
            variant="outline"
            class="text-white border-white hover:bg-white/10"
          >
            L'accompagnatrice
          </UButton>
        </div>
      </div>
      <div v-else class="vertical-text text-3xl font-light text-white">
        Montagne
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const activeSection = ref<'yoga' | 'mountain'>('yoga')

const setActiveSection = (section: 'yoga' | 'mountain') => {
  <template>
    <div class="relative h-screen overflow-hidden">
      <div class="flex h-full w-full">
        <!-- Yoga Panel -->
        <div
          class="relative transition-all duration-700 ease-in-out cursor-pointer overflow-hidden flex items-center justify-center"
          :class="activeSection === 'yoga' ? 'basis-[90%]' : 'basis-[10%]'"
          @click="setActiveSection('yoga')"
        >
          <NuxtImg src="/images/yoga-bg.jpg" alt="Yoga" class="absolute inset-0 w-full h-full object-cover" />
          <div class="absolute inset-0 bg-gradient-to-br from-orange-900/40 to-pink-900/40"></div>

          <div v-if="activeSection === 'yoga'" class="relative z-10 text-center space-y-6 px-8 animate-fade-in">
            <h1 class="text-6xl font-light text-white drop-shadow-lg">Yoga Iyengar</h1>
            <p class="text-xl text-white/90 max-w-2xl mx-auto drop-shadow">
              Découvrez la pratique du yoga Iyengar® avec Antonine Rochet
            </p>
            <div class="flex gap-4 justify-center mt-8">
              <UButton to="/yoga/studio" size="lg" color="primary" variant="solid">
                Découvrir le studio
              </UButton>
              <UButton to="/yoga/cours" size="lg" color="primary" variant="outline" class="bg-white/10 backdrop-blur">
                Les cours
              </UButton>
            </div>
          </div>
          <div v-else class="vertical-text text-3xl font-light text-white relative z-10 drop-shadow">
            Yoga
          </div>
        </div>

        <!-- Mountain Panel -->
        <div
          class="relative transition-all duration-700 ease-in-out cursor-pointer overflow-hidden flex items-center justify-center"
          :class="activeSection === 'mountain' ? 'basis-[90%]' : 'basis-[10%]'"
          @click="setActiveSection('mountain')"
        >
          <NuxtImg src="/images/mountain4.jpeg" alt="Montagne" class="absolute inset-0 w-full h-full object-cover" />
          <div class="absolute inset-0 bg-gradient-to-br from-stone-800/40 to-stone-900/40"></div>

          <div v-if="activeSection === 'mountain'" class="relative z-10 text-center space-y-6 px-8 animate-fade-in">
            <h1 class="text-6xl font-light text-white drop-shadow-lg">Accompagnateur en Montagne</h1>
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
          <div v-else class="vertical-text text-3xl font-light text-white relative z-10 drop-shadow">
            Montagne
          </div>
        </div>
      </div>
    </div>

  </template>
