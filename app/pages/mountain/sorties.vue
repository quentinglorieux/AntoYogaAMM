<template>
  <div class="min-h-screen bg-linear-to-br from-blue-50 to-green-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <div class="text-center mb-16">
        <h1 class="text-5xl font-light text-gray-900 mb-4">Les Sorties en Montagne</h1>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Découvrez les différentes sorties et randonnées proposées
        </p>
      </div>

      <div class="grid md:grid-cols-2 gap-12 items-start">
        <div class="space-y-6">
          <div class="prose prose-lg max-w-none">
            <h2 class="text-3xl font-light text-gray-900 mb-4">Explorez la nature</h2>
            <p class="text-gray-700 leading-relaxed">
              Accompagnatrice en montagne diplômée, je vous propose des sorties adaptées à tous les niveaux dans les plus beaux massifs.
            </p>
            <p class="text-gray-700 leading-relaxed">
              Des randonnées d'une journée aux séjours de plusieurs jours, découvrez la montagne en toute sécurité.
            </p>
          </div>
          
          <div class="mt-8">
            <UButton to="/mountain/accompagnatrice" size="lg" color="primary" variant="solid">
              En savoir plus
            </UButton>
          </div>
        </div>

        <div class="rounded-xl overflow-hidden shadow-2xl">
          <NuxtImg 
            src="/images/mountain1.jpg" 
            alt="Sorties en montagne" 
            class="w-full h-[500px] object-cover"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'default'
})
</script>
