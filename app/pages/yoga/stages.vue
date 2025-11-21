<template>
  <div class="min-h-screen bg-gradient-to-br from-green-50 to-teal-100">
    <div class="max-w-6xl mx-auto px-6 py-16 flex flex-col lg:flex-row gap-10">
      <!-- Image latérale -->
      <div class="hidden lg:block lg:w-80 shrink-0">
        <div class="rounded-lg overflow-hidden shadow-lg sticky top-8">
          <NuxtImg src="/images/studio4.jpeg" alt="Studio Yoga" class="w-full h-auto" />
        </div>
      </div>
      <!-- Contenu principal -->
      <div class="flex-1">
        <h1 class="text-5xl font-light text-gray-800 mb-8">Les Stages</h1>
        <div class="prose prose-lg max-w-none">
          <p class="text-xl text-gray-600 leading-relaxed mb-8">
            Des stages de yoga Iyengar pour approfondir votre pratique dans un cadre privilégié.
          </p>

          <div class="space-y-6">
            <div class="bg-white rounded-lg shadow-sm p-8">
              <h2 class="text-2xl font-light text-gray-800 mb-4">Stages week-end</h2>
              <p class="text-gray-600 mb-4">
                Des week-ends intensifs de pratique pour explorer en profondeur les postures et le pranayama.
              </p>
              <ul class="space-y-2 text-gray-600">
                <li>• Durée : 2 jours</li>
                <li>• Horaires : Samedi et dimanche 9h-12h / 14h-17h</li>
                <li>• Tarif : 120€</li>
              </ul>
            </div>

            <div class="bg-white rounded-lg shadow-sm p-8">
              <h2 class="text-2xl font-light text-gray-800 mb-4">Stages semaine</h2>
              <p class="text-gray-600 mb-4">
                Des stages d'une semaine en immersion totale, alliant yoga et montagne.
              </p>
              <ul class="space-y-2 text-gray-600">
                <li>• Durée : 5 jours</li>
                <li>• Programme : Yoga le matin, randonnée l'après-midi</li>
                <li>• Tarif : sur demande</li>
              </ul>
            </div>

            <div class="bg-white rounded-lg shadow-sm p-8">
              <h2 class="text-2xl font-light text-gray-800 mb-4">Stages à thème</h2>
              <p class="text-gray-600 mb-4">
                Des stages ciblés sur des aspects spécifiques du yoga Iyengar.
              </p>
              <ul class="space-y-2 text-gray-600">
                <li>• Inversions</li>
                <li>• Extensions arrière</li>
                <li>• Pranayama</li>
                <li>• Yoga restauratif</li>
              </ul>
            </div>
          </div>

          <div class="mt-12 bg-teal-200 rounded-lg p-6">
            <p class="text-gray-700">
              <strong>Prochains stages :</strong> Consultez régulièrement cette page pour connaître 
              les dates des prochains stages ou contactez-nous directement.
            </p>
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

useSeoMeta({
  title: 'Stages de Yoga Iyengar à Larchant et Fontainebleau | Week-ends & Retraites',
  description: 'Stages de yoga Iyengar en Seine-et-Marne : week-ends intensifs, retraites, ateliers thématiques. Approfondissez votre pratique à Larchant près de Fontainebleau.',
  keywords: 'stage yoga Larchant, stage yoga Fontainebleau, retraite yoga 77, week-end yoga Seine-et-Marne, stage yoga Iyengar, atelier yoga, séjour yoga France'
})
</script>
