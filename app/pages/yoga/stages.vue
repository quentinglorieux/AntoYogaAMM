<template>
  <div class="min-h-screen bg-gradient-to-br from-green-50 to-teal-100 relative overflow-hidden">


    <div class="max-w-6xl mx-auto px-6 py-16 flex flex-col lg:flex-row gap-10 relative z-10">
      <!-- Image latérale -->
      <div class="hidden lg:block lg:w-80 shrink-0">
        <div class="rounded-2xl overflow-hidden shadow-lg sticky top-8">
          <NuxtImg src="/images/studio4.jpeg" alt="Studio Yoga" class="w-full h-auto" />
        </div>
      </div>

      <!-- Contenu principal -->
      <div class="flex-1">
        <h1 class="text-5xl font-light text-gray-800 mb-8">Les Stages</h1>

        <p class="text-xl text-gray-600 leading-relaxed mb-12">
          Des stages de yoga Iyengar pour approfondir votre pratique dans un cadre privilégié.
        </p>

        <div class="space-y-6">
          <!-- Stage à venir -->
          <div class="bg-teal-700 rounded-2xl p-8 shadow-lg border-l-4 border-teal-400 relative overflow-hidden group">
            <div class="relative z-10">
              <div class="inline-flex items-center gap-1.5 bg-teal-500 text-white text-xs font-bold uppercase tracking-widest px-2.5 py-1 rounded-full mb-4">
                <span class="relative flex h-2 w-2">
                  <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-teal-100 opacity-75"></span>
                  <span class="relative inline-flex rounded-full h-2 w-2 bg-white"></span>
                </span>
                Prochain stage
              </div>

              <h2 class="text-3xl font-semibold text-white mb-2">11 et 12 avril 2026</h2>
              <p class="text-teal-50 text-lg mb-6 leading-relaxed">
                Un week-end au Studio de Larchant pour approfondir votre pratique.<br>
                <span class="font-medium bg-teal-800/50 px-2 py-0.5 rounded italic">Horaires : 9h30–12h30 & 15h00–17h00</span>
              </p>

              <div class="flex flex-col sm:flex-row items-center gap-4 pt-2">
                <UButton to="mailto:antonine.rochet@hotmail.fr" icon="i-heroicons-envelope" color="neutral" variant="solid" size="lg">
                  Réserver ma place
                </UButton>
                <span class="text-teal-100 text-sm">
                  ou contactez-moi : <a href="mailto:antonine.rochet@hotmail.fr" class="underline hover:text-white">antonine.rochet@hotmail.fr</a>
                </span>
              </div>
            </div>
          </div>

          <!-- Stage passé -->
          <div class="bg-white/50 backdrop-blur-sm rounded-2xl p-6 border border-gray-200 grayscale opacity-50 hover:opacity-80 transition-opacity">
            <div class="flex justify-between items-start">
              <div>
                <div class="inline-block bg-gray-400 text-white text-[10px] font-bold uppercase tracking-widest px-2 py-0.5 rounded mb-3">
                  Stage précédent
                </div>
                <h3 class="text-xl font-medium text-gray-700 mb-1">9-10 Février 2026</h3>
                <p class="text-gray-500">
                  Thème : Les Inversions — Studio de Larchant
                </p>
              </div>
            </div>
          </div>
        </div>


        <!-- Autres formules -->
        <div class="space-y-6">
          <div class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-sm p-8 relative overflow-hidden">
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

          <div class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-sm p-8 relative overflow-hidden">
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
