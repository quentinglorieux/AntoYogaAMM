<template>
  <div class="min-h-screen bg-linear-to-br from-blue-50 to-green-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <div class="text-center mb-16">
        <h1 class="text-5xl font-light text-gray-900 mb-4">L'Accompagnatrice en Montagne</h1>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Antonine Rochet, accompagnatrice diplômée
        </p>
      </div>

      <div class="grid md:grid-cols-2 gap-12 items-start">
        <div class="rounded-xl overflow-hidden shadow-2xl">
          <NuxtImg 
            src="/images/mountain2.jpeg" 
            alt="Antonine Rochet - Accompagnatrice en montagne" 
            class="w-full h-[500px] object-cover"
          />
        </div>

        <div class="space-y-6">
          <div class="prose prose-lg max-w-none">
            <h2 class="text-3xl font-light text-gray-900 mb-4">Passionnée de montagne</h2>
            <p class="text-gray-700 leading-relaxed">
              Diplômée accompagnatrice en montagne, je partage ma passion pour la nature et les grands espaces.
            </p>
            <p class="text-gray-700 leading-relaxed">
              Mon expérience me permet de vous guider en toute sécurité dans les massifs du Jura, des Vosges, du Massif Central et de Belledonne.
            </p>
          </div>
          
          <div class="mt-8">
            <UButton to="/mountain/sorties" size="lg" color="primary" variant="solid">
              Voir les sorties
            </UButton>
          </div>
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
